from __future__ import division, print_function

def name(f):
    return f.__name__

def module(f):
    return f.__module__

def fullname(f):
    return '{module}.{name}'.format(
        module=module(f),
        name=name(f),
    )
