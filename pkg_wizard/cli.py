import argparse
import os
from pkg_wizard.core.configuration_support import ConfigurationSupport
from pkg_wizard.core.docker_support import DockerSupport
from pkg_wizard.core.github_action_support import GithubActionSupport
from pkg_wizard.core.init_dir import InitDir
from pkg_wizard.core.pre_commit_support import PreCommitSupport
from pkg_wizard.core.test_support import TestSupport
from pkg_wizard.core.dev_container_support import DevContainerSupport


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
    parser.add_argument(
        "--sub_dirs",
        nargs="*",
        default=[],
        help="The subdirectories to create in the package.",
    )
    parser.add_argument(
        "--exclude_features",
        nargs="*",
        default=[],
        choices=[
            "config",
            "docker",
            "github_actions",
            "pre_commit",
            "tests",
            "dev_container",
        ],
        help="The features to exclude from the package.",
    )
    parser.add_argument(
        "--include_features",
        nargs="*",
        default=[
            "config",
            "docker",
            "github_actions",
            "pre_commit",
            "tests",
            "dev_container",
        ],
        choices=[
            "config",
            "docker",
            "github_actions",
            "pre_commit",
            "tests",
            "dev_container",
        ],
        help="The features to include in the package (default: all features).",
    )

    # add llm support arg
    parser.add_argument(
        "--llm",
        action="store_true",
        help="Include support for the LLM package.",
    )

    args = parser.parse_args()

    # set the package name in the environment variable
    os.environ["PACKAGE_NAME"] = args.package_name
    os.environ["BASE_IMAGE"] = args.docker_image
    print(args.sub_dirs)
    # ['units,core']
    if args.sub_dirs:
        dirs = args.sub_dirs[0]
        dirs = dirs.split(",")
    else:
        dirs = []

    from pkg_wizard.package_structure import PackageStructure

    if args.llm:
        dirs.append("llm")

    # Create package structure and files
    package_structure = PackageStructure(args.package_name, args.docker_image, dirs)
    package_structure.create_directories()
    ConfigurationSupport(package_name=args.package_name).create_files()
    DockerSupport(docker_image=args.docker_image).create_files()
    GithubActionSupport().create_files()
    PreCommitSupport().create_files()
    TestSupport().create_test_init()
    DevContainerSupport(pakcage_name=args.package_name).create_files()

    if args.llm:
        from pkg_wizard.core.llm_support import LLMSupport

        LLMSupport(package_name=args.package_name).create_files()

    InitDir().create_init_file(args.package_name, dirs)

    print(
        f"Successfully created Python package: {args.package_name} with Docker Image: {args.docker_image} and devcontaier support.\n"
    )
    print_pypi_instructions()


if __name__ == "__main__":
    main()
