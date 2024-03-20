#C4-15
import copy

def powerset(myset): 
    '''returns the power set of a list myset (expects list to have unique elements)'''

    result = [] #will become a list of lists
    partial = []  

    def directed_powerset(ind=0):

        if ind == len(myset):
            copy_partial = copy.copy(partial)
            result.append(copy_partial) #adds list partial to the list result
            return
        
        partial.append(myset[ind]) #state of partial remembered in each recursive call since it is defined in enclosing scope
        directed_powerset(ind+1)
        partial.pop() #un-appends last entry
        directed_powerset(ind+1)


    directed_powerset() #powerset() calls the inner directed_powerset() function
    return result

    
 


    






    
