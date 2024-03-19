#C4-12

def product(m,n,a=0): #a is the sum accumulator
    '''computes product of positive ints m & n using only addition/subtraction'''
    if n == 0:
        return a
    return product(m,n-1,a+m) #tail recursive


    