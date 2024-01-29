from lib.check_codeword import *

def test_check_codeword_is_horse():
    assert check_codeword("horse") == "Correct! Come in.", 'when correct codeword entered'

def test_if_close():
    assert check_codeword("hsdfe") == "Close, but nope.", 'when first and last letters are correct'

def test_if_wrong():
    assert check_codeword("jsofnl") == "WRONG!"
