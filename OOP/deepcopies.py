import copy
from class_credcard import CreditCard

'''know that we can declare an alias for a mutable object'''

A = [1, 2, 3, 4] #list is a mutable object in memory

B = A #B is an alias of A
print(B, A)
B.append(5) #will modify A too, since both A and B reference the same list
A[0] = -1 #will modify B too
print("after modification:", B, A)
print()

C = copy.copy(B) #C is a shallow copy of B and A; C references a distinct list
print(C, B, A)
C.append(6)
C[0] = 1
print("after modification:", C, B, A)
print()

Bob = CreditCard(1, 300)
Dylan = CreditCard(2, 1100)
cards = [Bob, Dylan] #list of CreditCard objects
mycopy = copy.copy(cards) #mycopy is a distinct list comprising of aliases to original
print(mycopy[0] == cards[0]) #True since mycopy's elements are aliases of original
mycopy.append(CreditCard(3, 8000))
print(len(mycopy), len(cards)) #successfuly added element to mycopy without changing cards
print()

dcopy = copy.deepcopy(cards)
print(dcopy[0] == cards[0]) #False since dcopy's elements are not aliases of original
dcopy.append(CreditCard(3, 8000))
print(len(dcopy), len(cards)) #successfuly added element to dcopy without changing cards
