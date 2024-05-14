#adapting doubly-linked list for public behavior of Deque (Double-ended Queue)
from doublylinkedbase import *
from linkedstack import Empty

class LinkedDeque(DoublyLinkedBase):
    '''Deque implementation using doubly-linked list for storage'''

    def is_empty(self):
        return self._size == 0

    def first(self):
        '''returns first element of queue, stored in node right after the header of linked list'''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element
    
    def last(self):
        '''returns last element of queue, stored in node right before the trailer of linked list'''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element
    
    def add_first(self, obj):
        '''insert new node, containing provided data, between header and current first node'''
        self._insert(obj, self._header, self._header._next)

    def add_last(self, obj):
        '''insert new node, containing provided data, between current last node and trailer'''
        self._insert(obj, self._trailer._prev, self._trailer)
    
    def del_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)

    def del_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)

    def __str__(self):
        try:
            return f'Deque(first={self.first()}, last={self.last()}, length={self._size})'     
        except:
            return '<Deque()>'
        