from _collections_abc import MutableMapping
#_collections_abc is a built-in module that provides abstract container classes

class MapBase(MutableMapping):
    
    class _Item:
        def __init__(self, k, obj):
            self._key = k
            self._value = obj
        
        def __eq__(self, other):
            return self._key == self._other
        
        def __ne__(self, other) -> bool:
            return not (self == other) #equivalent to not (self.__eq__(other))
        
        def __lt__(self, other):
            return self._key < other._key
        

        

