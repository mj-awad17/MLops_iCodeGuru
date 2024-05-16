# calculator
from Calculator_modularize import operate

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("*"*20)
print(f"Addition of {num1} and {num2}:", operate.addition(num1, num2))


print(f"Subtraction of {num1} and {num2}:", operate.subtraction(num1, num2))


print(f"Multiplication of {num1} and {num2}:", operate.multiplication(num1, num2))


print(f"Division of {num1} and {num2}:", operate.division(num1, num2))

print(f"Square of {num1}:", operate.square(num1))