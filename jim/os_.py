from __future__ import division, print_function

import os


def mkdirp(path):
    if not(os.path.exists(path)):
        os.mkdir(path)
