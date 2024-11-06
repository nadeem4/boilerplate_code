import os
from pkg_wizard.content import pre_commit_config_content
from pkg_wizard.util.file_creator import FileCreator


class PreCommitSupport:

    def __init__(self, override_files: list):
        self.file_creator = FileCreator()
        self.override_files = override_files

    def create_pre_commit_config(self):
        """Creates a pre-commit configuration file for the project.

        This function generates a .pre-commit-config.yaml file with specific repositories, hooks, and configurations for pre-commit checks.

        Returns:
            None

        Raises:
            None
        """
        file_name = pre_commit_config_content.file_name
        override = True if file_name in self.override_files else False
        pre_commit_config_path = os.path.join(file_name)
        content = pre_commit_config_content.content
        self.file_creator.create_file(
            pre_commit_config_path, content, override=override
        )
