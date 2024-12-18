from setuptools import setup, find_packages

setup(
    name="pkg_wizard",
    version="1.1.5",
    description="Generate a Python package structure with optional Docker support.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nadeem Khan",
    author_email="nadeem4.nk13@gmail.com",
    url="https://github.com/nadeem4/boilerplate_code",
    license="MIT",
    packages=find_packages(include=["pkg_wizard", "pkg_wizard.*"]),
    include_package_data=True,  # Ensure package data is included
    install_requires=[],
    entry_points={
        "console_scripts": [
            "generate=pkg_wizard.cli:main",
            "ppi=pkg_wizard.cli:print_pypi_instructions",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
