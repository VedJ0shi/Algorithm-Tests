
class PriorityQueueBase:
    '''Base class for a keys-based priority queue'''

    class _Item:
        '''single unit of store in priority queue'''

        def __init__(self, k, obj):
            self._key = k   #numerical (int/float)
            self._value = obj
        
        def __lt__(self, other):
            return self._key < other._key

        

        

        