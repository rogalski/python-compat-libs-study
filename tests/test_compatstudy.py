from __future__ import absolute_import, division, print_function, unicode_literals

import compatstudy.with_six
import compatstudy.with_nine
import compatstudy.with_future


def _test_module(module):
    assert not isinstance(module.get_range(), list)
    assert not isinstance(module.get_iteritems(), list)


def test_with_six():
    _test_module(compatstudy.with_six)


def test_with_nine():
    _test_module(compatstudy.with_nine)


def test_with_future():
    _test_module(compatstudy.with_future)
