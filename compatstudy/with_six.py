from __future__ import absolute_import, division, print_function, unicode_literals
import six
from six.moves import range


def get_range():
    return range(3)


def get_iteritems():
    return six.iteritems({})


def branching():
    if six.PY2:
        print("PY2")
    else:
        print("PY3")
