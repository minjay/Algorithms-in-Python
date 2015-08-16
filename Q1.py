# Programming Question-1 Algorithms Part 1
# Divide and Conquer
# Recursively

from math import log, ceil
# read
with open('/Users/minjay/Documents/Documents/Courses/Algorithms_Part1/IntegerArray.txt') as f:
	lines = f.read().splitlines()

# convert type
lines = map(int, lines)

def merge(left_lines, right_lines):
	"Merge two parts"
	i = 0
	j = 0
	n1 = len(left_lines)
	n2 = len(right_lines)
	n = n1+n2
	new_lines = list()
	number = 0
	for k in range(n):
		if left_lines[i]<right_lines[j]:
			new_lines.append(left_lines[i])
			if i==n1-1:
				# has to be extend
				new_lines.extend(right_lines[j:n2])
				break
			else:
				i = i+1
		else:
			new_lines.append(right_lines[j])
			number = number+n1-i
			if j==n2-1:
				new_lines.extend(left_lines[i:n1])
				break
			else:
				j = j+1
	return {'sorted':new_lines, 'number':number}

def count(lines):
	"Count the number of inversions"
	n = len(lines)
	
	if n==1:
		return {'sorted':lines, 'number':0}
	else:
		(d, r) = divmod(n, 2)
		left_lines = lines[0:d]
		right_lines = lines[d:n]
		left_count = count(left_lines)
		right_count = count(right_lines)
		split_count = merge(left_count['sorted'], right_count['sorted'])
		return {'sorted':split_count['sorted'], 'number':split_count['number']\
		+left_count['number']+right_count['number']}

result = count(lines)
