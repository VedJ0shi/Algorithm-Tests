#recursive algorithm to find a target value in an indexable sequence i.e. list

'''when sequence unsorted, need to do Sequential search which is O(n) and worst
case exhausts entire data
 '''

'''when sequence sorted, can take advantage of ordering and apply Binary search'''

def binary_search(seq, target, low=0, high=-1): #expects seq to be sorted
    if high == -1:
        high = len(seq)-1 #high initialized as greatest index of seq
    if low > high: #would occur when the interval of search becomes empty
        return (False, -1)
    else:
        mid = int((low+high)/2)
        print(vars())
        if target == seq[mid]:
            return (True, mid)
        elif target < seq[mid]:
            return binary_search(seq, target, low, mid-1)
        elif target > seq[mid]: 
            return binary_search(seq, target, mid+1, high )


'''since within in each recursive call, at most one new recursive call can be made
(due to if/elif/else), this is a linear recursive algorithm '''