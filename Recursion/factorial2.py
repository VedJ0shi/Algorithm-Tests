#employing 'tail recursion' to reduce cumulative memory storage

def factorial(n, a=1): #a is the product accumulator
    if n == 1:
        return a
    a = a*n
    print(vars())
    return factorial(n-1, a) #return value of recursive call immediately returned by enclosing recursion

