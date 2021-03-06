"""
Hamming distance calculator.
Written by Bede Kelly for Exercism.
"""

from itertools import izip_longest
__author__ = "Bede Kelly"

def hamming(strand_one, strand_two):
	"""Returns the hamming distance between two strands of DNA."""
	distance = 0
	for pair in izip_longest(strand_one, strand_two):
		if pair[0] != pair[1]:
			distance += 1
	return distance