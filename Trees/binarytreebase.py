from abc import abstractmethod
from treebase import TreeBase


class BinaryTreeBase(TreeBase):
    '''inherits from the abstract Tree class; is an abstract class itself'''

    @abstractmethod
    def left(self, pos):
        '''returns position of the left child of the node represented by given position'''

    @abstractmethod
    def right(self, pos):
        pass
    

    def sibling(self, pos):
        '''returns position of the sibling of the node represented by given position'''
        if self.is_root(pos):
            return None #root has no sibling
        parent = self.parent(pos)
        if pos is self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)
        
    def children(self, pos):
        '''generates an iteration of positions of children nodes'''
        for child in (self.left(pos), self.right(pos)):
            if child is not None:
                yield child
    
    
        