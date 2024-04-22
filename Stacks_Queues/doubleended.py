#adapting existing list class for the behavior of a Double-Ended Queue data struc
from arraystack import Empty

class Deque:
    '''Double-Ended Queue implementation using list as underlying storage--
    circularity approach for efficiency, where all modular arithmetic is wrt to length of _data'''

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