#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
	print("none")
	sys.exit()
par = sys.argv[1:]
print("parameters:", len(par))
for word in par:
	print(f"{word}: {len(word)}")
