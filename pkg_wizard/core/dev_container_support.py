from pkg_wizard.util.file_creator import FileCreator
from pkg_wizard.content import (
    devcontainer_json_content,
    post_create_sh_content,
    devcontainer_env_content,
)
import os


class DevContainerSupport:

    def __init__(self, override_files: list):
        self.file_creator = FileCreator()
        self.override_files = override_files

    def create_devcontainer_json(self):
        """
        Creates a devcontainer.json file for Visual Studio Code Remote - Containers.

        This function generates a devcontainer.json file with specific settings for a Visual Studio Code Remote - Containers development environment.

        Returns:
            None

        Raises:
            None
        """
        file_name = devcontainer_json_content.file_name
        override_files = self.override_files
        devcontainer_dir = os.path.join(".devcontainer")
        devcontainer_json_path = os.path.join(devcontainer_dir, file_name)
        content = devcontainer_json_content.content
        self.file_creator.create_file(
            devcontainer_json_path, content, override=override_files
        )

    def create_post_create_sh(self):
        """
        Creates a post-create.sh file for Visual Studio Code Remote - Containers.

        This function generates a post-create.sh file with specific settings for a Visual Studio Code Remote - Containers development environment.

        Returns:
            None

        Raises:
            None
        """
        file_name = post_create_sh_content.file_name
        override_files = self.override_files
        devcontainer_dir = os.path.join(".devcontainer")
        post_create_sh_path = os.path.join(devcontainer_dir, file_name)
        content = post_create_sh_content.content
        self.file_creator.create_file(
            post_create_sh_path, content, override=override_files
        )

    def create_dev_container_env(self):
        """Creates a devcontainer.env directory in devcontainer.json."""
        file_name = devcontainer_env_content.file_name
        devcontainer_dir = os.path.join(".devcontainer")
        devcontainer_env_path = os.path.join(devcontainer_dir, file_name)
        content = devcontainer_env_content.content
        self.file_creator.create_file(
            devcontainer_env_path, content, override=self.override_files
        )
