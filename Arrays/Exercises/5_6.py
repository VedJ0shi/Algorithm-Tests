#R5-6
import ctypes 

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

    def insert(self, k, obj): #insert obj into kth index; shifts subsequent values rightward
        if len(self) + 1 > self._capacity:
            self._resize(2*self._capacity, insert=k) 
        else:
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i-1]          
        self._A[k] = obj
        self._n = self._n + 1

    def __len__(self):
         return self._n
    
    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]
    
    def _resize(self, new, insert=None):
        B = self._make_array(new) #temporary
        if not insert: 
            for i in range(self._n):
                B[i] = self._A[i]
        else:
            for i in range(insert):
                B[i] = self._A[i]
            for i in range(insert, self._n):
                B[i+1] = self._A[i]    
        self._A = B
        self._capacity = new

    def _make_array(self, c):
        return (c * ctypes.py_object)() #returns a py_object_Array type with c cells

    def __repr__(self):
        return f"<DynamicArray(length={self._n}, allocated capacity={self._capacity})>"

    def __str__(self):
        return f'{[self._A[i] for i in range(self._n)]}'









