#O(n) algorithm
import time
from matplotlib import pyplot

def find_max(seq): #expects a list of floats/ints
    max = seq[0]
    for x in seq[1:]:
        if x > max:
            max = x
    return max

#runtimes for lists in increasing order:
runtimes = []
foo = []
for i in range(5000):
    foo.append(i+1)
    start = time.perf_counter()
    find_max(foo)
    end = time.perf_counter()
    runtimes.append((end-start)*(10**6))
    
pyplot.plot(runtimes)
pyplot.show()