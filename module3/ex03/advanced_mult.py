#! /usr/bin/env python3


n = 0 
while n <= 10:
	mult = 0
	print("Table of ", n, ":", end=" ")
	while mult <= 10:
		print(n*mult, end=" ")
		mult += 1
	print()
	n += 1


# for n in range(11):
# 	print("Table of", n, ":", end=" ")
# 	for mult in range(11):
# 		print(n*mult, end=" ")
# 	print()