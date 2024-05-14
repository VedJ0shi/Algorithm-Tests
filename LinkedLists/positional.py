from doublylinkedbase import *

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


    #-------------------------------private utility methods -----------------------------#
        
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
        
    #-----------------------------------------------------------------------------#

    
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
        '''inserts new node (containing provided data) and returns new position'''
        node = super()._insert(obj, predecessor, successor)
        return self._make_position(node)
    
    def _delete(self, pos):
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
        
