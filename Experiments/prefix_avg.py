#O(n^2) 'Prefix Averages producing' algorithm
import time
from matplotlib import pyplot

'''computes jth prefix average of given sequence separately and in a nested loop'''

def prefix_avgs(seq): #len(seq) = n
    A = []
    for j in range(len(seq)): #iterates n times, from j=0 to j=n-1
        sum = 0
        for i in range(j+1): #iterates from i=0 to i=j
            sum = sum + seq[i]
        A.append(sum/(j+1))
    return A #list of sequence averages

'''total run time is proportional to 1+2+3+...+n = n(n+1)/2 ~ n^2'''

'''in each iteration of outer loop, there is:
1 initialization of var => O(1)
1 nested loop => O(n) where n=j+1
1 list update => O(1) 
==> 2n*O(1) + O(n^2) ~ O(n^2)
'''

'''a for loop of range(n) requires n calls of next() in order to
advance the underlying iterator==> O(n)'''

runtimes = []
foo = []
for i in range(1000):
    foo.append(i+1)
    start = time.perf_counter()
    prefix_avgs(foo)
    end = time.perf_counter()
    runtimes.append((end-start)*(10**6))

pyplot.plot(runtimes)
pyplot.show()