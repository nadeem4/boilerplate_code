import os

content = f"""from setuptools import setup, find_packages

setup(
    name='{os.getenv("PACKAGE_NAME")}',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Your Name',
    author_email='your.email@example.com',
    description='A description of your package.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/{os.getenv("PACKAGE_NAME")}',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    extras_require={{
        'dev': [
            'pytest',
            'flake8',
            # Add other development dependencies here
        ],
    }},
    entry_points={{
        'console_scripts': [
            '{os.getenv("PACKAGE_NAME")}={os.getenv("PACKAGE_NAME")}.cli:main',
        ],
    }},
)
"""

file_name = "setup.py"
