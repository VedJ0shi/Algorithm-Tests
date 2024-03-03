#naive O(n^2) algorithm that determines if elements in sequence are unique

def is_unique(seq): #len(seq)=n
    for i in range(len(seq)): #from i=0 to i=n-1
        for j in range(i+1, len(seq)):
            if seq[j] == seq[i]:
                return False
    return True

'''worst case is no duplicates in seq  
=> worst case proportional to (n-1)+(n-2)+...+2+1 = (n-1)(n-2)/2 ~ n^2
=> worst case O(n^2)
'''

