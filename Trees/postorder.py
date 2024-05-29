#depth-first search where nodes are visited in the order- left subtree, right subtree, current node

class PostorderMixin:
    '''support for performing Postorder traversal of all positions'''

    def postorder(self):
        '''generates a postorder iteration of all positions in the tree'''
        if not self.is_empty():
            for pos in self._subtree_postorder(self.root()):
                yield pos

    def _subtree_postorder(self, pos, order=[]):
        '''non-public generalized postorder traversal; returns ordered list'''
        for child in self.children(pos):
            order = self._subtree_postorder(child, order)
        order.append(pos)
        return order

