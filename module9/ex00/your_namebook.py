#!/usr/bin/env python3

def array_of_names(dickt):
	arr = []
	for x, y in dickt.items():
		full_name = x.capitalize() + " " + y.capitalize()
		arr.append(full_name)
	return arr

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))