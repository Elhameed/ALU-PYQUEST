from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.3'
DESCRIPTION = 'Python Programming quiz'

def get_long_description():
    """
    Return the README.
    """
    return open("README.md", "r", encoding="utf8").read()

# Setting up
setup(
    name="ALU-PyQuest",
    version=VERSION,
    url="https://github.com/Elhameed/ALU-PYQUEST",
    license="MIT",
    description=DESCRIPTION,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Teniola Ajani",
    author_email="a.ajani@alustudent.com",
    packages=['src', 'src.beginner_questions', 'src.medium_questions', 'src.advanced_questions'],
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=[
    'beginner_questions',
    'medium_questions',
    'advanced_questions'
],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    # Specify the package data to be included in the distribution package
    package_data={'': ['*.txt', '*.md', '*.rst'], 'src': ['*.py']},
    # Specify the packages to be excluded from the distribution package
    exclude_package_data={'': ['__pycache__', '*.pyc', '*.pyo'], 'src': ['__pycache__', '*.pyc', '*.pyo']},
    entry_points={
        'console_scripts': [
            'PyQuest=src.quiz:playgame'
        ]
    },
    project_urls={
        "Source": "https://github.com/Elhameed/ALU-PYQUEST",
    },
)

