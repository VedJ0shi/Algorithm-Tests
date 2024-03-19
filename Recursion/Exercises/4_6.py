#R4-6

'''nth Harmonic number is [1]+[1/2]+[1/3]+...+[1/n]'''

def harmonic(n):
    if n==1:
        return 1

    return ((1/n) + harmonic(n-1)) #NOT tail recursive (not as efficient)

'''runtime is O(n)'''

def harmonic_TR(n,a=0): #a is the sum accumulator
    '''employs tail recursion'''
    a = a + (1/n)
    if n == 1:
        return a
    else:
        return harmonic_TR(n-1,a)
    