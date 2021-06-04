import unittest
import pytest
import deploy

import my_calc

def test_sum_happy_path():
    current_value = my_calc.add(10,20)
    expected_value = 30

    assert expected_value == current_value

def test_sum_wrong_datatype():
    with pytest.raises(Exception):
        my_calc.add('x','y')
