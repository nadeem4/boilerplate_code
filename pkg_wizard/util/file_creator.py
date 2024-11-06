import os


class FileCreator:
    """A class that creates files for a specified package using a given Docker image."""

    def create_file(self, file_path, content, override=False):
        if not os.path.exists(file_path) or override:
            with open(file_path, "w") as f:
                f.write(content)
            print(f"Created file: {file_path}")
        else:
            print(f"Skipped file (already exists): {file_path}")
