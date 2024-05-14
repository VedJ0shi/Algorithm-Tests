from linkedstack import Empty

class CircularQueue:
    '''Queue using circular linked list for storage; tail points back to head'''

    #-----------non-public (nested) Node class-----------------#
    class _Node:
        '''a Node object is a pair of references to the primary data and the next Node on linked list'''
        def __init__(self, obj, next):
            self._element = obj
            self._next = next
    #----------------------------------------------------------#
        
    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def enqueue(self, obj):
        '''insert at tail & reconfigure tail-head dependence'''
        enqueued = self._Node(obj, 'temporary')
        try:
            enqueued._next = self._tail._next #update to point to current head
            self._tail._next = enqueued 
        except: #if self._tail = None
            enqueued._next = enqueued #initialized recursively
        self._tail = enqueued
        self._size = self._size + 1

    def dequeue(self):
        '''remove and return from head & reconfigure tail-head dependence'''
        if self.is_empty():
            raise Empty('Queue is empty')
        head_node = self._tail._next
        if head_node != self._tail:
            self._tail._next = head_node._next #releases and replaces reference to current head (bypasses to next node after head)
        else: #if head_node = self._tail (only 1 node)
            self._tail = None
        self._size = self._size - 1
        return head_node._element

    
    def first(self): #returns the 'first' or 'current' element in queue
        if self.is_empty():
            raise Empty('Queue is empty')
        head_node = self._tail._next 
        return head_node._element
    
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next #head becomes new tail

    
    get = dequeue
    put = enqueue

    def __str__(self):
        try:
            return f'<Queue(first={self.first()}, last={self._tail._element}, length={self._size})>'     
        except:
            return '<Queue()>'
        