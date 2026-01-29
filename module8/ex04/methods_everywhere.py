#!/usr/bin/env python3
import sys
if len(sys.argv) <= 1:
	print("none")
	sys.exit()

def shrink(text):
	print(text[:8])

def enlarge(text):
	while len(text) < 8:
		text += "Z"
	print(text)

for arg in sys.argv[1:]:
	if len(arg) > 8:
		shrink(arg)
	elif len(arg) < 8:
		enlarge(arg)
	else:
		print(arg)