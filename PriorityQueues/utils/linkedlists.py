class Empty(Exception):
    '''raised when accessing element from empty object'''
    pass

#----------------------------------------------------#

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
#-------------------------------------------------------#


class PositionalList(DoublyLinkedBase):
    '''sequential container of elements allowing positional access'''

    class _Position:
        '''encapsulates an underlying linked list node'''

        def __init__(self, container, node):
            self._container = container #of type PositionalList
            self._node = node #of type _Node

        def element(self):
            return self._node._element
    
        def __eq__(self, other) -> bool:
            '''comparison returns True iff the two _Position instances encapsulate the same node'''
            if type(self) == type(other): #other must also be of type _Position
                return self._node is other._node #equivalence: both _Position instances storing same _Node instance
            return False

        def __ne__(self, other) -> bool:
            return not self._node is other._node

        
    def _validate(self, pos):
        '''return underlying node; raise Exceptions if invalid'''
        if not isinstance(pos, self._Position):
            raise TypeError('must be of _Position type')
        if pos._container is not self:
            raise ValueError('position does not belong to this List')
        if pos._node._next is None: #convention for deprecated underlying node
            raise ValueError('position is no longer valid')
        return pos._node
    

    def _make_position(self, node):
        '''returns a _Position instance encapsulating given node'''
        if node is self._header or node is self._trailer:
            return None
        else: 
            return self._Position(self, node) #constructs new _Position instance contained inside the current Positional List

    
    def first(self):
        return self._make_position(self._header._next)


    def last(self):
        return self._make_position(self._trailer._prev)
    

    def before(self, pos):
        '''provides interior list access'''
        node = self._validate(pos)
        return self._make_position(node._prev)


    def after(self, pos):
        '''provides interior list access'''
        node = self._validate(pos)
        return self._make_position(node._next)
    

    def __iter__(self):
        '''generates forward iteration of elements'''
        cursor = self.first()
        while cursor != None: 
            yield cursor.element()
            cursor = self.after(cursor)

    
    def _insert(self, obj, predecessor, successor): #override inherited method
        '''inserts new node (containing provided data) and returns its position'''
        node = super()._insert(obj, predecessor, successor)
        return self._make_position(node)
    
    def delete(self, pos):
        '''removes underlying node at the given position and returns its data'''
        node = self._validate(pos)
        return super()._delete_node(node)
    
    def add_first(self, obj):
        return self._insert(obj, self._header, self._header._next)
    
    def add_last(self, obj):
        return self._insert(obj, self._trailer._prev, self._trailer)
    
    def add_before(self, pos, obj):
        node = self._validate(pos)
        return self._insert(obj, node._prev, node)

    def add_after(self, pos, obj):
        node = self._validate(pos)
        return self._insert(obj, node, node._next)

    def replace(self, pos, obj):
        '''replace data of the node at given position with new data'''
        node = self._validate(pos)
        node._element = obj