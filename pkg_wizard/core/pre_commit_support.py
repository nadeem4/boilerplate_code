import os
from pkg_wizard.utils.file import create_file, read_file, get_file_path


class PreCommitSupport:

    def __init__(self, override_files: list = []):
        self.override_files = override_files
        self.folder_name = "pre_commit"

    def create_pre_commit_config(self):
        """Creates a pre-commit configuration file for the project.

        This function generates a .pre-commit-config.yaml file with specific repositories, hooks, and configurations for pre-commit checks.

        Returns:
            None

        Raises:
            None
        """
        file_name, content = read_file(
            get_file_path(self.folder_name, ".pre-commit-config.yaml")
        )
        overwrite = True if file_name in self.override_files else False
        pre_commit_config_path = os.path.join(file_name)
        create_file(pre_commit_config_path, content, overwrite=overwrite)

    def create_files(self):
        self.create_pre_commit_config()
