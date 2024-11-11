from pkg_wizard.utils.file import create_file, read_file, get_file_path
import os


class LLMSupport:
    def __init__(self, package_name, override_files: list = []):
        self.override_files = override_files
        self.folder_name = "llm"
        self.llm_dir = os.path.join(package_name, "llm")

    def create_few_shot_learning_py(self):
        """Creates the few_shot_learning.py file for LLM support.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the few_shot_learning.py file.
        """
        file_name, content = read_file(
            get_file_path(self.folder_name, "few_shot_learning.py")
        )
        overwrite = file_name in self.override_files
        few_shot_path = os.path.join(self.llm_dir, file_name)
        create_file(few_shot_path, content, overwrite=overwrite)

    def create_apikey_handler_py(self):
        """Creates the apikey_handler.py file for API key management.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the apikey_handler.py file.
        """
        file_name, content = read_file(
            get_file_path(self.folder_name, "apikey_handler.py")
        )
        overwrite = file_name in self.override_files
        apikey_handler_path = os.path.join(self.llm_dir, file_name)
        create_file(apikey_handler_path, content, overwrite=overwrite)

    def create_azurekeyvault_apikey_handler_py(self):
        """Creates the azurekeyvault_apikey_handler.py file for Azure Key Vault API key
        management.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the azurekeyvault_apikey_handler.py file.
        """
        file_name, content = read_file(
            get_file_path(self.folder_name, "azurekeyvault_apikey_handler.py")
        )
        overwrite = file_name in self.override_files
        azure_apikey_handler_path = os.path.join(self.llm_dir, file_name)
        create_file(azure_apikey_handler_path, content, overwrite=overwrite)

    def create_env_apikey_handler_py(self):
        """Creates the env_apikey_handler.py file for environment variable API key
        management.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the env_apikey_handler.py file.
        """
        file_name, content = read_file(
            get_file_path(self.folder_name, "env_apikey_handler.py")
        )
        overwrite = file_name in self.override_files
        env_apikey_handler_path = os.path.join(self.llm_dir, file_name)
        create_file(env_apikey_handler_path, content, overwrite=overwrite)

    def create_llm_util_py(self):
        """Creates the llm_util.py file for LLM utilities.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the llm_util.py file.
        """
        file_name, content = read_file(get_file_path(self.folder_name, "llm_util.py"))
        overwrite = file_name in self.override_files
        llm_util_path = os.path.join(self.llm_dir, file_name)
        create_file(llm_util_path, content, overwrite=overwrite)

    def create_llm_py(self):
        """Creates the llm.py file for LLM functionalities.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the llm.py file.
        """
        file_name, content = read_file(get_file_path(self.folder_name, "llm.py"))
        overwrite = file_name in self.override_files
        llm_path = os.path.join(self.llm_dir, file_name)
        create_file(llm_path, content, overwrite=overwrite)

    def create_constant_py(self):
        """Creates the llm.py file for LLM functionalities.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the llm.py file.
        """
        file_name, content = read_file(get_file_path(self.folder_name, "constant.py"))
        overwrite = file_name in self.override_files
        llm_path = os.path.join(self.llm_dir, file_name)
        create_file(llm_path, content, overwrite=overwrite)

    def create_init_file(self):
        """Create an __init__.py file to initialize the package.

        This function generates an __init__.py file within the package directory to initialize the package.

        Raises:
            OSError: If there are issues creating the file.
        """
        init_path = os.path.join(self.llm_dir, "__init__.py")
        content = f'"""Initialize the LLM package."""\n'
        create_file(init_path, content)

    def create_files(self):
        self.create_few_shot_learning_py()
        self.create_apikey_handler_py()
        self.create_azurekeyvault_apikey_handler_py()
        self.create_env_apikey_handler_py()
        self.create_llm_util_py()
        self.create_llm_py()
        self.create_init_file()
        self.create_constant_py()
