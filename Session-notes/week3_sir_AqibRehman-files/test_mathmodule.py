from mathmodule import *
""" star means all the function in mathmodule
    when you requried specific function from module you just name after import.
"""

def test_calc_add():
    assert calc_add(3, 5) == 8
    assert calc_add(7, 5) == 12
    assert calc_add(3, 2) == 5
    
def test_calc_sub():
    assert calc_sub(3, 5) == -2
    assert calc_sub(7, 5) == 2
    assert calc_sub(3, 2) == 1
    
def test_calc_mult():
    assert calc_mult(3, 5) == 15
    assert calc_mult(7, 5) == 35
    assert calc_mult(3, 2) == 6

def test_calc_div():
    assert calc_div(10, 2) == 5
    assert calc_div(0, 5) == 0
    assert calc_div(-10, -2) == 5