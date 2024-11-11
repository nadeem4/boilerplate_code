import os
from pkg_wizard.utils.file import create_file


class TestSupport:

    def __init__(self, override_files: list = []):
        self.override_files = override_files

    def create_test_init(self):
        """Create an __init__.py file for the tests module.

        Args:
            self: The instance of the class calling the method.
                It should have the attributes 'package_name' and 'create_file'.

        Returns:
            None

        Raises:
            FileNotFoundError: If the specified path for the __init__.py file does not exist.
        """
        test_init_path = os.path.join("tests", "__init__.py")
        content = f'"""Initialize the test module."""\n'
        create_file(test_init_path, content)
