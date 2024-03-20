#C4-19

def rearrange_integers(nums):
    '''rearranges list nums of ints such that all even values appear before odd values'''
    evens = []
    odds = []

    def split(i=0):
        if i == len(nums):
            return      
        
        if nums[i] % 2 != 0:
            odds.append(nums[i])
        else:
            evens.append(nums[i]) #Note: append() is in amortized O(1) time since lists are randomly (not sequentially) accessed
        
        split(i+1)

    split()

    return evens + odds

#https://stackoverflow.com/questions/33044883/why-is-the-time-complexity-of-pythons-list-append-method-o1
