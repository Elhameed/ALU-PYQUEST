from setuptools import setup, find_packages

setup(
    name='ALU-PyQuest',
    version='0.1.7',
    packages=['src'],
    install_requires=[
        # list your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'PyQuest=src.quiz:playgame'
        ]
    },
    python_requires='>=3.7',
    include_package_data=True,
    author='Teniola Ajani',
    author_email='a.ajani@alustudent.com',
    description='Python Programming quiz',
    license='MIT',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Elhameed/ALU-PYQUEST',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
)

