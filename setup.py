#!/usr/bin/env python
"""Setup.py."""
import setuptools

with open("README.md", "r") as ld:
    long_description = ld.read()

setuptools.setup(
    name="chimopy",
    version="0.0.1",
    author="Antony Gakuru",
    author_email="antony123muriithi@gmail.com",
    description="A Python wrapper for Chimoney APIs abstracting raw https requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/morehwachege/chimopy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "certifi",
        "chardet",
        "future",
        "idna",
        "requests",
        "six",
        "urllib3",
    ],
)