#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# If Django has a new release, we branch, tag, then update this setting after the tag.
version = "3.0.10"

if sys.argv[-1] == "tag":
    os.system(f'git tag -a {version} -m "version {version}"')
    os.system("git push --tags")
    sys.exit()

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="mydigitaldevops-cookiecutter",
    version=version,
    description="A Cookiecutter starter for creating our production-ready Django-based platform. ",
    long_description=long_description,
    author="Nicolas Ahouandjinou",
    author_email="mydigitaldevops@gmail.com",
    url="https://github.com/mydigitaldevops-com/mydigitaldevops-cookiecutter",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, starter, boilerplate, Python3, automation, django3 "
        "skeleton, scaffolding, setup.py"
    ),
)
