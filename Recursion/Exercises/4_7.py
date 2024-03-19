#R4-7

def str_to_int(digits, i=0, a=0):
    '''converts str of digits to corresponding int object'''
    multiplier = 10**(len(digits)-1-i)
    a = a + int(digits[i])*multiplier
    i=i+1
    if i==len(digits):
        return a
    return str_to_int(digits, i, a) #tail recursive, with parameter i incremented in the code

