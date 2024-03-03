#naive O(n^3) algorithm that determines disjointness of 3 sets
#if the intersection is empty, then the 3 sets are 'disjoint' and returns True
#strategy is to return False once the first common value is found

def is_disjoint(A, B, C): #assumes no individual sequence contains duplicates
    for a in A:
        for b in B:
            for c in C:
                if a==b and b==c and a==c: #checking for common value
                    return False                
    return True

'''best case is A=B=C; worst case is A, B, C distinct (actually A, B distinct sufficient)'''
'''in worst case, O(n^3)'''