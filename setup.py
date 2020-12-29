#!/usr/bin/env python

import setuptools

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open("README.rst", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="mydigitaldevops-cookiecutter",
    version="1.0.dev1",
    description="A sweet command-line tool that generates robust development/production Django-based environments. ",
    long_description=long_description,
    author="Nicolas Ahouandjinou",
    author_email="nico@mydigitaldevops.com",
    url="https://github.com/mydigitaldevops-com/mydigitaldevops-cookiecutter",
    packages=setuptools.find_packages(),
    license="GPLv3",
    zip_safe=False,
    classifiers=[
        "Topic :: Software Development",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: Django :: 3.0",
        "Operating System :: OS Independent",
        (
            "License :: OSI Approved :: "
            "GNU General Public License v3 or later (GPLv3+)"
        ),
    ],
    python_requires=">=3.7",
    keywords=(
        "Scaffold, Python3, Django3, flake8, pytest, code-black, coverage,"
        "Build automation, Integrated tests"
    ),
)
