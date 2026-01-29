#!/usr/bin/env python3


def greetings(name="noble stranger"):
	if not isinstance(name, str):
		print("Error! It was not a name.")
	else:
		print(f"Welcome, {name}.")

greetings()
greetings("Veronika")
greetings(42)
