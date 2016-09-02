from __future__ import absolute_import, division, print_function, unicode_literals
import sys
from future.builtins import range
from future.utils import iteritems


def get_range():
    return range(3)


def get_iteritems():
    return iteritems({})


def branching():
    if sys.version_info[0] == 2:
        print("PY2")
    else:
        print("PY3")
