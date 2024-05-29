#depth-first search where nodes are visited in the order- left subtree, current node, right subtree

class InorderMixin:
    '''support for performing Inorder traversal of all positions;  mixed into any concrete subclass of BinaryTreeBase'''

    def inorder(self):
        if not self.is_empty():
            for pos in self._subtree_inorder(self.root()):
                yield pos

    def _subtree_inorder(self, pos, order=[]):
        left = self.left(pos)
        right = self.right(pos)
        if left:
            order = self._subtree_inorder(left, order)
        order.append(pos)
        if right:
            order = self._subtree_inorder(right, order) 
        return order
            





