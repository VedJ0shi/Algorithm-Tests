from priorqueuebase import *
from utils.linkedlists import *


class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self) == 0
    
    def add(self, key, value):
        new_item = self._Item(key, value)
        current = self._data.last()
        prev_pos = self._data.before #callable
        while not current is None:
            if current.element() < new_item:
                break
            current = prev_pos(current)
        if current is None: #made it to self._header node in the underlying linked list
            self._data.add_first(new_item)
        else:
            self._data.add_after(current, new_item)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        min_pos = self._data.first()
        item = min_pos.element()
        return (item._key, item._value)
    
    def dequeue_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        min_pos = self._data.first()
        item = self._data.delete(min_pos)
        return (item._key, item._value)
