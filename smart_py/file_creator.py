import os
from smart_py.content import setup_file_content
from smart_py.content import pre_commit_config_content
from smart_py.content import publish_yaml_content
from smart_py.content import post_create_sh_content
from smart_py.content import dev_requirements_txt_content
from smart_py.content import gitignore_content
from smart_py.content import readme_content
from smart_py.content import devcontainer_json_content
from smart_py.content import dockerfile_content
from smart_py.content import post_create_sh_content
from smart_py.content import requirements_txt_content


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

    def create_init_file(self):
        """Create an __init__.py file to initialize the package.

        This function generates an __init__.py file within the package directory to initialize the package.

        Raises:
            OSError: If there are issues creating the file.
        """
        init_path = os.path.join(self.package_name, self.package_name, "__init__.py")
        content = f'"""Initialize the {self.package_name} package."""\n'
        self.create_file(init_path, content)

    def create_setup_file(self):
        """Creates a setup.py file for the package.

        This function generates a setup.py file with the necessary metadata for the package setup. It includes information such as package name, version, author details, description, dependencies, entry points, and classifiers.

        Returns:
            None

        Raises:
            FileNotFoundError: If the README.md file is not found.
            OSError: If an error occurs while creating the setup.py file.
        """
        setup_path = os.path.join(self.package_name, setup_file_content.file_name)
        content = setup_file_content.content
        self.create_file(setup_path, content)

    def create_readme(self):
        """Generate a README file for the Python package.

        Creates a README.md file in the package directory with information about the package, its features, installation instructions, contribution guidelines, license details, and contact information.

        Returns:
            None

        Raises:
            FileNotFoundError: If the package directory does not exist.
            PermissionError: If the user does not have permission to create the README file.
        """
        readme_path = os.path.join(self.package_name, readme_content.file_name)
        content = readme_content.content
        self.create_file(readme_path, content)

    def create_test_init(self):
        """Create an __init__.py file for the tests module.

        Args:
            self: The instance of the class calling the method.
                It should have the attributes 'package_name' and 'create_file'.

        Returns:
            None

        Raises:
            FileNotFoundError: If the specified path for the __init__.py file does not exist.
        """
        test_init_path = os.path.join(self.package_name, "tests", "__init__.py")
        content = f'"""Initialize the test module for {self.package_name} package."""\n'
        self.create_file(test_init_path, content)

    def create_gitignore(self):
        """Create a .gitignore file for the package.

        This function creates a .gitignore file in the specified package directory with common Python project ignore patterns.

        Raises:
            OSError: If there is an issue creating the .gitignore file.
        """
        gitignore_path = os.path.join(self.package_name, gitignore_content.file_name)
        content = gitignore_content.content
        self.create_file(gitignore_path, content)

    def create_requirements(self):
        """Create a requirements.txt file for the package.

        This function creates a requirements.txt file in the package directory with a default content to add package dependencies.

        Raises:
            OSError: If an error occurs while creating the requirements.txt file.
        """
        requirements_path = os.path.join(
            self.package_name, requirements_txt_content.file_name
        )
        content = requirements_txt_content.content
        self.create_file(requirements_path, content)

    def create_dev_requirements(self):
        """Create a 'dev_requirements.txt' file with specified development dependencies.

        This function generates a 'dev_requirements.txt' file within the package directory containing the required development dependencies for the project.

        Returns:
            None

        Raises:
            FileNotFoundError: If the package directory does not exist.
            OSError: If there is an issue creating the 'dev_requirements.txt' file.
        """
        dev_requirements_path = os.path.join(
            self.package_name, dev_requirements_txt_content.file_name
        )
        content = dev_requirements_txt_content.content
        self.create_file(dev_requirements_path, content)

    def create_devcontainer_json(self):
        """
        Creates a devcontainer.json file for Visual Studio Code Remote - Containers.

        This function generates a devcontainer.json file with specific settings for a Visual Studio Code Remote - Containers development environment.

        Returns:
            None

        Raises:
            None
        """
        devcontainer_dir = os.path.join(self.package_name, ".devcontainer")
        devcontainer_json_path = os.path.join(
            devcontainer_dir, devcontainer_json_content.file_name
        )
        content = devcontainer_json_content.content
        self.create_file(devcontainer_json_path, content)

    def create_dockerfile(self):
        """Create a Dockerfile for the project.

        This function generates a Dockerfile in the project's .devcontainer directory with the specified Docker image, installs pip and upgrades it, sets the working directory to /workspace, copies the project's contents into the container, and installs the package in editable mode with dev dependencies.

        Raises:
            None
        """
        devcontainer_dir = os.path.join(self.package_name, ".devcontainer")
        dockerfile_path = os.path.join(devcontainer_dir, dockerfile_content.file_name)
        content = dockerfile_content.content
        self.create_file(dockerfile_path, content)

    def create_post_create_sh(self):
        """Create a requirements.txt file for the package.

        This function creates a requirements.txt file in the package directory with a default content to add package dependencies.

        Raises:
            OSError: If an error occurs while creating the requirements.txt file.
        """
        devcontainer_dir = os.path.join(self.package_name, ".devcontainer")
        post_create = os.path.join(devcontainer_dir, post_create_sh_content.file_name)
        content = post_create_sh_content.content
        self.create_file(post_create, content)

    def create_publish_yml(self):
        """Creates a publish.yml file for GitHub Actions workflow to publish a Python
        package.

        The function generates the content for the publish.yml file, which includes the workflow configuration for building and publishing a Python package to PyPI.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the publish.yml file.
        """
        workflows_dir = os.path.join(self.package_name, ".github", "workflows")
        publish_yml_path = os.path.join(workflows_dir, publish_yaml_content.file_name)
        content = publish_yaml_content.content
        self.create_file(publish_yml_path, content)

    def create_pre_commit_config(self):
        """Creates a pre-commit configuration file for the project.

        This function generates a .pre-commit-config.yaml file with specific repositories, hooks, and configurations for pre-commit checks.

        Returns:
            None

        Raises:
            None
        """
        pre_commit_config_path = os.path.join(
            self.package_name, pre_commit_config_content.file_name
        )
        content = pre_commit_config_content.content
        self.create_file(pre_commit_config_path, content)
