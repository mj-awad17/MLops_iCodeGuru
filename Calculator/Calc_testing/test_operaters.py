from Calc_functions.operate import addition, subtraction, multiplication, division, square

# test_addition function
def test_addition():
    assert addition(5, 6) == 11
    assert addition(4, 5) == 9


# test_subtraction function
def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(9, 3) == 6
    
# test_multiplication function
def test_multiplication():
    assert multiplication(5, 5) == 25
    assert multiplication(2, 3) == 6

# test_division function
def test_division():
    assert division(10, 2) == 5
    assert division(15, 3) == 5
    
# test_square function
def test_square():
    assert square(5) == 25
    assert square(9) == 81
    
# =========================================================================== #