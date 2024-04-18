#Stack that supports getMin() --> minimum element in stack 
#getMin() query should run in amortized O(1) time (like pop() or push())
from arraystack import Empty, ArrayStack

class MinStack(ArrayStack):
    '''LIFO Stack with getMin() method; manages two lists behind the scenes'''

    def __init__(self):
        super().__init__()
        self._auxillary = [] #stores minimum values in the order they were pushed
    
    def push(self, obj):
        current_min = self._auxillary[-1]
        super().push(obj)
        if not self._auxillary:
            self._auxillary.append(obj)
        else:
            self._auxillary.append(min(current_min, obj))
    
    def pop(self):
        removed = super().pop() 
        self._auxillary.pop() #pop() is the list operation not stack operation
        return removed

    def getMin(self):
        return self._auxillary[-1]

