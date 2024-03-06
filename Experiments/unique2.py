#better O(nlogn) algorithm that determines if elements in sequence are unique

def is_unique(seq):
    seq.sort() #edits the  list seq so that it is numerically sorted
    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            return False
    return True

'''sort() guarantees worst case run time of O(nlogn) and subsequent loop is O(n) (n-1 itrns)
==> worst case O(nlogn) '''

