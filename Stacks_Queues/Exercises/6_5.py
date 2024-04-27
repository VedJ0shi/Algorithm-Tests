#R6-5
from classes import *

def reverse(list1): #expects a non-empty list
    '''returns a reversed version of list1'''
    helper_stack = ArrayStack()
    list2 = []
    for element in list1:
        helper_stack.push(element)

    while not helper_stack.is_empty():
        list2.append(helper_stack.pop())

    return list2