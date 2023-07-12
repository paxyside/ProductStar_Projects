# Вывод номера строки
import sys

try:
    a = 5/0
except ZeroDivisionError as ex:
    line_num = sys.exc_info()[-1].tb_lineno
    print('Error in line %s: %s' % (str(line_num), str(ex)))
    
    
# Вызов исключения
def print_age():
    age = input('Введите ваш возраст: ')
    if int(age) < 0:
        raise ValueError('Возраст не может быть меньше 0!')
    else:
        print('Вы проходите!')
print_age()

#Пользовательское исключение

class TooLongNameException(Exception):
    pass
class TooShortNameException(Exception):
    pass
class NameIsEmpty(Exception):
    pass

def check_name():
    name = input('Введите имя пользователя для регистрации: ')
    if len(name) == 0:
        raise NameIsEmpty("Имя пользователя не может быть пустым")
    elif len(name) > 10:
        raise TooLongNameException("Слишком длинное имя пользователя")
    elif len(name)<2:
        raise TooShortNameException('Слишком короткое имя пользователя')
    
    else:
        print('Имя пользователя подходит!')

check_name()