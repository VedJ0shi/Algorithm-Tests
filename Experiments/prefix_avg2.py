#better O(n) 'Prefix Averages producing' algorithm
import time
from matplotlib import pyplot

def prefix_avgs(seq): #len(seq) = n
    A = []
    sum = 0
    for i in range(len(seq)): #iterates n times, from i=0 to i=n-1
        sum = sum + seq[i]
        A.append(sum/(i+1))
    return A

'''total run time is proportion to 1+1+1+...+1 = n'''

'''in each iteration of loop, there is:
1 variable update => O(1)
1 list update => O(1)
'''

'''this algo dynamically stores sum instead of recalculating it
with each iteration of the loop, avoiding quadratic behavior'''

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
