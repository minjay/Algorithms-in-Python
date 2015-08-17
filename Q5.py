# Programming Question-5 Algorithms Part 1
# Question 1
# Dijkstra's Shortest Path

import numpy as np

graph = []
# read
with open('/Users/minjay/Documents/Documents/Courses/Algorithms_Part1/dijkstraData.txt') as f:
	for line in f:
		line = line.rstrip()
		line = line.replace(',', '\t')
		line = line.split('\t')
		line = [int(i) for i in line]
		graph.append(line)

# transform
nodes = []
edges = []
weights = []
for line in graph:
	nodes.append(line[0])
	for i in range(1, len(line), 2):
		tmp = [line[0], line[i]]
		flag = 0
		for j in edges:
			if set(tmp)==set(j):
				flag = 1
				break
		if flag==0:
			edges.append(tmp)
			weights.append(line[i+1])

# init
n = len(nodes)
X = [1]
# row-major order
A = np.ones((1, n))*1000000
A[0][0] = 0

# main
while len(X)<n:
	# put outside
	min_dist = 1000000
	w_star = 0
	v_star = 0
	for j in range(len(edges)):
		edge = edges[j]
		if edge[0] in X and edge[1] not in X:
			dist = A[0][edge[0]-1]+weights[j]
			if dist<min_dist:
				min_dist = dist
				w_star = edge[1]
				v_star = edge[0]
		elif edge[0] not in X and edge[1] in X:
			dist = A[0][edge[1]-1]+weights[j]
			if dist<min_dist:
				min_dist = dist
				w_star = edge[0]
				v_star = edge[1]
	# put outside
	X.append(w_star)
	A[0][w_star-1] = min_dist

print(A[0][6])
print(A[0][36])
print(A[0][58])
print(A[0][81])
print(A[0][98])
print(A[0][114])
print(A[0][132])
print(A[0][164])
print(A[0][187])
print(A[0][196])