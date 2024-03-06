#better O(n^2) algorithm that determines disjointness of 3 sets

def is_disjoint(A, B, C):
    for a in A:
        for b in B:
            if b==a:
                for c in C:
                    if c==b:
                        return False
    return True

'''best case is when A=B=C, worse case is when A=B & C distinct'''

'''in the B loop, a==b can only happen a maximum of 1 time since
by assumption B has no duplicates => worst case a==b True n times
==> worst case innermost C loop entered n times ==> worst case O(n^2)'''