from setuptools import setup, find_packages

setup(
    name="smart-py",
    version="1.0.0",
    description="Generate a Python package structure with optional Docker support.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nadeem Khan",
    author_email="nadeem4.nk13@gmail.com",
    url="https://github.com/nadeem4/boilerplate_code",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "gps=smart_py.cli:main",
            "ppi=smart_py.cli:print_pypi_instructions",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
