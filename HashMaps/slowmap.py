from mapbase import *

class SlowMap(MapBase):
    '''Slow-access map that uses an unsorted list for storage'''

    def __init__(self):
        self._map = []  #array of _Item instances
    
    def __len__(self):
        return len(self._map)

    def __getitem__(self, k):
        for item in self._map:
            if item._key == k:
                return item._value
        raise KeyError('Key not found')
    
    def __setitem__(self, k, obj):
        for item in self._map:
            if item._key == k:
                item._value = obj
                return 
        self._map.append(self._Item(k,obj))

    def __delitem__(self, k):
        for j in range(len(self._map)):
            if self._map[j]._key == k:
                self._map.pop(j)
                return
        raise KeyError('Key not found')

    def __iter__(self):
        for item in self._map:
            yield item._key
                

    def __str__(self):
        return f'{[(k, self[k]) for k in self]}' #relies on .__iter__() & .__getitem__()
