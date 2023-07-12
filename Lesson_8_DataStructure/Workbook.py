# a = [1, 2, 3]
# b = [4, 5, 6]
# scalar(a, b) = 1*4 + 2*5 + 3*6 = 32 

class SparseVector:
    def __init__(self, elements_array, size):
        self.elements = {}
        self.size = size
        for i, value in elements_array:
            self.elements[i] = value
    
    def __repr__(self):
        return f"Sparcevector(size ={self.size}, elements = {self.elements}"
    
    def scalar(self, other):
        if self.size != other.size:
            raise Exception("Размеры векторов не равны!")
        scalar_product = 0
        for i, value in self.elements.items():
            if i in other.elements:
                scalar_product += value * other.elements[i]
            return scalar_product
        
        
a = SparseVector([
    (0, 1),
    (1, 2),
    (3, 3),
], size= 10000)

b = SparseVector([
    (0, 4),
    (1, 5),
    (3, 6),
], size= 10000)
    
print(a.scalar(b))