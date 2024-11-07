import os


def create_file(file_path, content, overwrite=False):
    if not os.path.exists(file_path) or overwrite:
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Created file: {file_path}")
    else:
        print(f"Skipped file (already exists): {file_path}")


def read_file(file_path):
    with open(file_path, "r") as f:
        return (os.path.basename(f.name), f.read())


BASE_PATH = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))


# fetches the file path of files within the directory of content folder
def get_file_path(folder, file_name):
    return os.path.join(BASE_PATH, "content", folder, file_name)
