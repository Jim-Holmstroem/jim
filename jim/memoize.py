from __future__ import division, print_function

from functools import (
    wraps,
)

from jim import function
from jim.os_ import mkdirp


def memoized(directory='data'):
    mkdirp(directory)

    def _memoized(f):
        import os

        function_directory = os.path.join(
            directory,
            function.fullname(f)
        )
        mkdirp(function_directory)

        @wraps(f)
        def memoized_f(arg):
            data_path = os.path.join(
                function_directory,
                str(hash(arg)),
            )
            if not(os.path.exists(data_path)):
                return_value = f(arg)
                with open(data_path, 'w') as f_:
                    f_.write(return_value)
                    f_.flush()

            with open(data_path, 'r') as f_:
                return f_.read()

        return memoized_f

    return _memoized
