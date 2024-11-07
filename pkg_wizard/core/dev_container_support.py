from pkg_wizard.utils.file import create_file, read_file, get_file_path
import os


class DevContainerSupport:

    def __init__(self, override_files: list):
        self.override_files = override_files
        self.folder_name = "devcontainer"

    def create_devcontainer_json(self):
        """
        Creates a devcontainer.json file for Visual Studio Code Remote - Containers.

        This function generates a devcontainer.json file with specific settings for a Visual Studio Code Remote - Containers development environment.

        Returns:
            None

        Raises:
            None
        """
        file_name, content = read_file(
            get_file_path(self.folder_name, "devcontainer.json")
        )
        override_files = self.override_files
        devcontainer_dir = os.path.join(".devcontainer")
        devcontainer_json_path = os.path.join(devcontainer_dir, file_name)
        create_file(devcontainer_json_path, content, override=override_files)

    def create_post_create_sh(self):
        """
        Creates a post-create.sh file for Visual Studio Code Remote - Containers.

        This function generates a post-create.sh file with specific settings for a Visual Studio Code Remote - Containers development environment.

        Returns:
            None

        Raises:
            None
        """
        file_name, content = read_file(
            get_file_path(self.folder_name, "post-create.sh")
        )
        override_files = self.override_files
        devcontainer_dir = os.path.join(".devcontainer")
        post_create_sh_path = os.path.join(devcontainer_dir, file_name)
        create_file(post_create_sh_path, content, override=override_files)

    def create_dev_container_env(self):
        """Creates a devcontainer.env directory in devcontainer.json."""
        file_name, content = read_file(
            get_file_path(self.folder_name, "devcontainer.env")
        )
        devcontainer_dir = os.path.join(".devcontainer")
        devcontainer_env_path = os.path.join(devcontainer_dir, file_name)
        create_file(devcontainer_env_path, content, override=self.override_files)

    def create_files(self):
        """Create all files for the devcontainer support."""
        self.create_devcontainer_json()
        self.create_post_create_sh()
        self.create_dev_container_env()
