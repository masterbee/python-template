# -*- coding: utf-8 -*-

import pytest

from package.core import package


def test_takeoff():
    assert takeoff() == 'Takeoff complete!'
