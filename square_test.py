import imp
import pytest
from square import squ
import warnings
"""
unit test working with classes

unit test - test an isolated unit of code
integration test - test the working interaction of ur code

test file needs to be saved as filename_test.py

tests
-----
unit tests / integration test / regression test / acceptance test
"""

def test_out():
    assert squ(2)==4

def test_out_type():
    assert type(squ(2))==int

def test_inp_error():
    with pytest.raises(TypeError):
        squ('meep')

def test_warning_float():
    with pytest.warns(UserWarning):
        squ(3.0)
