#C4-11

def is_unique(seq, instances={}):
    '''determines if all elements in a sequence are unique using dictionary'''
    instances[seq[0]] = instances.get(seq[0],0) +1 #.get() returns 0 if given key does not yet exist
    print(vars())
    if instances[seq[0]] > 1:
        return False
    if len(seq) == 1: #base case 
        return True  
    return is_unique(seq[1:], instances)

def is_unique2(seq):
    '''determines uniqueness by recursively checking first element against rest'''
    if len(seq) == 1: #base case
        return True
    for i in range(1, len(seq)):
        if seq[i] == seq[0]:
            return False
    return is_unique2(seq[1:])
