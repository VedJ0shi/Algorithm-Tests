#creating a robust new class that represents a multidimensional vector

class Vector:

    def __init__(self, *args):
        self._coords = list(args) #args is a tuple, which needs to be converted to a list (mutable)

    @classmethod
    def origin(cls, n):
        k = (0,)*n
        return cls(*k)

    def __len__(self): #returns dimension of vector
        return len(self._coords)
    
    def __getitem__(self, j): #returns jth coordinate of vector
        return self._coords[j]
    
    def __setitem__(self, j, x): #sets jth coordinate to x 
        self._coords[j] = x
    
    def __add__(self, vec): #assumes arg is a list or Vector object
        if len(self) != len(vec):
            raise ValueError("dimensions must agree")
        else:
            result = Vector.origin(len(self)) #constructs origin Vector object
            #implementing coordinate wise addition:
            for i in range(len(self)):
                result[i] = self[i] + vec[i]
        return result
    
    def __repr__(self):
        return f"{self._coords}"


