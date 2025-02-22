import math
class Vector:

    def __init__(self, *args):
        if not all(isinstance(x, (int,float)) for x in args):
            raise TypeError("All components must be numbers")
        
        self.components = tuple(args)
    
    def __str__(self):
        return f"Vector({', '.join(map(str,self.components))})"
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension to be added")

        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def __sub__(self,other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension to be subtracted")

        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self,other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension to be multiplied")
        
        return sum(a*b for a,b in zip(self.components,other.components))
    
    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.components))
            
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize the zero vector")
        return Vector(*(a / mag for a in self.components))
    
    def __rmul__(self, scalar):    
        new_components = tuple(scalar * component for component in self.components)
        return Vector(*new_components)

v1 = Vector(1,4,5)
v2 = Vector(1,3,6)
v5 = 3*v1
dot_product = v1*v2
print(v1+v2)
print(v1-v2)  
print(dot_product) 
print(v1.magnitude())
print(v2.normalize())
print(v5)