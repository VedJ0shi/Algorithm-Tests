#C5-21
import time
import matplotlib.pyplot as pyplot
import numpy as np

'''comparing efficiency of 3 different methods in composing a long str:
1. direct str concatenation
2. multiple appends to temporary (mutable) list and then joining
3. list comprehension with join
'''
def compose_str1(length):
    '''concatenates until str is of given length-- needs to initiate new str object each time (immutability)'''
    mystr = '' #immutable, takes O(n) time to initialize str object of n chars
    start = time.perf_counter()
    while len(mystr) < length:
        mystr = mystr + 'A'
    end = time.perf_counter()
    return end-start

def compose_str2(length):
    mychars = [] #mutable, append with dynamic resizing is an amortized O(1) operation
    start = time.perf_counter()
    while len(mychars) <= length:
        mychars.append('A') #n appends will take amortized O(n) time with multiple resizes of array 
    ''.join(mychars) #returns str of joined chars in the list mychars, takes O(n) time
    end = time.perf_counter()
    return end-start

def compose_str3(length):
    start = time.perf_counter()
    mychars = ['A' for i in range(length)] #take O(n) time, but optimized since no resizing events occur (final array length implicity passed in)
    ''.join(mychars)
    end = time.perf_counter()
    return end-start


def avg_return_val(func, l):
    '''returns average return value of the str composing func over 40 experiments'''
    sum = 0
    for _ in range(40):
        sum = sum + func(l)
    return sum/40

x = np.array([i for i in range(1, 100)]) #x-axis is final length of str
y1 = np.array([avg_return_val(compose_str1, l) for l in x])
y2 = np.array([avg_return_val(compose_str2, l) for l in x])
y3 = np.array([avg_return_val(compose_str3, l) for l in x])

pyplot.plot(x, y1) #linear time, steepest increase in avg runtime wrt final str length --> slowest method
pyplot.plot(x, y2) 
pyplot.plot(x, y3) #linear time, lowest increase in avg runtime wrt final str length --> fastest method
pyplot.show() 

'''Interesting result: surprisingly compose_str1 runs in O(n) time in this code instead O(n^2) since 
the original str object (mystr) has ref count = 1 -- thus the interpreter allows direction mutation of 
underlying str obj (as a dynamic array) as part of a Python runtime optimization'''