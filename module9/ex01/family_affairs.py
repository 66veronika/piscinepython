#!/usr/bin/env python3

def find_the_redheads(dickt):
	arr = []
	for x, y in dickt.items():
		if y == "red":
			arr.append(x)
	return arr



dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))