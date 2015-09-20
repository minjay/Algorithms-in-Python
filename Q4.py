# Programming Question-4 Algorithms Part 1
# Question 1
# Strongly connected components

import sys
import resource
from time import *

sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

t1 = time()
print('loading data')
with open('/home/minjay/SCC.txt') as f:
	G = {}
	G_rev = {}
	nodes = []
	for line in f:
		line = line.rstrip()
		line = line.split(' ')
		line = [int(i) for i in line]
		tail = line[0]
		head = line[1]
		if tail not in G:
			G[tail] = [head]
		else:
			G[tail].append(head)
		if head not in G_rev:
			G_rev[head] = [tail]
			nodes.append(head)
		else:
			G_rev[head].append(tail)

def DFS(G, i, visited, f):
	# passed by reference
	visited.add(i)
	# check whether i has outer edges
	if i in G:
		for j in G[i]:
			if j not in visited:
				DFS(G, j, visited, f)
	f.append(i)

print(time()-t1)

t1 = time()
print('first DFS-loop')
# first DFS-loop
# slow for list O(n)
# set: check whether a in x
# list: iteration
visited = set()
f = []
# list is faster than dictionary
for i in nodes:
	if i not in visited:
		DFS(G_rev, i, visited, f)

f.reverse()

print(time()-t1)

t1 = time()
print('second DFS-loop')
# second DFS-loop
visited = set()
SCC_size = []
for i in f:
	if i not in visited:
		SCC = []
		DFS(G, i, visited, SCC)
		SCC_size.append(len(SCC))

SCC_size = sorted(SCC_size, reverse=True)

print(time()-t1)

if len(SCC_size)>=5:
	print(SCC_size[0:5])
else:
	print(SCC.size[0:len(SCC_size)])