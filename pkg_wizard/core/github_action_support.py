from pkg_wizard.util.file_creator import FileCreator
from pkg_wizard.content import publish_yaml_content
import os


class GithubActionSupport:

    def __init__(self, override_files: list):
        self.file_creator = FileCreator()
        self.override_files = override_files

    def create_publish_yml(self):
        """Creates a publish.yml file for GitHub Actions workflow to publish a Python
        package.

        The function generates the content for the publish.yml file, which includes the workflow configuration for building and publishing a Python package to PyPI.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the publish.yml file.
        """
        file_name = publish_yaml_content.file_name
        override = True if file_name in self.override_files else False
        workflows_dir = os.path.join(".github", "workflows")
        publish_yml_path = os.path.join(workflows_dir, file_name)
        content = publish_yaml_content.content
        self.file_creator.create_file(publish_yml_path, content, override=override)
