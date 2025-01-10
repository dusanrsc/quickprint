# setup.py

from setuptools import setup, find_packages

setup(
    name="quickprint",
    version="1.1.0",
    packages=find_packages(),
    description="A small module to replace print() and input() functions for reduced typing time.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Dušan Rosić",
    author_email="dusanrosic25.06.1997@email.com",
    url="https://github.com/dusanrsc/quickprint",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
