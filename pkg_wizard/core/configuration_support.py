import os
from pkg_wizard.utils.file import create_file, read_file, get_file_path


class ConfigurationSupport:

    def __init__(self, package_name, override_files: list = []):
        self.override_files = override_files
        self.folder_name = "configurations"
        self.package_name = package_name

    def create_gitignore(self):
        """Create a .gitignore file for the package.

        This function creates a .gitignore file in the specified package directory with common Python project ignore patterns.

        Raises:
            OSError: If there is an issue creating the .gitignore file.
        """
        file_name, content = read_file(get_file_path(self.folder_name, ".gitignore"))
        overwrite = True if file_name in self.override_files else False
        gitignore_path = os.path.join(file_name)
        create_file(gitignore_path, content, overwrite=overwrite)

    def create_requirements(self):
        """Create a requirements.txt file for the package.

        This function creates a requirements.txt file in the package directory with a default content to add package dependencies.

        Raises:
            OSError: If an error occurs while creating the requirements.txt file.
        """
        file_name, content = read_file(
            get_file_path(self.folder_name, "requirements.txt")
        )
        overwrite = True if file_name in self.override_files else False
        requirements_path = os.path.join(file_name)
        create_file(requirements_path, content, overwrite=overwrite)

    def create_dev_requirements(self):
        """Create a 'dev_requirements.txt' file with specified development dependencies.

        This function generates a 'dev_requirements.txt' file within the package directory containing the required development dependencies for the project.

        Returns:
            None

        Raises:
            FileNotFoundError: If the package directory does not exist.
            OSError: If there is an issue creating the 'dev_requirements.txt' file.
        """
        file_name, content = read_file(
            get_file_path(self.folder_name, "dev_requirements.txt")
        )
        overwrite = True if file_name in self.override_files else False
        dev_requirements_path = os.path.join(file_name)
        create_file(dev_requirements_path, content, overwrite=overwrite)

    def create_readme(self):
        """Generate a README file for the Python package.

        Creates a README.md file in the package directory with information about the package, its features, installation instructions, contribution guidelines, license details, and contact information.

        Returns:
            None

        Raises:
            FileNotFoundError: If the package directory does not exist.
            PermissionError: If the user does not have permission to create the README file.
        """
        file_name, content = read_file(get_file_path(self.folder_name, "readme.md"))
        content = content.replace("{{package_name}}", self.package_name)
        overwrite = True if file_name in self.override_files else False
        readme_path = os.path.join(file_name)
        create_file(readme_path, content, overwrite=overwrite)

    def create_setup_file(self):
        """Creates a setup.py file for the package.

        This function generates a setup.py file with the necessary metadata for the package setup. It includes information such as package name, version, author details, description, dependencies, entry points, and classifiers.

        Returns:
            None

        Raises:
            FileNotFoundError: If the README.md file is not found.
            OSError: If an error occurs while creating the setup.py file.
        """
        file_name, content = read_file(get_file_path(self.folder_name, "setup.py"))
        content = content.replace("{{package_name}}", self.package_name)
        overwrite = True if file_name in self.override_files else False
        setup_path = os.path.join(file_name)
        create_file(setup_path, content, overwrite=overwrite)

    def create_files(self):
        """Create configuration files for the package.

        This function creates configuration files for the package, including .gitignore, requirements.txt, dev_requirements.txt, README.md, and setup.py.

        Returns:
            None

        Raises:
            FileNotFoundError: If any of the configuration files are not found.
            OSError: If there is an issue creating the configuration files.
        """
        self.create_gitignore()
        self.create_requirements()
        self.create_dev_requirements()
        self.create_readme()
        self.create_setup_file()
