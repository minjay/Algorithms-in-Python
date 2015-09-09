# Programming Question-6 Algorithms Part 1
# Question 1
# Hash Table (Dictionary)

import math

with open('/Users/minjay/Documents/Documents/Courses/Algorithms_Part1/2sum.txt') as f:
	lines = f.read().splitlines()

lines = map(int, lines)
n = len(lines)

# construct hash table 1
ht1 = {}

for i in range(n):
	x = int(math.floor(lines[i]/1e4))
	if str(x) in ht1:
		ht1[str(x)].append(lines[i])
	else:
		ht1[str(x)] = [lines[i]]

ht2 = {}

for key1 in ht1:
	key1_int = int(key1)
	range_key2 = [-2-key1_int, -1-key1_int, -key1_int, 1-key1_int]
	for key2 in range_key2:
		if str(key2) in ht1:
			for x in ht1[key1]:
				for y in ht1[str(key2)]:
					t = x+y
					if t>=-10000 and t<=10000 and x!=y and t not in ht2:
						ht2[str(t)] = [x, y]

tot = len(ht2)