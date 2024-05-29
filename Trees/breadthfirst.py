#breadth-first search
import queue

class BreadthFirstMixin:
    '''support for performing BFS traversal of all positions'''

    def breadthfirst(self):
        '''generates a bfs iteration of all positions in the tree'''
        if not self.is_empty():
            for pos in self._subtree_breadthfirst(self.root()):
                yield pos

    def _subtree_breadthfirst(self, pos, order=[]):
        '''non-public generalized bfs traversal; returns ordered list'''
        q = queue.Queue(maxsize=len(self))
        q.put(pos)
        while not q.empty():
            order.append(q.get())
            for child in self.children(order[-1]):
                q.put(child)
        return order










