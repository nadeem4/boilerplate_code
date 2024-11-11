from pkg_wizard.utils.file import create_file, read_file, get_file_path
import os


class DockerSupport:

    def __init__(self, docker_image, override_files: list = []):
        self.override_files = override_files
        self.folder_name = "docker"
        self.docker_image = docker_image

    def create_dockerfile(self):
        """Create a Dockerfile for the project.

        This function generates a Dockerfile in the project's .devcontainer directory with the specified Docker image, installs pip and upgrades it, sets the working directory to /workspace, copies the project's contents into the container, and installs the package in editable mode with dev dependencies.

        Raises:
            None
        """
        file_name, content = read_file(get_file_path(self.folder_name, "Dockerfile"))
        content = content.replace("{{docker_image}}", self.docker_image)
        overwrite = True if file_name in self.override_files else False
        dockerfile_path = os.path.join(file_name)
        create_file(dockerfile_path, content, overwrite=overwrite)

    def create_files(self):
        self.create_dockerfile()
