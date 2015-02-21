from __future__ import division, print_function

from jim.memoize import memoized


@memoized('data')
def download(url):
    from urllib2 import urlopen

    with closing(urlopen(url)) as f:
        return f.read()
