import sys
import scipy.stats as stats

print
print 'total number in population: ' + sys.argv[1]
print 'total number with condition in population: ' + sys.argv[2]
print 'number in subset: ' + sys.argv[3]
print 'number with condition in subset: ' + sys.argv[4]
print
print 'p-value <= ' + sys.argv[4] + ': ' + str(stats.hypergeom.cdf(int(sys.argv[4]) + 1,int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
print 
print 'p-value >= ' + sys.argv[4] + ': ' + str(stats.hypergeom.sf(int(sys.argv[4]) - 1,int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
print