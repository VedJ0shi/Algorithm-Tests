#implementing a linear recursive algorithm to reverse list by index

def lin_reverse(seq):
    '''recursively builds a new list using list concatenation (operator overload of +)'''
    last = len(seq)-1 #greatest index of current list
    if last==0:
        return [seq[0]]
    print(vars())
    return ([seq[last]] + lin_reverse(seq[:last]) )

'''runtime is NOT O(n) since each list slicing (seq[:last]) operation take O(n) time'''



