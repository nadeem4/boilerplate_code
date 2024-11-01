import argparse
import os


def print_pypi_instructions():
    """Print instructions for publishing a package to PyPI.

    This function prints a set of instructions detailing the steps required to publish a package to PyPI. It provides guidance on generating a PyPI API token and adding it as a GitHub secret for use in the publishing process.

    No parameters are required for this function.

    Returns:
        None

    Raises:
        No exceptions are raised by this function.
    """
    print(
        """
To publish your package, you need to create a PyPI API token and add it as a GitHub secret:

Step 1: Generate a PyPI API Token
1. Log in to your PyPI account: https://pypi.org/
2. Go to 'Account settings' and create a new API token.
3. Copy the token immediately as it will not be shown again.

Step 2: Save the API Token as a GitHub Secret
1. Go to your GitHub repository.
2. Navigate to 'Settings' > 'Secrets and variables' > 'Actions'.
3. Click 'New repository secret'.
4. Name the secret 'PYPI_API_TOKEN' and paste the token.
5. Click 'Add secret'.

The GitHub Actions workflow will use this secret to publish your package to PyPI.
"""
    )


def main():
    """Generate a Python package structure with optional Docker support.

    Args:
        package_name (str): The name of the package to create.
        docker_image (str): The Docker image to use (default: python:3.9-slim).

    Returns:
        None

    Raises:
        argparse.ArgumentError: If there are issues with parsing command-line arguments.
        FileNotFoundError: If any file creation operation fails.
        OSError: If there are issues with directory creation or file writing.
    """
    parser = argparse.ArgumentParser(
        description="Generate a Python package structure with optional Docker support."
    )
    parser.add_argument(
        "package_name", type=str, help="The name of the package to create."
    )
    parser.add_argument(
        "--docker_image",
        type=str,
        default="python:3.9-slim",
        help="The Docker image to use (default: python:3.9-slim).",
    )
    args = parser.parse_args()

    # set the package name in the environment variable
    os.environ["PACKAGE_NAME"] = args.package_name
    os.environ["BASE_IMAGE"] = args.docker_image

    from smart_py.package_structure import PackageStructure
    from smart_py.file_creator import FileCreator

    # Create package structure and files
    package_structure = PackageStructure(args.package_name, args.docker_image)
    package_structure.create_directories()

    file_creator = FileCreator(args.package_name, args.docker_image)
    file_creator.create_init_file()
    file_creator.create_setup_file()
    file_creator.create_readme()
    file_creator.create_test_init()
    file_creator.create_gitignore()
    file_creator.create_requirements()
    file_creator.create_dev_requirements()
    file_creator.create_devcontainer_json()
    file_creator.create_post_create_sh()
    file_creator.create_dockerfile()
    file_creator.create_publish_yml()

    print(
        f"Successfully created Python package: {args.package_name} with Docker Image: {args.docker_image} and devcontaier support.\n"
    )
    # print_pypi_instructions()


if __name__ == "__main__":
    main()
