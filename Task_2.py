import math
from email.header import make_header

n = int(input("Enter a number: "))

#Square root
if n < 0:
    print("Square root is not defined for Negative number")
else:
    square_root = math.sqrt(n)
    print(f"Square Root: {square_root}")

#Logarithm
if n < 0:
    print("Logarithm are not defined for Negative number")
else:
    logarithm = math.log(n)
    print(f"Logarithm: {logarithm}")

#Sin
sin = math.sin(n)
print(f"Sine: {sin}")