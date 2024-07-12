from mapbase import *

class MapStorageException(Exception):
    pass


class ProbeHashMap(MapBase):
    '''Open-addressed hashmap with linear probing for collision resolution 
        and fixed-length array for storage'''

    def __init__(self, max_size):
        self._map = [()]*max_size #fixed-length array that stores _Item instances
        self._size = 0 #number of occupied slots in _map

    def __len__(self):
        return self._size
    
    def __getitem__(self, k):
        i = hash(k) % len(self._map)
        if isinstance(self._map[i], tuple):
            raise KeyError('Key not found')
        if self._map[i]._key == k:
            return self._map[i]._value
        else:
            #linear probe to search thru consecutive slots:
            j = (i+1) % len(self._map)
            while not isinstance(self._map[j], tuple):
                if j == i:
                    break
                if self._map[j]._key == k:
                    return self._map[j]._value
                j = (j+1) % len(self._map)
            raise KeyError('Key not found')


    def __setitem__(self, k, obj):
        i = hash(k) % len(self._map) #index compression is where collisions may occur
        if isinstance(self._map[i], tuple):
            self._map[i] = self._Item(k, obj)
            self._size = self._size + 1
            return
        elif self._map[i]._key is None:
            self._map[i]._key = k
            self._map[i]._value  = obj
            self._size = self._size + 1
            return
        elif self._map[i]._key == k:
            self._map[i]._value = obj
            return
        else:
            #linear probe to search for empty or available slots or for matching key:
            j = (i+1) % len(self._map)
            while not isinstance(self._map[j], tuple):
                if j == i:
                    raise MapStorageException('Cannot add new items; reached max size')
                if self._map[j]._key is None: #if available slot
                    self._map[j]._key = k
                    self._map[j]._value  = obj
                    self._size = self._size + 1
                    return
                elif self._map[j]._key == k:
                    self._map[j]._value = obj
                    return
                j = (j+1) % len(self._map)
            self._map[j] = self._Item(k, obj) #probing found empty slot
            self._size = self._size + 1
            return


    def __delitem__(self, k):
        i = hash(k) % len(self._map)
        if isinstance(self._map[i], tuple):
            raise KeyError('Key not found')
        if self._map[i]._key == k:
            self._map[i]._key = None #deprecates _Item instance; now it is an available slot
            self._size = self._size - 1
            return
        else:
            #linear probe to search thru consecutive slots:
            j = (i+1) % len(self._map)
            while not isinstance(self._map[j], tuple):
                if j == i:
                    break
                if self._map[j]._key == k:
                    self._map[j]._key = None
                    self._size = self._size - 1
                    return
                j = (j+1) % len(self._map)
            raise KeyError('Key not found')
        

    def __iter__(self):
        for i in range(len(self._map)):
            if isinstance(self._map[i], self._Item) and not self._map[i]._key is None:
                yield self._map[i]._key
                

    def __str__(self):
        return f'{[(k, self[k]) for k in self]}' 

