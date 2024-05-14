#Queue dequeue() and enqueue() must run in true O(1) time
#--> front of Queue will be at head of linked list
#enqueue() will be insertion at the tail
#dequeue() will be a removal from the head

from linkedstack import Empty

class LinkedQueue:
    '''FIFO Queue using singly linked list for storage'''

    #-----------non-public (nested) Node class-----------------#
    class _Node:
        '''a Node object is a pair of references to the primary data and the next Node on linked list'''
        def __init__(self, obj, next):
            self._element = obj
            self._next = next
    #----------------------------------------------------------#
    
    def __init__(self):
        self._head = None
        self._size = 0
        self._tail = None

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def enqueue(self, obj):
        enqueued = self._Node(obj, None)
        try:
            self._tail._next = enqueued
        except: #if self._tail = None
            pass
        self._tail = enqueued
        self._size = self._size + 1
        if self._size == 1:
            self._head = self._tail

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        first_node = self._head
        self._head = self._head._next #releases and replaces reference to current _head (irreversible)
        self._size = self._size - 1
        if self._size == 0:
            self._tail = None
        return first_node._element
        
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    
    get = dequeue
    put = enqueue

    def __str__(self):
        try:
            return f'Queue(first={self.first()}, last={self._tail._element}, length={self._size})'     
        except:
            return '<Queue()>'
        