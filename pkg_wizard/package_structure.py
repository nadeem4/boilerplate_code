import os


class PackageStructure:
    """A class that defines the structure of a Python package including directories and
    Docker image configuration."""

    def __init__(self, package_name, docker_image="python:3.9-slim", sub_dirs=[]):
        """Initialize a PackageBuilder object with the provided package name and
        optional Docker image.

        Args:
            package_name (str): The name of the package being built.
            docker_image (str, optional): The Docker image to use for building the package. Defaults to 'python:3.9-slim'.

        Attributes:
            package_name (str): The name of the package being built.
            docker_image (str): The Docker image used for building the package.
            dirs (list): A list of directories associated with the package, including the package directory, subdirectories,
                         and directories for testing, development containers, and GitHub workflows.

        Raises:
            None
        """
        self.package_name = package_name
        self.docker_image = docker_image
        self.dirs = [
            package_name,
            "tests",
            ".devcontainer",
            os.path.join(".github", "workflows"),
        ] + [os.path.join(package_name, sub_dir) for sub_dir in sub_dirs]

    def create_directories(self):
        """Create directories based on the list of directories provided.

        Creates directories using the list of directories stored in the 'dirs' attribute of the object.
        If a directory already exists, it does not raise an error due to the 'exist_ok=True' parameter in 'os.makedirs'.

        Raises:
            OSError: If there is an issue creating the directories.

        Returns:
            None
        """
        for dir in self.dirs:
            os.makedirs(dir, exist_ok=True)
            print(f"Created directory: {dir}")
