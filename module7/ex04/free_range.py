#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
	print("none")
	sys.exit()

start = int(sys.argv[1])
end = int(sys.argv[2])
if start >= end:
	print("none")
	sys.exit()
array = []
x = range(start, end + 1)
for n in x:
	array.append(n)
print (array)
