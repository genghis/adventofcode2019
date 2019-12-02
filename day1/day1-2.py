import os
import math

array = []
def mathing(num):
	returnnumber = int(num) / 3
	return (math.floor(returnnumber)) - 2


with open('./input2.txt') as fp:
	for line in fp.readlines():
		while mathing(line) > 0:
			line = mathing(line)
			array.append(line)

print(sum(array))
