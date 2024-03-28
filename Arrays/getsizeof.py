#seeing how Python saves str objects internally with sys.getsizeof()
import sys

'''while len() returns number of (iterable) items in a collection, sys.getsizeof()
returns memory size of the object in RAM'''

'''strs (and lists and tuples) are saved as randomly-accessible arrays in memory, 
even though they are sequential in usage'''


empty = '' #empty str
empty_bytes = b'' #empty bytes obj
print('len(empty):', len(empty) ) #returns 0 (0 chars)
print('len(empty_bytes):', len(empty_bytes)) #returns 0 (0 bytes)
print('sys.getsizeof(empty):', sys.getsizeof(empty) ) #returns 49 bytes in RAM
print('sys.getsizeof(empty_bytes):', sys.getsizeof(empty_bytes)) #returns 33 bytes in RAM

'''An empty str takes up 49 bytes of memory since Python creates supplementary space 
for length info, encoding type, garbage collection overhead, etc.'''

print('sys.getsizeof(empty + "a"):', sys.getsizeof(empty + "a") ) #memory size increments by 1
print('sys.getsizeof(empty_bytes + b"a"):', sys.getsizeof(empty_bytes + b"a")) #memory size increments by 1

print('len("你"):', len('你')) #returns 1 (1 char)
print('len("你".encode()):', len('你'.encode())) #returns 3 (utf-8 encoding maps to 3 bytes)
print('sys.getsizeof("你"):', sys.getsizeof("你")) #returns 76 bytes; memory incremented by 27 bytes since more str object overhead to save Chinese str character
print('sys.getsizeof("你".encode()):', sys.getsizeof("你".encode())) #returns 36 bytes; memory incremented by exactly 3 bytes as expected

print('sys.getsizeof("你你"):', sys.getsizeof("你你")) 
print('sys.getsizeof("你你a"):', sys.getsizeof("你你a"))
print('sys.getsizeof("你你a "):', sys.getsizeof("你你a ")) #memory size increments by 2; str encoding type determines cell size in array  

'''underlying str objects are saved as compact arrays + supplementary storage info'''

#https://stackoverflow.com/questions/17574076/what-is-the-difference-between-len-and-sys-getsizeof-methods-in-python
#https://rushter.com/blog/python-strings-and-memory/#:~:text=Note%20that%20every%20string%20in,takes%2049%20bytes%20of%20memory.
