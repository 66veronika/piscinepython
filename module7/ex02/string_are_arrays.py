#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
	print("none")
	sys.exit()
par = sys.argv[1:]
count = 0
for sttr in par:
	if sttr == "z":
		count += 1
if count >= 1:
	hl = 0
	while hl < count:
		print("z", end=" ")
		hl += 1
else:
	print("none")
