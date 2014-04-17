import sys
from scipy import linalg
import numpy as np

data = .... # a 2d array of your data
mat = np.matrix(data) #setup your matrix

#svd the matrix to get the 3 decomposed matrices
u, s, v = np.linalg.svd(mat, full_matrices=True)

#number of components you want to get rid of
x = 1
newS = s[-x:] = 0

#new matrix with components removed
newMat = np.dot(np.dot(u,linalg.diagsvd(newS,len(mat),len(v))),v)

'''
# Following code was used on regeneration time-course data

inFile = open(sys.argv[1],'r')

header = inFile.next().strip()

ids = []
mat = []
for line in inFile:
	data = line.strip().split()
	if data[1] == 'tail':
		ids.append(data[0])
		mat.append([float(x) for x in data[2:]])

mat = np.matrix(mat)
u, s, v = np.linalg.svd(mat, full_matrices=True)

compNum = len(s)
print 'components\t' + header

for i in range(compNum):
	newS = s.copy()
	if i > 0:
		newS[-i:] = 0

	newMat= np.dot(np.dot(u,linalg.diagsvd(newS,len(mat),len(v))),v)

	idCount = 0
	for row in newMat:
		out = []
		for a in range(newMat.shape[1]):
			out.append(str(row[0,a]))
		
		print str(compNum - i) + "\t" + ids[idCount] + "\thead\t" + '\t'.join(out)
		
		idCount += 1
'''