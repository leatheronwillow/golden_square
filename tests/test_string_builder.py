from lib.string_builder import *

def test_initialise_string_builder():
    builder = StringBuilder()
    assert builder.output() == ""

def test_add_string_builder():
    builder = StringBuilder()
    builder.add("Hello")
    assert builder.output() == "Hello"

def test_string_builder_size():
    builder = StringBuilder()
    builder.add("Hello")
    assert builder.size() == 5