# TODO: update this function to return the correct messages for the LLM
def generate_message_for_llm():
    system_message = "Please provide a brief description of the code snippet."
    user_message = "Please provide a brief description of the code snippet."
    messages = [
        {
            "role": "system",
            "content": system_message,
        },
        {
            "role": "user",
            "content": user_message,
        },
    ]
    return messages


# TODO: apply post processing to the response from the LLM
def post_process_response_from_llm(raw_response):
    response = raw_response
    return response
