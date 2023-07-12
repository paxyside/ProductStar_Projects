def function():
    """Эта функция ничего не делает"""
pass  



a=5
b=2
def y(x):
    global a
    a=10
    return a*x+b
print(f"y(1) = {y(1)}")
print(f"a = {a}")


def hello(name):
    print(f'Hello,{name}!')
hello("Anna")
    
    
def add_2(a, b):
    return a+b

def y(x, a, b):
    return a * x + b
for a in range(1, 3):
    for b in range(-1, 1):
        for i in range(3):
            print(f'a = {a}, b = {b} => y = {y(i, a, b)}')
            
            
def y(x,a=5,b=2):
    return a*x+b
print(y(1))
print(y(1, 10, 4))




def g(x):
    return 5*x

def y(x, g):
    return g(x) + 2

print(f"y = {y(1,g)}")
print(f"y = {y(1, lambda x:5*x)}")

minimum = lambda a, b: a if a < b else b
print(minimum(3,5))
    






