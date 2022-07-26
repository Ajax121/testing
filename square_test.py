"""
asd
"""
import pytest
from square import squ

def test_out():
    """
    unit test working with classes

    unit test - tests an isolated unit of code
    integration test - test the working interaction of ur code

    test file needs to be saved as filename_test.py

    tests
    -----
    unit tests / integration test / regression test / acceptance test
    """
    assert squ(2)==4

def test_out_type():
    """_summary_
    """
    assert isinstance(squ(2),int)  #type(squ(2))==int

def test_inp_error():
    """_summary_
    """
    with pytest.raises(TypeError):
        squ('meep')

def test_warning_float():
    """_summary_
    """
    with pytest.warns(UserWarning):
        squ(3.0)
