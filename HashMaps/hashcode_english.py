#implementation of a 'Polynomial accumulation' hash code on English str keys

def hashcode(key, a=33):
    '''applies polynomial accumulation on each byte/char of the English key'''
    hc = 0
    n = len(key)
    for i, char in enumerate(key):
        hc = hc + ord(char)*(a**(n-1-i))
    return hc
    



