#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
	print("none")
	sys.exit()

needle = "ism"
par = sys.argv[1:]
for word in par:
	if word.find("ism", len(word) - 3) == -1:
			print(f"{word}ism")
