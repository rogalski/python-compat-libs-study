from __future__ import absolute_import, division, print_function, unicode_literals
from nine import range, iteritems, IS_PYTHON2


def get_range():
    return range(3)


def get_iteritems():
    return iteritems({})


def branching():
    if IS_PYTHON2:
        print("PY2")
    else:
        print("PY3")
