# # Массивы
# # Объявление нового массива
i = []
print(i)

i = [1,2,3]
print(i)

i = list()
print(i)

# Добавление нового элемента .append()

i.append(4)
i.insert(0,0)
print(i)

import timeit
import random

def test_append():
    I = []
    for i in range(10000):  
        I.append(random.randint(0,1000))
print(timeit.timeit('test_append()', globals=locals(), number= 1000))

def test_insert_front():
    I = []
    for i in range(10000):  
        I.insert(0, random.randint(0,1000))
print(timeit.timeit('test_insert_front()', globals=locals(), number= 1000))

# Удаление элементов
last_element = i.pop()
print(f"Last element: {last_element}")
del i[2]
print(i)


# Стеки на основе массива
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
print("stack:", stack)

print('peek', stack[-1])
print('pop:', stack.pop())
print('pop:', stack.pop())
print('pop:', stack.pop())


# Очереди

from queue import Queue

q = Queue()
print(f'empty:{q.empty()}')
q.put(1)
q.put(2)
q.put(3)
print(f"now:{q.empty()}")
print(q.get(block= False))
print(q.get(block= False))
print(q.get(block= False))

from collections import deque