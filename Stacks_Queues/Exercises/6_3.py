#R6-3
from classes import *

def transfer(stack1, stack2): #expects both args to be ArrayStack objects
    '''transfers elements of stack1 to stack2'''

    while not stack1.is_empty():
        top = stack1.pop()
        stack2.push(top)

    return stack2

