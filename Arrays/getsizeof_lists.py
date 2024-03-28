#seeing how Python saves list objects (mutable) internally with sys.getsizeof()
import sys

'''lists are saved as dynamic reference arrays'''

print('sys.getsizeof([]):', sys.getsizeof([]))
size = sys.getsizeof([])
print()

data = []
for i in range(20):
    data.append(None) #append the None type obj
    print(data)
    print(f'id(data[{i}]):', id(data[i])) #references the same object in memory (None)
    print('sys.getsizeof(data):', sys.getsizeof(data))
    if sys.getsizeof(data) > size:
        print(f'New array dynamically created with {sys.getsizeof(data)-size} bytes more reserved capacity!')
        size = sys.getsizeof(data)
    print()

'''on 64-bit machine, each memory address is 8 bytes/64 bits-- 
which becomes the fixed cell size of a reference array'''
