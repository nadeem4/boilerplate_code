import os


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
        setup_path = os.path.join(self.package_name, "setup.py")
        content = f"""from setuptools import setup, find_packages

setup(
    name='{self.package_name}',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Your Name',
    author_email='your.email@example.com',
    description='A description of your package.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/{self.package_name}',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    extras_require={{
        'dev': [
            'pytest',
            'flake8',
            # Add other development dependencies here
        ],
    }},
    entry_points={{
        'console_scripts': [
            '{self.package_name}={self.package_name}.cli:main',
        ],
    }},
)
"""
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
        readme_path = os.path.join(self.package_name, "README.md")
        content = f"""# {self.package_name}

## Overview

{self.package_name} is a Python package that provides functionality for [describe the purpose of the package here]. This package is designed to help [target audience] achieve [specific goals].

## Features

- Feature 1: [Describe feature 1]
- Feature 2: [Describe feature 2]
- Feature 3: [Describe feature 3]

## Installation

To install the package, use the following command:

```
pip install {self.package_name}
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please reach out to [your.email@example.com].
"""
        self.create_file(readme_path, content)

    def create_license(self):
        """Create a license file for the package.

        This function generates a license file with the MIT License text and copyright information.

        Returns:
            None

        Raises:
            OSError: If an error occurs while creating the license file.
        """
        license_path = os.path.join(self.package_name, "LICENSE")
        content = "MIT License\n\nCopyright (c) 2023 Your Name"
        self.create_file(license_path, content)

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
        gitignore_path = os.path.join(self.package_name, ".gitignore")
        content = "*.pyc\n__pycache__/\nbuild/\ndist/\n*.egg-info/\n"
        self.create_file(gitignore_path, content)

    def create_requirements(self):
        """Create a requirements.txt file for the package.

        This function creates a requirements.txt file in the package directory with a default content to add package dependencies.

        Raises:
            OSError: If an error occurs while creating the requirements.txt file.
        """
        requirements_path = os.path.join(self.package_name, "requirements.txt")
        content = "# Add your package dependencies here\n"
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
        dev_requirements_path = os.path.join(self.package_name, "dev_requirements.txt")
        content = """# Development dependencies
                    pre-commit==3.8.0
                    black==24.10.0
                    docformatter==1.4
                    flake8>=4.0.1,<5.0.0
                    pytest>=7.2.0,<8.0.0
                    docu_gen
                """
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
        devcontainer_json_path = os.path.join(devcontainer_dir, "devcontainer.json")
        content = f"""{{
    "name": "{self.package_name}",
    "dockerFile": "Dockerfile",
    "context": "..",
    "customizations": {{
        "vscode": {{
            "extensions": [
                "ms-python.python",
                "ms-python.vscode-pylance",
                "mhutchie.git-graph",
                "eamodio.gitlens",
                "GitHub.copilot-chat",
                "GitHub.copilot"
            ]
        }}
    }},
    "forwardPorts": [],
    "postCreateCommand": "pip install -r dev_requirements.txt",
    "features": {{
        "ghcr.io/devcontainers/features/docker-in-docker:2": {{
            "moby": true,
            "azureDnsAutoDetection": true,
            "installDockerBuildx": true,
            "installDockerComposeSwitch": true,
            "version": "latest",
            "dockerDashComposeVersion": "latest"
        }},
        "ghcr.io/devcontainers/features/git:1": {{
            "ppa": true,
            "version": "latest"
        }},
        "ghcr.io/devcontainers/features/github-cli:1": {{
            "installDirectlyFromGitHubRelease": true,
            "version": "latest"
        }}
    }}
}}
"""
        self.create_file(devcontainer_json_path, content)

    def create_dockerfile(self):
        """Create a Dockerfile for the project.

        This function generates a Dockerfile in the project's .devcontainer directory with the specified Docker image, installs pip and upgrades it, sets the working directory to /workspace, copies the project's contents into the container, and installs the package in editable mode with dev dependencies.

        Raises:
            None
        """
        devcontainer_dir = os.path.join(self.package_name, ".devcontainer")
        dockerfile_path = os.path.join(devcontainer_dir, "Dockerfile")
        content = f"""FROM {self.docker_image}

# Install pip and upgrade it
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /workspace

# Copy the current directory contents into the container
COPY . /workspace

# Install the package in editable mode with dev dependencies
RUN pip install -e .[dev]
"""
        self.create_file(dockerfile_path, content)

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
        publish_yml_path = os.path.join(workflows_dir, "publish.yml")
        content = """name: Publish Python Package

on:
  push:
    tags:
      - '*.*.*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install setuptools wheel

      - name: Build package
        run: |
          python setup.py sdist bdist_wheel

      - name: Publish package
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          password: ${{ secrets.PYPI_API_TOKEN }}
"""
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
            self.package_name, ".pre-commit-config.yaml"
        )
        content = """
repos:
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5  # Specify the version you want
    hooks:
      - id: docformatter
        args:
          - --in-place
          - --recursive
          - --wrap-summaries=88
          - --wrap-descriptions=88
        files: \.py$

  - repo: https://github.com/psf/black
    rev: 24.10.0  # Specify the version of black you want
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: debug-statements
      - id: check-merge-conflict
"""
        self.create_file(pre_commit_config_path, content)
