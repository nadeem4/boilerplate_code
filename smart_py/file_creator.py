import os

class FileCreator:
    def __init__(self, package_name, docker_image, override_files=[]):
        self.package_name = package_name
        self.docker_image = docker_image
        self.override_files = override_files

    def create_file(self, file_path, content):
        if not os.path.exists(file_path) or file_path in self.override_files:
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created file: {file_path}")
        else:
            print(f"Skipped file (already exists): {file_path}")

    def create_init_file(self):
        init_path = os.path.join(self.package_name, self.package_name, '__init__.py')
        content = f'"""Initialize the {self.package_name} package."""\n'
        self.create_file(init_path, content)

    def create_setup_file(self):
        setup_path = os.path.join(self.package_name, 'setup.py')
        content = f'''from setuptools import setup, find_packages

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
'''
        self.create_file(setup_path, content)

    def create_readme(self):
        readme_path = os.path.join(self.package_name, 'README.md')
        content = f'''# {self.package_name}

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
'''
        self.create_file(readme_path, content)


    def create_license(self):
        license_path = os.path.join(self.package_name, 'LICENSE')
        content = 'MIT License\n\nCopyright (c) 2023 Your Name'
        self.create_file(license_path, content)

    def create_test_init(self):
        test_init_path = os.path.join(self.package_name, 'tests', '__init__.py')
        content = f'"""Initialize the test module for {self.package_name} package."""\n'
        self.create_file(test_init_path, content)

    def create_gitignore(self):
        gitignore_path = os.path.join(self.package_name, '.gitignore')
        content = '*.pyc\n__pycache__/\nbuild/\ndist/\n*.egg-info/\n'
        self.create_file(gitignore_path, content)

    def create_requirements(self):
        requirements_path = os.path.join(self.package_name, 'requirements.txt')
        content = '# Add your package dependencies here\n'
        self.create_file(requirements_path, content)

    def create_dev_requirements(self):
        dev_requirements_path = os.path.join(self.package_name, 'dev_requirements.txt')
        content = '''# Development dependencies
pre-commit==3.8.0
black==24.10.0
docformatter==1.4
flake8>=4.0.1,<5.0.0
pytest>=7.2.0,<8.0.0
docu_gen
'''
        self.create_file(dev_requirements_path, content)

    def create_devcontainer_json(self):
        devcontainer_dir = os.path.join(self.package_name, '.devcontainer')
        devcontainer_json_path = os.path.join(devcontainer_dir, 'devcontainer.json')
        content = '''{{
    "name": "{package_name} Development Container",
    "dockerFile": "Dockerfile",
    "context": "..",
    "settings": {{
        "terminal.integrated.shell.linux": "/bin/bash"
    }},
    "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
    ],
    "forwardPorts": [],
    "postCreateCommand": "pip install -r dev_requirements.txt"
}}
'''.format(package_name=self.package_name)
        self.create_file(devcontainer_json_path, content)

    def create_dockerfile(self):
        devcontainer_dir = os.path.join(self.package_name, '.devcontainer')
        dockerfile_path = os.path.join(devcontainer_dir, 'Dockerfile')
        content = f'''FROM {self.docker_image}

# Install pip and upgrade it
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /workspace

# Copy the current directory contents into the container
COPY . /workspace

# Install the package in editable mode with dev dependencies
RUN pip install -e .[dev]
'''
        self.create_file(dockerfile_path, content)

    def create_publish_yml(self):
        workflows_dir = os.path.join(self.package_name, '.github', 'workflows')
        publish_yml_path = os.path.join(workflows_dir, 'publish.yml')
        content = '''name: Publish Python Package

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
'''
        self.create_file(publish_yml_path, content)

    def create_pre_commit_config(self):
        pre_commit_config_path = os.path.join(self.package_name, '.pre-commit-config.yaml')
        content = '''
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
    rev: v3.8.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: debug-statements
      - id: check-merge-conflict
'''
        self.create_file(pre_commit_config_path, content)
