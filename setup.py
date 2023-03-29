from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = 'Python Programming quiz'
LONG_DESCRIPTION = 'A python programming quiz that tests users on the concepts of python programming'

# Setting up
setup(
    name="ALU-PYQUEST",
    version=VERSION,
    author="Teniola Ajani",
    author_email="a.ajani@alustudent.com",
    license="MIT",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[''],
    keywords=['python', 'quiz', 'game'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"
    ]
)

