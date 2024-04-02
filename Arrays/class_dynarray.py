import ctypes #provides low-level arrays built on PyObjects

class DynamicArray:
    '''emulates underlying memory behavior of list'''

    def __init__(self):
        '''creates empty array from ctype module'''
        self._n = 0 #current number of elements, initially empty
        self._capacity = 1 #current capacity
        self._A = self._make_array(self._capacity)
    
    def append(self, obj):
        if len(self) + 1 > self._capacity: #if self._n == self._capacity
            self._resize(2*self._capacity) #doubles capacity
        self._A[self._n] = obj
        self._n = self._n + 1     
    
    def __len__(self):
         return self._n
    
    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]
    
    def _resize(self, new):
        B = self._make_array(new) #temporary 
        for i in range(self._n):
            B[i] = self._A[i] 
        self._A = B
        self._capacity = new

    def _make_array(self, c):
        return (c * ctypes.py_object)() #returns a py_object_Array type
    
   
    def __repr__(self):
        return f"<DynamicArray(length={self._n}, allocated capacity={self._capacity})>"