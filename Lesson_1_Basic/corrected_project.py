print('Enter some numbers in one line')
# Тут добавили ковычки недостающие
raw_input = input()
splitted_input = raw_input.split()
parsed_input = list()
for raw in splitted_input:
    parsed_input.append(int(raw))
parsed_input.sort()
# Тут была пропущена бука "p"
print(f'Your result: {parsed_input}')
# Тут команду "int" исправили на "print", а так же убрали лишнюю фигурную скобку
# Данная программа принимает на вход числа и преобразовывает их в списокPavlik1100