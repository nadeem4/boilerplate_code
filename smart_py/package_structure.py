import os

class PackageStructure:
    def __init__(self, package_name, docker_image='python:3.9-slim'):
        self.package_name = package_name
        self.docker_image = docker_image
        self.dirs = [
            package_name,
            os.path.join(package_name, package_name),
            os.path.join(package_name, 'tests'),
            os.path.join(package_name, '.devcontainer'),
            os.path.join(package_name, '.github', 'workflows')
        ]

    def create_directories(self):
        for dir in self.dirs:
            os.makedirs(dir, exist_ok=True)
            print(f"Created directory: {dir}")
