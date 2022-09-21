#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):

	return [max(i) for i in numbers]

def join_integers(numbers):
	return int(''.join([str(num) for num in numbers]))

def generate_prime_numbers(limit):
	primes = []
	numbers = list(range(2, limit + 1))

	while len(numbers):
		number = numbers[0]
		primes.append(number)
		for el in numbers:
			if el % number == 0:
				numbers.remove(el)

	return primes




def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	numbers = [i for i in range(1, num_combinations + 1) if excluded_multiples != None and i % excluded_multiples != 0]
	numbers = [i for i in range(1, num_combinations + 1) if excluded_multiples == None]
	return list(map(lambda x: str(x[0]) + str(x[1]), itertools.product(strings, numbers)))

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
