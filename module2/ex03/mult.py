#! /usr/bin/env python3

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = a*b
if c < 0:
	print(a, "x", b, " = ", c, "The result is negative.")
elif c > 0:
	print(a, "x", b, "=", c, "The result is positive.")
elif c == 0:
	print(a, "x", b, "=", c, "The result is positive and negative.")

