import os
import math

array = []
def mathing(num):
	returnnumber = int(num) / 3
	return (math.floor(returnnumber)) - 2


with open('./input.txt') as fp:
	for line in fp.readlines():
		array.append(mathing(line))
		print(mathing(line))

print(sum(array))
