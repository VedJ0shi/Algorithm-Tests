from positional import *

def insertion_sort(seq):
    '''insertion sort on the PositionalList seq'''
    
    marker = seq.first()
    for _ in range(1, len(seq)): #len(seq) returns _size (defined in DoublyLinkedBase parent class)
        pivot = seq.after(marker)
        current = pivot.element()
        while pivot != seq.first() and current < seq.before(pivot).element():
            seq.replace(pivot, seq.before(pivot).element())
            pivot = seq.before(pivot)
        seq.replace(pivot, current) #may not change anything if while loop not entered
        marker = seq.after(marker) #advance position
        
    return seq



        

