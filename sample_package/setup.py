from setuptools import setup, find_packages

setup(
    name="sample_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A description of your package.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sample_package",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    extras_require={
        "dev": [
            "pytest",
            "flake8",
            # Add other development dependencies here
        ],
    },
    entry_points={
        "console_scripts": [
            "sample_package=sample_package.cli:main",
        ],
    },
)
