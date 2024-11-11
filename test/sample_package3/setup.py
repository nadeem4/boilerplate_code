from setuptools import setup, find_packages

setup(
    name="smart_py_with_llm",
    version="1.0.0",
    description="",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    author="<author_name>",
    author_email="<author_email>",
    url="<github_url>",
    license="<license>",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": ["gps=pkg_wizard.cli:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
