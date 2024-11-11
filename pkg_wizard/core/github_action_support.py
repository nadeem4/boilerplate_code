from pkg_wizard.utils.file import create_file, read_file, get_file_path
import os


class GithubActionSupport:

    def __init__(self, override_files: list = []):
        self.override_files = override_files
        self.folder_name = "github_actions"

    def create_publish_yml(self):
        """Creates a publish.yml file for GitHub Actions workflow to publish a Python
        package.

        The function generates the content for the publish.yml file, which includes the workflow configuration for building and publishing a Python package to PyPI.

        Returns:
            None

        Raises:
            OSError: If there is an issue creating the publish.yml file.
        """
        file_name, content = read_file(get_file_path(self.folder_name, "publish.yml"))
        overwrite = True if file_name in self.override_files else False
        workflows_dir = os.path.join(".github", "workflows")
        publish_yml_path = os.path.join(workflows_dir, file_name)
        create_file(publish_yml_path, content, overwrite=overwrite)

    def create_files(self):
        self.create_publish_yml()
