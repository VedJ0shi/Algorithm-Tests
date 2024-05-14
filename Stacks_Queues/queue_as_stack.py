#adapting Queue class for behavior of Stack data struc
#all public methods are Stack methods
from arrayqueue import *

class QStack:
    '''LIFO Stack implementation using Queue object as underlying storage'''

    def __init__(self):
        self._data = ArrayQueue()
        self._top = None
    
    def __len__(self):
        return len(self._data) #returns _size of Queue object
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, obj):
        self._data.enqueue(obj) 
        self._top = obj

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        j = 1
        while j < len(self._data): #inefficient loop
            first = self._data.dequeue()
            self._data.enqueue(first)
            j = j + 1
        if j == 1: #if len(self._data) = 1
            self._top = None
        else:
            self._top = first
        return self._data.dequeue()
    
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._top