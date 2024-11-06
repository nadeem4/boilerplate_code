from pkg_wizard.util.file_creator import FileCreator
from pkg_wizard.content import dockerfile_content
import os


class DockerSupport:

    def __init__(self, override_files: list):
        self.file_creator = FileCreator()
        self.override_files = override_files

    def create_dockerfile(self):
        """Create a Dockerfile for the project.

        This function generates a Dockerfile in the project's .devcontainer directory with the specified Docker image, installs pip and upgrades it, sets the working directory to /workspace, copies the project's contents into the container, and installs the package in editable mode with dev dependencies.

        Raises:
            None
        """
        file_name = dockerfile_content.file_name
        override = True if file_name in self.override_files else False
        dockerfile_path = os.path.join(dockerfile_content.file_name)
        content = dockerfile_content.content
        self.file_creator.create_file(dockerfile_path, content, override=override)
