#recursion to solve n!


def factorial(n): #expects n non-negative
    '''
    non recursive implementation:
    prod = 1
    for m in range(1,n+1):
        prod = prod * m
    return prod
    '''
    print(vars()) #returns dict of local namespace in each recursive call; in this case-- {'n': ...}

    if n == 0: #no further recursive calls made once base case reached
        return 1
    else:
        return n * factorial(n-1) 
        #when recursive call is made, execution of former call is suspended until call returns
        #different namespace for each active call
