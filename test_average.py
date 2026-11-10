import pytest
from average import average

def test_basic():
    assert average([1, 2, 3]) == 2.0

def test_equal_values():
    assert average([5, 5]) == 5.0

def test_single_item():
    assert average([7]) == 7.0

def test_empty_raises():
    with pytest.raises(ZeroDivisionError):
        average([])