# Programming Question-2 Algorithms Part 1
# Question 2
# Quicksort

# read
with open('/Users/minjay/Documents/Documents/Courses/Algorithms_Part1/QuickSort.txt') as f:
	lines = f.read().splitlines()

# convert type
lines = map(int, lines)

def Quicksort(lines, l, r):
	"Count the number of comparisons"
	#list: pass the reference (not the copy)
	if l<r:
		# pivot: "median-of-three"
		n = r-l+1
		if n%2==0:
			middle = int(n/2)+l-1
		else:
			middle = int(n/2)+l
		med = sorted([lines[l], lines[r], lines[middle]])
		if lines[l]==med[1]:
			p_ind = l
		elif lines[r]==med[1]:
			p_ind = r
		else:
		    p_ind = middle
		tmp = lines[l]
		lines[l] = lines[p_ind]
		lines[p_ind] = tmp
		p = lines[l]
		i = l+1
		for j in range(l+1, r+1):
			if lines[j]<p:
				tmp = lines[j]
				lines[j] = lines[i]
				lines[i] = tmp
				i = i+1
		tmp = lines[i-1]
		lines[i-1] = lines[l]
		lines[l] = tmp
		return Quicksort(lines, l, i-2)+Quicksort(lines, i, r)+r-l
	else:
	    return 0
		
n = len(lines)

times = Quicksort(lines, 0, n-1)
