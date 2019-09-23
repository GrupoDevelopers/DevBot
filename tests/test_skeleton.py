# -*- coding: utf-8 -*-

import pytest
from devbot.skeleton import fib

__author__ = "Mike Douglas Oliveira Coelho"
__copyright__ = "Mike Douglas Oliveira Coelho"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
