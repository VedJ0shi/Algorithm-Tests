#R4-1 (from 'Data Structures and Algorithms' by Goodrich, Tamassia, Goldwasser)

def find_max(seq, max=(0,0), i=-1):
    '''returns the maximum element and its (greatest) index'''
    if i == -1: #initialization
        i = len(seq) - 1
        max = (seq[i], i)
    if seq[i] > max[0]:
        max = (seq[i], i)
    if i == 0:
        return max
    return find_max(seq, max, i-1) #tail recursive

'''
runtime is in O(n)-- n recursive calls, each taking O(1) time
recursive depth is also O(n)
 '''

