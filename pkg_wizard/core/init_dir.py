import os
from pkg_wizard.utils.file import create_file


class InitDir:

    def create_init_file(self, package_name, sub_dirs: list):
        """Create an __init__.py file to initialize the package.

        This function generates an __init__.py file within the package directory to initialize the package.

        Raises:
            OSError: If there are issues creating the file.
        """
        init_path = os.path.join(package_name, "__init__.py")
        content = f'"""Initialize the {package_name} package."""\n'
        create_file(init_path, content)

        for sub_dir in sub_dirs:
            init_path = os.path.join(package_name, sub_dir, "__init__.py")
            content = f'"""Initialize the {sub_dir} module."""\n'
            create_file(init_path, content)
