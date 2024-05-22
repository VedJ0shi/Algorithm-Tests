#function that produces an array-based tree from a given linked-base tree (array-based sheme on p.325 )
from linkedbinarytree import LinkedBinaryTree

def linked_to_array(tree): #expects a non-empty instance of LinkedBinaryTree
    '''recursively calculates array indices for all the linked nodes on the binary tree'''

    arr = [()] #initialized; array length may double multiple times as algorithm progresses
    root_pos = tree.root()
    arr[0] = root_pos.element()

    def _build_array(pos=root_pos, j=0):
        if tree.num_children(pos) > 0:
            if 2*j + 2 > len(arr) - 1: #will first run along the rightmost branch of execution
                increase = (2*j + 2) - (len(arr) - 1)
                arr = arr + [()]*increase 
            left_pos = tree.left(pos)
            right_pos = tree.right(pos)
            if right_pos:
                i = 2*j + 2
                arr[i] = right_pos.element()
                _build_array(right_pos, i)
            if left_pos:
                i = 2*j + 1
                arr[i] = left_pos.element()
                _build_array(left_pos, i)
            
    _build_array() 
    return arr 


'''Memory: final length of arr is 1+max value of the 'j' arg across all 
recursive calls-- array length can exponentially increase in worst case'''









