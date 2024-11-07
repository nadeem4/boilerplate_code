file_path = "pkg_wizard/pre_commit/.pre-commit-config.yaml"


def read_file_as_string_with_name(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return (file.name, content)


print(read_file_as_string_with_name(file_path))
