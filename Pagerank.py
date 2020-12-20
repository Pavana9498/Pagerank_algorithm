import sys
import re
data_file_path = sys.argv[1]
output_file_path = sys.argv[2]
graph_matrix = []

with open(data_file_path, 'r', encoding = 'utf-8-sig') as data_file:
	matrix = data_file.readlines()
	for row in matrix:
		print(row)
		row = re.sub('[\(\)]','', row.strip()).split("\t")
		row = [int(i) for i in row]
		graph_matrix.append(list(row))
print(graph_matrix)
n = len(graph_matrix)
probability_matrix = []
for row in graph_matrix:
	o_links = 0
	probability_row = []
	for node in row:
		if node == 1:
			o_links = o_links+1
	for node in row:
		if node == 1:
			prob = round(1/o_links, 3)
		else:
			prob = 0
		probability_row.append(prob)
	probability_matrix.append(probability_row)
print("27: ", probability_matrix)
with open(output_file_path, 'w') as o_file:
	o_file.write("95\n")
	o_file.write("(")
	for i in range(len(probability_matrix)):
		if i != 0:
			o_file.write(" ")
		for j in range(len(probability_matrix[i])):
			o_file.write(str(round(probability_matrix[i][j],2)))
			if j != n-1:
				o_file.write(" ")

		if i != n-1:
			o_file.write("\n")
		else:
			o_file.write(")")


for row in probability_matrix:
	s = 0
	for node in row:
		s = s+node
	if s == 0:
		for i in range(len(row)):
			row[i] = 1/n
print(probability_matrix)

with open(output_file_path, 'a') as o_file:
	o_file.write("\n(")
	for i in range(len(probability_matrix)):
		if i != 0:
			o_file.write(" ")
		for j in range(len(probability_matrix[i])):
			o_file.write(str(round(probability_matrix[i][j],2)))
			if j != n-1:
				o_file.write(" ")

		if i != n-1:
			o_file.write("\n")
		else:
			o_file.write(")")

visible1 = [False for i in range(n)]
visible2 = [False for i in range(n)]
print(visible1)
print(visible2)

reverse_matrix = [[probability_matrix[j][i] for j in range(len(probability_matrix))] for i in range(len(probability_matrix[0]))]
print(reverse_matrix)

def dfs1(vertex):
	visible1[vertex] = True
	for j in range(len(probability_matrix[vertex])):
		if probability_matrix[vertex][j] != 0 and not visible1[j]:
			dfs1(j)

def dfs2(vertex):
	visible2[vertex] = True
	for j in range(len(reverse_matrix[vertex])):
		if reverse_matrix[vertex][j] != 0 and not visible2[j]:
			dfs2(j)
dfs1(1)
dfs2(1)

print(visible1)
print(visible2)

def isIrreducible():
	for i in range(len(visible1)):
		if not visible1[i]:
			return False
	for i in range(len(visible2)):
		if not visible2[i]:
			return False
probability_transpose = [[probability_matrix[j][i] for j in range(len(probability_matrix))] for i in range(len(probability_matrix[0]))]
# print(probability_transpose)



if not isIrreducible():
	for row in probability_transpose:
		for i in range(len(row)):
			temp = (0.1/n)+(0.9*row[i])
			row[i] = round(temp, 3)
	print("\n", probability_transpose)

with open(output_file_path, 'a') as o_file:
	o_file.write("\n(")
	for i in range(len(probability_transpose)):
		if i != 0:
			o_file.write(" ")
		for j in range(len(probability_transpose[i])):
			o_file.write(str(round(probability_transpose[i][j],2)))
			if j != n-1:
				o_file.write(" ")

		if i != n-1:
			o_file.write("\n")
		else:
			o_file.write(")")

def powerIteration():
	p0 = [1/n]*n
	pk = p0
	k = 1
	while k <= 2:
		tempList = []
		for i in range(len(probability_transpose)):
			s = 0
			for j in range(len(probability_transpose[i])):
				s = s+probability_transpose[i][j]*pk[j]
			tempList.append(s)
		print("before: ",pk)
		pk = tempList
		k = k+1
		print("after: ",pk)
	with open(output_file_path, 'a') as o_file:
		o_file.write("\n(")
		for i in range(len(pk)):
			if i != 0:
				o_file.write(" ")
			o_file.write(str(round(pk[i],2)))
			if i == n-1:
				o_file.write(")")

powerIteration()



