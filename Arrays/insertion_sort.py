
def insertion_sort(seq):
    '''sorts a list seq into ascending order by reordering subarrays from the left onwards'''
    for k in range(len(seq)):
        #k is length of subarray to be considered in the while loop
        current = seq[k]
        j = k
        while j > 0 and current < seq[j-1]:
            seq[j] = seq[j-1]
            j = j - 1
        seq[j] = current
        
    return seq

'''in worst case (seq originally in descending order), inner loop is entered in every outer iteration
-- worst case runtime is in O(0 + 1 + 2 + ... + n) = O(n^2) '''
