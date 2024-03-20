#C4-16

def reverse_str(s, r=''): 
    '''reverses characters in a given str s'''
    if len(s) == 1:
        return r + s[0] #Note: str concatenation is NOT commutative
    r = r + s[-1]
    return reverse_str(s[:-1], r) #s[:-1] makes a new sliced copy in O(n) time

