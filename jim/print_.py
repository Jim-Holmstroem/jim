from __future__ import division, print_function

from itertools import (
    chain,
    starmap,
)

from functools import (
    wraps,
)


def rendered_function(end='', print=print):
    def _rendered_function(f):
        @wraps(f)
        def __rendered_function(*args, **kwargs):
            def function_name(f):
                return f.__name__

            print(function_name(f), end='')
            print(
                '({arguments})'.format(
                    arguments=', '.join(
                        chain(
                            ', '.join(
                                map(
                                    '{0}'.format,
                                    args
                                )
                            ),
                            ', '.join(
                                starmap(
                                    '{0}={1}'.format,
                                    kwargs.iteritems()
                                )
                            ),
                        )
                    )
                ),
                end=''
            )
            print('{', end='')
            return_value = f(*args, **kwargs)
            print('}}={return_value}'.format(return_value=return_value), end='')

            return return_value

        return __rendered_function

    return _rendered_function
