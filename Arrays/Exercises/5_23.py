#C5-23
import time
import matplotlib.pyplot as pyplot
import numpy as np

'''comparing efficiency of 2 different methods in building a list:
1. multiple appends
2. list comprehension
'''

def avg_return_val(func):
    def wrapper(length):
        sum = 0
        for _ in range(40):
            sum = sum + func(length)
        return sum/40
    return wrapper

@avg_return_val
def build_list1(length):
    mylist = []
    start = time.perf_counter()
    while len(mylist) <= length:
        mylist.append(None)
    end = time.perf_counter()
    return end-start


@avg_return_val
def build_list2(length):
    start = time.perf_counter()
    mylist = [None for i in range(length)]
    end = time.perf_counter()
    return end-start

x = np.array([i for i in range(1, 101)]) #x-axis is final length of list
y1 = np.array([build_list1(l) for l in x])
y2 = np.array([build_list2(l) for l in x])

pyplot.plot(x, y1)
pyplot.plot(x, y2)
pyplot.show()