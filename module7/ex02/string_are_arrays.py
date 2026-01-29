#!/usr/bin/env python3
import sys

#if len(sys.argv) != 2:
#	print("none")
#	sys.exit()
#par = sys.argv[1]
#count = 0
#for sttr in par:
#	if sttr == "z":
#		count += 1
#if count >= 1:
#	hl = 0
#	while hl < count:
#		print("z", end="")
#		hl += 1
#else:
#	print("none")




if len(sys.argv) != 2:
	print("none")
	sys.exit()
par = sys.argv[1]
count = 0
i = 0
while i < len(par):
	if par[i] == "z":
		count += 1
	i += 1
if count >= 1:
	hl = 0
	while hl < count:
		print("z", end="")
		hl += 1
else:
	print("none")
