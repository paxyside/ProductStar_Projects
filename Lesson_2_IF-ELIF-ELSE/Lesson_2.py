a = 2
b = 5
c = 3
import math
#a*x**2+b*x+c=0
D = b**2-4*a*c
if D > 0:
    x1 = (-b-math.sqrt(D))/(2*a)
    x2 = (-b+math.sqrt(D))/(2*a)
    print(f'x1=', x1)
    print(f'x2=', x2)
elif D == 0:
    x = -b/(2*a)
    print(f'x=', x)
else:
    print("Решений нет!")
    
    
#Пример того, как можно решать матан в питончике)