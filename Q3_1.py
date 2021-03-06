# Programming Question-3 Algorithms Part 1
# Question 1
# Min-cut

import numpy as np
import math
import copy

# read
with open('/Users/minjay/Documents/Documents/Courses/Algorithms_Part1/kargerMinCut.txt') as f:
	# loop over
	graph = []
	for line in f:
		# remove \n
		line = line.rstrip()
		line = line.split('\t')
		line = [int(i) for i in line]
		graph.append(line)

# get nodes and edges
nodes = []
edges = []

for line in graph:
	nodes.append(line[0])
	for i in range(1, len(line)):
		tmp = [line[0], line[i]]
		flag = 0
		for j in edges:
			if set(tmp)==set(j):
				flag = 1
				break
		if flag==0:
			edges.append(tmp)

n = len(nodes)
N = int(math.ceil(n*math.log(n)))
# copy the object
rec_nodes = copy.deepcopy(nodes)
rec_edges = copy.deepcopy(edges)

# calculate min-cut
min_cut = len(rec_edges)
# set seed
np.random.seed(0)
for i in range(N):
	# retrieve the object
	nodes = copy.deepcopy(rec_nodes)
	edges = copy.deepcopy(rec_edges)
	while len(nodes)>2:
		# high exclusive
		index = np.random.randint(0, len(edges))
		remove_edge = edges[index]
		node1 = remove_edge[0]
		node2 = remove_edge[1]
		# merge
		for j in range(len(edges)):
			if edges[j][0]==node2:
				edges[j][0] = node1
			if edges[j][1]==node2:
				edges[j][1] = node1
		# remove node2
		nodes.remove(node2)
		# remove self-loops
		tmp_edges = copy.deepcopy(edges)
		for j in tmp_edges:
			if j[0]==j[1]:
				edges.remove(j)
	print(len(edges))
	if len(edges)<min_cut:
		min_cut = len(edges)

print(min_cut)