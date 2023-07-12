# Как склеить два списка в словарь
names = ['igor', 'dasha', 'martin', 'vladimir', 'rishat', 'maria', 'marat', 'petr', 'dima', 'polina', 'katya', 'elena']
occupations = ['smm', 'developer', 'analyst', 'president', 'analyst', 'ceo', 'customer development', 'founder', 'developer', 'ml engineer', 'product manager', 'cmo']
proffesion = dict(zip(names, occupations))
print(proffesion)

#Соединяем два списка в один
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 12, 13]

c = sorted(list(set(a) & set(b)))
print (c)