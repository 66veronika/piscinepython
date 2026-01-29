#!/usr/bin/env python
import sys

if len(sys.argv) != 3:
	print("none")
	sys.exit()
count = 0
needle = sys.argv[1]
stack = sys.argv[2]
pos = stack.find(needle, 0)
while pos != -1:
	count += 1
	pos = stack.find(needle, pos + 1)
if count > 0:
	print(count)
else:
	print("none")
