#! /usr/bin/env python3

or_array = [1, 3, 7, 20, 0, -5]

new_array = []
for num in or_array:
	if num > 5:
		new_array.append(num + 2)

print(or_array)
print(new_array)