#C4-9

def find_extremes(seq, i=0):
    '''returns min and max of list seq; uses built-in min()/max() functions'''
    if i == len(seq)-1: #base case
        return (seq[i], seq[i])
    
    _max, _min = find_extremes(seq, i+1)
    return (max(seq[i], _max), min(seq[i], _min))
    
'''essentially, _max and _min are the stored max and min values in seq[i+1:]'''
    
'''runtime is O(n)'''

    