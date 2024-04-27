#copy of Stack, Queue and Deque classes

#0. 
class Empty(Exception):
    pass

#1.
class ArrayStack:
    
    def __init__(self):
        self._data = [] #nonpublic list instance; data storage
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, obj):
        self._data.append(obj) #rightmost element is the last/top element of stack

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
            self.top()
            return f'<Stack({[str(self._data[i]) for i in range(len(self._data))]})>'
        except Empty:
            return f'<Stack()>'

#2.
class ArrayQueue:

    init_capacity = 10  #default value

    def __init__(self):
        self._data = [None]*ArrayQueue.init_capacity #reserves exact amount of memory in array; data storage
        self._size = 0 #actual number of queued elements, as opposed to len of _data
        self._front = 0 #index within _data of the first element in queue
        self._tail = 0 #index within _data of the back of the queue-- next vacant position
    
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
            self._resize(len(self._data)//2) #assures proportionality between number of queued elements and length of _data (memory usage)
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
        
    #define some aliases for main public methods:
    get = dequeue
    put = enqueue

    @classmethod
    def raise_capacity(cls):
        print(f'current initial capacity: {cls.init_capacity}' )
        k = int(input('raise initial capacity for all instances by: '))
        cls.init_capacity = cls.init_capacity + k
        print('implemented')

#3.
class Deque:

    init_capacity = 10  #default value

    def __init__(self):
        self._data = [None]*Deque.init_capacity
        self._size = 0
        self._front = 0
        self._tail = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._tail - 1]
    
    def add_first(self, obj):
        '''enqueue obj to the front '''
        if self.is_empty():
            self._front = 0
            self._data[self._front] = obj
            self._tail = 1
        else:
            self._conditional_resize()
            self._front = (self._front - 1)%len(self._data)
            self._data[self._front] = obj
        self._size = self._size + 1

    def add_last(self, obj):
        '''enqueue obj to the back (same as Queue) '''
        if self.is_empty():
            self._front = 0
            self._data[self._front] = obj
            self._tail = 1
        else:
            self._conditional_resize()
            self._data[self._tail] = obj
            self._tail = (self._tail + 1)%len(self._data)
        self._size = self._size + 1
    
    def del_first(self):
        '''dequeue from the front (same as Queue)'''
        if self.is_empty():
            raise Empty('Deque is empty')
        else:
            first = self._data[self._front]
            self._data[self._front] = None 
            self._front = (self._front + 1)%(len(self._data))
            self._size = self._size - 1
            self._conditional_resize()
            return first
    
    def del_last(self):
        '''dequeue from the back'''
        if self.is_empty():
            raise Empty('Deque is empty')
        else:
            self._tail = (self._tail - 1)%(len(self._data))
            last = self._data[self._tail]
            self._data[self._tail] = None 
            self._size = self._size - 1
            self._conditional_resize()
            return last


    def _conditional_resize(self):
        if len(self._data)//4 <= self._size < len(self._data):
            pass
        else:
            def resize(capacity): #can access self from the enclosing scope
                stored = self._data
                self._data = [None] * (capacity)
                i = self._front
                for k in range(self._size):
                    self._data[k] = stored[i]
                    i = (i + 1)%(len(stored))
                self._front = 0 
                self._tail = self._size      
        
            if self._size == len(self._data):
                resize(2*len(self._data))
            
            elif self._size < len(self._data)//4:
                resize(len(self._data)//2)
        

    def __str__(self):
        try:
            self.first()
            return f'<Deque({[str(self._data[i]) for i in range(len(self._data))]})>'
        except Empty:
            return f'<Deque()>'
        
    @classmethod
    def raise_capacity(cls):
        print(f'current initial capacity: {cls.init_capacity}' )
        k = int(input('raise initial capacity for all instances by: '))
        cls.init_capacity = cls.init_capacity + k
        print('implemented')