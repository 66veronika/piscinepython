#! /usr/bin/env python3
import sys

args = sys.argv[1:]
args.reverse()
if len(sys.argv) <= 2:
	print("none")
else:
	for arg in args:
		print(arg)



