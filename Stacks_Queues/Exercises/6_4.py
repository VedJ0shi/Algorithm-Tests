#R6-4
from classes import *

def clear(stack): #expects ArrayStack obj
    '''recursively clears all elements from stack'''
    if stack.is_empty():
        return 
    stack.pop() #mutates stack and returns top element
    clear(stack)


