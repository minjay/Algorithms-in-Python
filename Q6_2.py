# Programming Question-6 Algorithms Part 1
# Question 2
# Median Maintenance

from heapq import *

with open('/Users/minjay/Documents/Documents/Courses/Algorithms_Part1/Median.txt') as f:
	lines = f.read().splitlines()

lines = map(int, lines)

n = len(lines)

# init two heaps
# h_low records negative values
h_low = []
h_high = []

s = 0
for i in range(n):
	if i==0:
		heappush(h_low, -lines[0])
		s = s+lines[0]
	elif i==1:
		if lines[1]>=lines[0]:
			heappush(h_high, lines[1])
			s = s+lines[0]
		else:
			heappush(h_high, lines[0])
			h_low = []
			heappush(h_low, -lines[1])
			s = s+lines[1]
	else:
		bound_1 = -nsmallest(1, h_low)[0]
		bound_2 = nsmallest(1, h_high)[0]
		if lines[i]>=bound_2:
			heappush(h_high, lines[i])
			if len(h_high)>len(h_low):
				ele = heappop(h_high)
				heappush(h_low, -ele)
		else:
			heappush(h_low, -lines[i])
			if len(h_low)-len(h_high)>1:
				ele = -heappop(h_low)
				heappush(h_high, ele)
		s = s-nsmallest(1, h_low)[0]

print(s)