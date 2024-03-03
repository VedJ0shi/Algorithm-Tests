#O(1) algorithm
import time

def length(seq): #expects a list arg
        return len(seq)

'''list class maintains a private instance attribute that records
current length of the list object; hence, for any length seq, length() simply
accesses the attribute when calling len()-- accessing a variable is
 a constant time operation'''

runtimes = []
for i in range(20):
        foo = ['a']*((i+1)**2) #a quadratically increasing list
        start = time.perf_counter()
        length(foo)
        end = time.perf_counter()
        runtimes.append((end-start)*(10**6))

print(runtimes) #no correlation between seq length and runtime
