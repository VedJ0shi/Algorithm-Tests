#implementing a linear recursive algorithm to find sum of elements in a list

'''linear recursion: when every recursive call initiates at most one other'''

def lin_sum(seq, n):
    '''returns sum of first n elements (indices 0 to n-1) of list seq'''
    if n==0: #base case, when list has been exhausted
        return 0
    
    return (seq[n-1] + lin_sum(seq, n-1))

    


