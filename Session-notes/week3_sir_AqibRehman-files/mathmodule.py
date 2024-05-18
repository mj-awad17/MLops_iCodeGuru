# mathmodule

# calc_add function
def calc_add(num1, num2):
    return num1 + num2

# calc_sub function
def calc_sub(num1, num2):
    return num1 - num2

# calc_mult function
def calc_mult(num1, num2):
    return num1 * num2

#calc_div function
def calc_div(num1, num2):
    if (num2 == 0):
        raise ValueError("Cannot divide by zero.")
    return num1 / num2
