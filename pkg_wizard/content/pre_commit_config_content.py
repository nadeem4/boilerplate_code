content = """
repos:
- repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5  # Specify the version you want
    hooks:
    - id: docformatter
        args:
        - --in-place
        - --recursive
        - --wrap-summaries=88
        - --wrap-descriptions=88
        files: \.py$

- repo: https://github.com/psf/black
    rev: 24.10.0  # Specify the version of black you want
    hooks:
    - id: black
        language_version: python3

- repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
    - id: trailing-whitespace
    - id: debug-statements
    - id: check-merge-conflict
"""

file_name = ".pre-commit-config.yaml"
