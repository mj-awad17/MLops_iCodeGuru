# calculator
import streamlit as st

from Calc_functions.operate import addition, subtraction, multiplication, division, square

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("*"*20)
print(f"Addition of {num1} and {num2}:", addition(num1, num2))


print(f"Subtraction of {num1} and {num2}:", subtraction(num1, num2))


print(f"Multiplication of {num1} and {num2}:", multiplication(num1, num2))


print(f"Division of {num1} and {num2}:", division(num1, num2))

print(f"Square of {num1}:", square(num1))