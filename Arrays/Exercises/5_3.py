#R5-3
import sys

data = []
size = sys.getsizeof(data)
print(f'BEFORE len(data): {len(data)}, sys.getsizeof(data): {size} ')
sizes = []
limit = 10
for i in range(10000):
    '''grow underlying array normally, but shrink it by half whenever length reaches a power of 10 '''
    data.append(None)
    if sys.getsizeof(data) < size:
        sizes.append((f'prev: {size}', f'decreased to:{sys.getsizeof(data)}')) 
    size, length = (sys.getsizeof(data), len(data))
    if length == limit:
        while len(data) > length/2:
            data.pop()
        limit = limit*10

print(sizes)
print(f'AFTER len(data): {length}, sys.getsizeof(data): {size} ')



    
