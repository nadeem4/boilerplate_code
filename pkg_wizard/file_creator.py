import os
from pkg_wizard.content import setup_file_content
from pkg_wizard.content import pre_commit_config_content
from pkg_wizard.content import publish_yaml_content
from pkg_wizard.content import post_create_sh_content
from pkg_wizard.content import dev_requirements_txt_content
from pkg_wizard.content import gitignore_content
from pkg_wizard.content import readme_content
from pkg_wizard.content import devcontainer_json_content
from pkg_wizard.content import dockerfile_content
from pkg_wizard.content import post_create_sh_content
from pkg_wizard.content import requirements_txt_content


class FileCreator:
    """A class that creates files for a specified package using a given Docker image."""

    def __init__(self, package_name, docker_image, override_files=[]):
        """Initialize a Package object with the provided package name, Docker image, and
        optional override files.

        Args:
            package_name (str): The name of the package.
            docker_image (str): The Docker image associated with the package.
            override_files (list, optional): A list of files to override in the package. Defaults to an empty list.

        Raises:
            None

        Returns:
            None
        """
        self.package_name = package_name
        self.docker_image = docker_image
        self.override_files = override_files

    def create_file(self, file_path, content):
        """Create a file at the specified path with the given content.

        Args:
            file_path (str): The path where the file will be created.
            content (str): The content to be written to the file.

        Raises:
            None

        Returns:
            None
        """
        if not os.path.exists(file_path) or file_path in self.override_files:
            with open(file_path, "w") as f:
                f.write(content)
            print(f"Created file: {file_path}")
        else:
            print(f"Skipped file (already exists): {file_path}")
