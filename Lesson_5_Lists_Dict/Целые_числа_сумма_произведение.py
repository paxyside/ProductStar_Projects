natural_numbers = list(range(5, 15))
even_number = natural_numbers[1:10:2]
print(even_number)

from functools import reduce

product = reduce(lambda x, y: x*y,even_number)
print(product)
sum = sum(even_number)
print(sum)

even_number.append(product)
even_number.append(sum)
even_number.sort(reverse=True)
print(even_number)

even_number = str(even_number)
print(type(even_number))
print(even_number)


print("=".join(even_number))