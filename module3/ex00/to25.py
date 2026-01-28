#! /usr/bin/env python3

n = int(input())
if n <= 25:
	while n <= 25:
		print("Inside the loop, my variable is", n)
		#print(F"Inside the loop, my variable is {n}")
		n += 1
else:
	print("Error")