
# Boilerplate Code Generator

This repository provides a Python script that automates the creation of a standardized package structure for Python projects.
It facilitates the setup of essential directories and files, streamlining the initial phase of project development.

## Features

- **Automated Directory Creation**: Generates a hierarchical folder structure, including main package directories, test folders, and configuration directories.
- **Essential File Generation**: Creates foundational files such as `__init__.py`, `setup.py`, `README.md`, `LICENSE`, and `.gitignore`.
- **Development Environment Setup**: Sets up development dependencies and configurations, including `requirements.txt`, `dev_requirements.txt`, and pre-commit hooks.
- **Docker and DevContainer Support**: Provides Dockerfile and DevContainer configurations for containerized development environments.
- **CI/CD Workflow Integration**: Includes GitHub Actions workflow files for continuous integration and deployment.

## Installation

```sh
pip install pkg-wizard
```

## Usage

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/nadeem4/boilerplate_code.git
   ```

2. **Navigate to the Directory**:

   ```sh
   cd boilerplate_code
   ```

3. **Install Package**

   ```sh
   pip install .
   ```

4. **Run the Script**:

   ```sh
   gps <package_name> [--docker_image <docker_image>] [--override <file1> <file2> ...]
   ```

   - `<package_name>`: Name of the package to create.
   - `--docker_image`: (Optional) Docker image to use (default: `python:3.9-slim`).
   - `--override`: (Optional) List of files to override if they already exist.

   **Example**:

   ```sh
   gps my_package --docker_image python:3.10-slim --override README.md LICENSE
   ```

## Requirements

- **Python 3.6 or higher**: Ensure Python is installed on your system.
- **Setuptools**: Used for packaging Python projects.
- **Git**: For version control and repository management.

## Development Setup

1. **Install Development Dependencies**:

   ```sh
   pip install -r dev_requirements.txt
   ```

2. **Initialize Pre-Commit Hooks**:

   ```sh
   pre-commit install
   ```

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for your feature or bug fix, and submit a pull request. Ensure your code adheres to the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please reach out to [codewithnk@gmail.com](mailto:codewithnk@gmail.com).
