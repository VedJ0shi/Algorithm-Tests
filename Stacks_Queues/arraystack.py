#adapting existing list class for the behavior of a LIFO Stack data struc

'''
Stacks should not formally implement indices, __getitem__() & __setitem__(),
 instead implement:
- top() to read from the next element on the stack
- push() to place an element on the stack
- pop() to return and remove next element on the stack 
'''
class Empty(Exception):
    '''raised when accessing element from empty stack'''
    pass

class ArrayStack:
    '''LIFO Stack implementation using list (dynamic reference array) as underlying storage'''

    def __init__(self):
        self._data = [] #nonpublic list instance
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, obj):
        self._data.append(obj) #rightmost element is the last element of stack

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def __str__(self):
        try:
            last = self.top()
        except Empty:
            last = None
        return f'<Stack(Last element:{str(last)}, Length:{len(self)})>'

