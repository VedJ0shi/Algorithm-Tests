from priorqueuebase import *
from utils.linkedlists import *


class UnsortedPriorityQueue(PriorityQueueBase):
    
    def __init__(self):
        self._data = PositionalList() #stores _Item instances
    
    def __len__(self):
        return len(self._data)  #returns _size attribute defined in DoublyLinkedBase
    
    def is_empty(self):
        return len(self) == 0

    def _find_min(self): #private utility method
        '''returns position of item with minimum key; traverses entire _data'''
        if self.is_empty():
            raise Empty('Priority queue is empty')
        current = self._data.first()
        next_pos = self._data.after #next is now a callable
        walk = next_pos(current)
        while not walk is None:
            if walk.element() < current.element() : #.element() returns an _Item instance
                current = walk
            walk = next_pos(walk)
        return current

    def add(self, key, value):
        '''since _data is unsorted, this simply adds to end of PositionalList'''
        self._data.add_last(self._Item(key,value)) #_element of the inserted node is an _Item object

    def min(self):
        pos = self._find_min()  #O(n) task
        item = pos.element()
        return (item._key, item._value)
    
    def dequeue_min(self):
        pos = self._find_min()  #O(n) task
        item = self._data.delete(pos)
        return (item._key, item._value)



            


        




