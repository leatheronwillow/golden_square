from lib.present import *
import pytest

def test_check_if_present():
    present = Present()
    present.wrap('Tennis racquet')
    assert present.unwrap() == 'Tennis racquet'

def test_check_error_wrap():
    present = Present()
    present.wrap('Cricket Bat')
    with pytest.raises(Exception) as e:
        present.wrap('Something else')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_check_unwrap_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."