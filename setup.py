from __future__ import division, print_function

import os
from setuptools import (
    setup,
    find_packages,
)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="jim",
    version="0.1.0",
    author="Jim Holmstrom",
    author_email="jim.holmstroem@gmail.com",
    description="Utils for various things",
    long_description=read('README.md'),
    license="GPLv2",
    keywords="utility",
    url="http://packages.python.org/jim",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: GPLv2",
    ],
)
