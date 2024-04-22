#adapting existing list class for the behavior of a FIFO Queue data struc
from arraystack import Empty

class ArrayQueue:
    '''FIFO Queue implementation using list (dynamic reference array) as underlying storage--
    circularity approach for efficiency, where all modular arithmetic is wrt to length of _data'''

    init_capacity = 10  #default value

    def __init__(self):
        self._data = [None]*ArrayQueue.init_capacity #reserves exact amount of memory in array; data storage
        self._size = 0 #actual number of queued elements, as opposed to len of _data
        self._front = 0 #index within _data of the first element in queue
        self._tail = 0 #index within _data of the back of the queue-- next vacant index
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        '''remove and return first element of queue (FIFO)'''
        if self.is_empty():
            raise Empty('Queue is empty')
        first = self._data[self._front]
        self._data[self._front] = None #rewrite it to None for garbage collection; system will reclaim memory location of the dequeued obj
        self._front = (self._front + 1)%(len(self._data)) #circularity
        self._size = self._size - 1
        if self._size < len(self._data)//4: 
            self._resize(len(self._data)//2) #assures proportionality between number of queued elements and length of _data
        return first
    
    def enqueue(self, obj):
        '''add obj to back of queue'''
        if self._size == len(self._data):
            self._resize(2*len(self._data)) #increases length of _data (recreates list for greater storage)
        self._data[self._tail] = obj
        self._tail = (self._tail + 1)%(len(self._data)) #circularity
        self._size = self._size + 1

    '''.enqueue() advances _tail ; .dequeue() advances _front'''
        
    def _resize(self, capacity): #called from enqueue() for growing or from dequeue() for shrinking
        stored = self._data
        self._data = [None] * capacity #reallocate new array with greater capacity
        i = self._front
        for k in range(self._size):
            self._data[k] = stored[i]
            i = (i + 1)%(len(stored))
        self._front = 0 #reset front index
        self._tail = self._size #reset tail index


    def __str__(self):
        try:
            self.first()
            return f'<Queue({[str(self._data[i]) for i in range(len(self._data))]})>'
        except Empty:
            return f'<Queue()>'
        
    #define some aliases for main methods:
    get = dequeue
    put = enqueue

    @classmethod
    def raise_capacity(cls):
        print(f'current initial capacity: {cls.init_capacity}' )
        k = int(input('raise initial capacity for all instances by: '))
        cls.init_capacity = cls.init_capacity + k
        print('implemented')