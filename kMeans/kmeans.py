import numpy, sys, Pycluster, os
from scipy.spatial.distance import pdist, squareform

def kmeans(t,d,k,p):
	dMatrix = squareform(pdist(d, 'correlation'))
	labels, error, nfound = Pycluster.kcluster(d, nclusters=k,npass=p,dist='c')
	kIndices = [numpy.flatnonzero(labels==ki) for ki in range(k)]

	return kIndices, labels, dMatrix

def silhouette(t, d, k, labels, dM, kIndices):
	num = len(d)
	a = numpy.zeros(num)
	b = numpy.zeros(num)

	for i in range(num):
		a[i] = numpy.mean([dM[i][ind] for ind in kIndices[int(labels[i])] if ind!=i])
		b[i] = numpy.min([numpy.mean(dM[i][ind]) for ki,ind in enumerate(kIndices) if labels[i]!=ki])

	s = (b-a)/numpy.maximum(a,b)

	return s

zData = []
tidIndex = []
inFile = open(sys.argv[1],'r')

print inFile.next().strip() + "\tcluster"
for line in inFile:
	data = line.strip().split()
	vals = [float(x) for x in data[1:]]
	tidIndex.append(data[0])
	zData.append(vals)

zData = numpy.array(zData)

inK = int(sys.argv[2])
passNum = int(sys.argv[3])

kIndices, labels, dMatrix = kmeans(tidIndex, zData, inK, passNum)

count = 1
for kIndex in kIndices:
	for i in kIndex:
		out = [tidIndex[i]]
		out.extend([str(x) for x in zData[i]])

		print '\t'.join(out) + "\t" + str(count)

	count += 1