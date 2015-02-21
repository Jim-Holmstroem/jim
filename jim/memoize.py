from __future__ import division, print_function

from functools import (
    wraps,
)

from jim import function


def memoized(directory='data'):
    def _memoized(f):
        import os
        directory = 'data'
    
        @wraps(f)
        def memoized_f(arg):
            data_path = os.path.join(directory, function.fullname(f), arg)
            if not(os.path.exists(data_path)):
                with open(data_path, 'w') as f:
                    f.write(f(arg))
    
            with open(data_path, 'r') as f:
                return f.read()
  
        return memoized_f

    return _memoized
