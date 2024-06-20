#more robust and faster (but more memory) Linked List structure

class DoublyLinkedBase:
    '''a base class for adapting doubly-linked lists for higher level structures'''

    class _Node:
        def __init__(self, obj, prev, next):
            self._element = obj
            self._prev = prev
            self._next = next
            
        
    def __init__(self):
        self._trailer = self._Node(None, None, None)
        self._header = self._Node(None, None, self._trailer) #_header and _trailer nodes do not contain primary data
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size
    
    def _insert(self, obj, predecessor, successor): #cannot do a positional insert (no concept of index)
        '''inserts new node (containing provided data) in between the two nodes'''
        inserted = self._Node(obj, predecessor, successor)
        predecessor._next = inserted #prior to this, predecessor._next = successor
        successor._prev = inserted
        self._size = self._size + 1
        return inserted

    def _delete_node(self, node):
        '''removes selected node and returns its stored data'''
        obj = node._element
        predecessor = node._prev
        successor = node._next
        node._element = None #dereferences original data for garbage collection
        node._next = None #formal convention for deprecated node
        predecessor._next = successor
        successor._prev = predecessor #bypassing selected node
        self._size = self._size - 1
        return obj
    
