from lib.counter import *

def test_counter():
    counter = Counter()
    assert counter.count == 0, 'check initialisation'

def test_counter_add():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."



