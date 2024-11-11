import threading
from openai import OpenAI
from groq import Groq
from docu_gen.examples import python
from .env_apikey_handler import EnvAPIKeyHandler
from .azurekeyvault_apikey_handler import AzureKeyVaultAPIKeyHandler
import sys
import os
from .constant import INFERENCE_CLIENTS
import logging
from .llm_util import generate_message_for_llm, post_process_response_from_llm

logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.CRITICAL)


class LLM:
    """A class that represents a Language Model (LLM) supporting multiple providers with
    streaming capabilities."""

    def __init__(self, stream=True):
        """Initialize a Model object with the specified model name and model family.

        Args:
            model_name (str): The name of the model. Defaults to value from AI_MODEL.
            model_family (str): The family to which the model belongs. Defaults to value from AI_MODEL.
            stream (bool): Whether to enable response streaming. Defaults to True.

        Returns:
            None

        Raises:
            ValueError: If the specified model family is not supported.
            stream (bool): Whether to enable response streaming. Defaults to True.
        """
        self.stream = stream
        self._initialize_client()

    def _initialize_client(self):
        """Initialize the LLM client based on the specified model family.

        Returns:
            None

        Raises:
            ValueError: If the model family is not supported or API key retrieval fails.
        """
        handler_chain = EnvAPIKeyHandler(successor=AzureKeyVaultAPIKeyHandler())
        d = handler_chain.handle()
        api_key = d.get("api_key") if d else None
        inference_client = d.get("inference_client") if d else None
        self.model_name = d.get("model_name") if d else None

        if not api_key:
            logging.error(
                f"Failed to retrieve the {inference_client.upper()} API key from any source.",
            )
            sys.exit(1)

        # Initialize appropriate client
        if inference_client == "openai":
            self.client = OpenAI(api_key=api_key)
        elif inference_client == "groq":
            self.client = Groq(api_key=api_key)
        else:
            raise ValueError(
                f"Inference Client: {inference_client} not supported. Allowed values: {INFERENCE_CLIENTS}"
            )

    def _process_streaming_response(self, response):
        """Process streaming response from the LLM.

        Args:
            response: The streaming response object from the LLM.

        Returns:
            str: The complete generated docstring.
        """
        collected_content = []
        for chunk in response:
            if chunk.choices[0].finish_reason is None:
                # Get the content from the chunk
                content = chunk.choices[0].delta.content
                if content is not None:
                    collected_content.append(content)
                    # Optional: Print the chunk as it comes in
                    # logging.info(content, end='', flush=True)

        return "".join(collected_content)

    def get_response(self, messages):
        """Get response from the LLM.

        Args:
            messages (list): List of messages to send to the LLM.

        Returns:
            str: The response from the LLM.
        """
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            max_tokens=1000,
            temperature=0,
            stream=self.stream,
        )

        if self.stream:
            raw_response = self._process_streaming_response(response)
        else:
            raw_response = response.choices[0].message.content.strip()

        return post_process_response_from_llm(raw_response)
