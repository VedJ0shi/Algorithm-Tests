from abc import ABCMeta, abstractmethod

class Tree(metaclass=ABCMeta):

    class _Position:
        '''abstraction that represents a node location on the tree'''

        @abstractmethod #all subclasses must override the method
        def element(self):
            '''returns element stored at this position'''

        @abstractmethod
        def __eq__(self, other):
            '''returns True iff other represents same position on the tree'''
        
        
        def __ne__(self, other):
            '''returns True iff other does not represent the same position'''
            return not self is other
        
    @abstractmethod
    def root(self):
        '''returns position of the root node'''

    @abstractmethod
    def parent(self, pos):
        '''returns position of the parent of the node represented by the given position'''
    
    @abstractmethod
    def num_children(self, pos):
        '''returns number of children of the node represented by the given position '''
    
    @abstractmethod
    def children(self, pos):
        '''generates an iteration of positions of the children nodes'''
    
    @abstractmethod
    def __len__(self):
        pass
    

    def is_root(self, pos):
        return self.root() is pos

    def is_leaf(self, pos):
        return self.num_children(pos) == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def depth(self, pos):
        '''recursively calculates depth of the node represented by given position'''
        if self.is_root(pos):
            return 0
        return 1 + self.depth(self.parent(pos))
    
    def height(self, pos=None):
        '''recursively calculates absolute height of the node represented by given position;
        if no arg given, then defaults to finding absolute height of the root'''
        if pos == None:
            pos = self.root()
        if self.is_leaf(pos):
            return 0
        heights = [] #list of relative heights (height relative to child path taken)
        for child in self.children(pos):
            h = 1 + self.height(child)
            heights.append(h)
        return max(heights)
    
    
    