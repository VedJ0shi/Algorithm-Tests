#implementing a binary recursive algorithm to find sum of elements in a list

'''binary recursion: when every recursive call initiates at most two others'''

def bin_sum(seq, start=0, stop=-1):
    '''return sum of elements in list slice seq[start:stop]'''
    if stop == -1:
        stop = len(seq)-1
    
    if start == stop: #base case
        return seq[start]

    else:
        mid = int((start+stop)/2)
        return (bin_sum(seq, start, mid) + bin_sum(seq, mid+1, stop) )


'''if len(seq) = n, then both of the recursive calls are effectively running the
 same algorithm on an input of size n/2 --> t(n) = 2t(n/2) + 1 --> t(n) is in O(n) '''

'''recursive depth d(n) is in O(logn) since an input of 2n (doubling) would increase the
depth of recursive calls by one'''