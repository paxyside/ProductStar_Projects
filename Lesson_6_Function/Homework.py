import math


def discriminant(a, b, c):
    """Функция нахождения дискриминанта"""
    return b**2-4*a*c

def solve(a, b, c):
    """Функция решения квадратного уравнения"""
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / 2 / a
        x2 = (-b - math.sqrt(d)) / 2 / a
        print(f"Два корня, x1= {x1}, x2= {x2}")
              
    elif d == 0:
        x =  - b / 2 / a
        print (f"В этом уравнении один корень: {x}")
        
    else:
        print("Решений нет!")
        
solve(1, 2, 1)
solve(2, 5, 3)
solve(1, -1, 3)
solve(1, 11, 111)
solve(12, 34, 56)
solve(-12, 12, -12)