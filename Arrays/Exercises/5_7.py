#R5-7

def find_duplicate(special_seq):
    '''special_seq is of length n containing all ints from 1 to n-1; there is one duplicate'''
    sum = 0
    max = len(special_seq) - 1
    for i in range(len(special_seq)):
        sum = sum + special_seq[i] 
    #sum will account for the duplicate
    return sum - ((max*(max-1)/2) + max) #second term is the closed form solution to the arith series





