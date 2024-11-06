import os
from pkg_wizard.content import (
    gitignore_content,
    requirements_txt_content,
    dev_requirements_txt_content,
    readme_content,
    setup_file_content,
)
from pkg_wizard.util.file_creator import FileCreator


class ConfigurationSupport:

    def __init__(self, override_files: list):
        self.file_creator = FileCreator()
        self.override_files = override_files

    def create_gitignore(self):
        """Create a .gitignore file for the package.

        This function creates a .gitignore file in the specified package directory with common Python project ignore patterns.

        Raises:
            OSError: If there is an issue creating the .gitignore file.
        """
        override = True if gitignore_content.file_name in self.override_files else False
        gitignore_path = os.path.join(gitignore_content.file_name)
        content = gitignore_content.content
        self.file_creator.create_file(gitignore_path, content, override=override)

    def create_requirements(self):
        """Create a requirements.txt file for the package.

        This function creates a requirements.txt file in the package directory with a default content to add package dependencies.

        Raises:
            OSError: If an error occurs while creating the requirements.txt file.
        """
        file_name = requirements_txt_content.file_name
        override = True if file_name in self.override_files else False
        requirements_path = os.path.join(file_name)
        content = requirements_txt_content.content
        self.file_creator.create_file(requirements_path, content, override=override)

    def create_dev_requirements(self):
        """Create a 'dev_requirements.txt' file with specified development dependencies.

        This function generates a 'dev_requirements.txt' file within the package directory containing the required development dependencies for the project.

        Returns:
            None

        Raises:
            FileNotFoundError: If the package directory does not exist.
            OSError: If there is an issue creating the 'dev_requirements.txt' file.
        """
        file_name = dev_requirements_txt_content.file_name
        override = True if file_name in self.override_files else False
        dev_requirements_path = os.path.join(dev_requirements_txt_content.file_name)
        content = dev_requirements_txt_content.content
        self.file_creator.create_file(dev_requirements_path, content, override=override)

    def create_readme(self):
        """Generate a README file for the Python package.

        Creates a README.md file in the package directory with information about the package, its features, installation instructions, contribution guidelines, license details, and contact information.

        Returns:
            None

        Raises:
            FileNotFoundError: If the package directory does not exist.
            PermissionError: If the user does not have permission to create the README file.
        """
        file_name = readme_content.file_name
        override = True if file_name in self.override_files else False
        readme_path = os.path.join(file_name)
        content = readme_content.content
        self.file_creator.create_file(readme_path, content, override=override)

    def create_setup_file(self):
        """Creates a setup.py file for the package.

        This function generates a setup.py file with the necessary metadata for the package setup. It includes information such as package name, version, author details, description, dependencies, entry points, and classifiers.

        Returns:
            None

        Raises:
            FileNotFoundError: If the README.md file is not found.
            OSError: If an error occurs while creating the setup.py file.
        """
        file_name = setup_file_content.file_name
        override = True if file_name in self.override_files else False
        setup_path = os.path.join(file_name)
        content = setup_file_content.content
        self.file_creator.create_file(setup_path, content, override=override)
