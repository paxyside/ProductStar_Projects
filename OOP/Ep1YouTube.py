# class Point:
#     color = 'red'
#     circle = 2
    
    # def __new__(cls, *args, **kwargs):
    #     print('Call __new__ for' + str(cls))
    #     return super().__new__(cls)
    
    # def __init__(self, x=0, y=0):
    #     self.x = x
    #     self.y = y
    
    # def __del__(self):
    #     print(f'Deleted: {self.x}')
                  
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
        
#     def get_coords(self):
#         return self.x, self.y
    
# pt = Point(10, 20)
# print(pt)

# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
    
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
    
    
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
        
#     def get_coord(self):
#         return self.x, self.y
    
#     @staticmethod
#     def norm2(x, y):
#         return x*x + y*y




# v = Vector(1, 200)
# print(Vector.validate(5))
# res = v.get_coord()
# print(res)
# print(v.norm2(5,6))

# from accessify import private, protected
# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.__x = self.__y = 0
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y
#     @private
#     @classmethod    
#     def check_value(cls, x):
#         return type(x) in (int, float)
        
#     def set_coord(self ,x ,y):
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y
#         else :
#             raise ValueError('Coord must be numbers')
#     def get_coord(self):
#         return self.__x, self.__y
        
# pt = Point(1,2)
# pt.set_coord(10, 20)
# print(pt.get_coord())
# print(pt._Point__x) # обращение к приватному методу


# class Point:
#     MIN_COORD = 0
#     MAX_COORD = 100
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def set_coord(self, x, y):
#         if self.MIN_COORD <= x <= self.MAX_COORD:
#             self.x = x
#             self.y = y
#     def __getattribute__(self, item):
#         if item == 'x':
#             raise ValueError('Not found')
#         else:
#             return object.__getattribute__(self, item) 
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('Error')
#         else:
#             object.__setattr__(self, key, value)
#     def __getattr__(self, item):
#         return False
#     def __delattr__(self, item):
#         object.__delattr__(self, item) 
    
# pt1 = Point(1,2)
# pt2 = Point(10,20)
# print(pt1.__dict__)

# Паттерн моносостояния
# class ThreadData:
#     __shared_attrs = {
#         'name': 'thread_1',
#         'data': {},
#         "id": 1
#     }
    
#     def __init__(self):
#         self.__dict__ = self.__shared_attrs
        
        
# td1 = ThreadData()
# th2 = ThreadData()
# th2.id = 3
# td1.attr_new = 'new_attr'
# print(th2.__dict__)

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
        
    def get_old(self):
        return self.__old
    
    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)
        
p = Person('Pavel', 22)
p.set_old(35)
print(p.get_old())
p.old = 35
print(p.old)

