content = """name: Publish Python Package

on:
push:
    tags:
    - '*.*.*'

jobs:
build:
    runs-on: ubuntu-latest
    steps:
    - name: Check out code
        uses: actions/checkout@v3

    - name: Set up Python
        uses: actions/setup-python@v4
        with:
        python-version: '3.x'

    - name: Install dependencies
        run: |
        python -m pip install --upgrade pip
        pip install setuptools wheel

    - name: Build package
        run: |
        python setup.py sdist bdist_wheel

    - name: Publish package
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
        password: ${{ secrets.PYPI_API_TOKEN }}
"""

file_name = "publish.yml"
