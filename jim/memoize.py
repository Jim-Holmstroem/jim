from __future__ import division, print_function

from functools import (
    wraps,
)

from jim import function
from jim.os import mkdirp


def memoized(directory='data'):
    mkdirp(directory)

    def _memoized(f):
        import os

        function_directory = os.path.join(directory, function.fullname(f))
        mkdirp(function_directory)

        @wraps(f)
        def memoized_f(arg):
            data_path = os.path.join(function_directory, arg)
            if not(os.path.exists(data_path)):
                with open(data_path, 'w') as f:
                    f.write(f(arg))

            with open(data_path, 'r') as f:
                return f.read()

        return memoized_f

    return _memoized
