#R5-8
import time
import matplotlib.pyplot as pyplot
import numpy as np

def get_pop_time(k, n):
    '''returns time spent on .pop(index=k) on a list of fixed length n'''
    temp = [None]*n
    start = time.perf_counter()
    temp.pop(k)
    end = time.perf_counter()
    return end-start 


def avg_return_val(func, k, n):
    '''returns average return value of func (with arg k passed to it) over 40 experiments'''
    sum = 0
    for _ in range(40):
        sum = sum + func(k, n)
    return sum/40

x = np.array([10, 100, 1000, 10000])

y1 = np.array([avg_return_val(get_pop_time, n-1, n)  for n in x])
y2 = np.array([avg_return_val(get_pop_time, n//2, n)  for n in x])
y3 = np.array([avg_return_val(get_pop_time, n//4, n)  for n in x])
y4 = np.array([avg_return_val(get_pop_time, 0, n)  for n in x])

pyplot.plot(x, y1) #popping from the end is constant wrt length of list
pyplot.plot(x, y2) #linear
pyplot.plot(x, y3) #linear
pyplot.plot(x, y4) #popping from the first index is linear (steepest)
pyplot.show() 