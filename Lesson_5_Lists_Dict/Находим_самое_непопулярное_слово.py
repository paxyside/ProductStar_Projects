#Самая не популярная буква

from collections import defaultdict
def count_characters(s):
    counter = defaultdict(int)
    for char in s:
        counter[char] += 1
    return counter
given_string = "Python Star Course for beginners and experts for data science and analytics without sql with code"
# создаем словарь с количеством вхождений каждого символа
char_counts = count_characters(given_string)
# сортируем символы по возрастанию количества вхождений
least_common_chars = sorted(char_counts, key=char_counts.get)[:8]
# выводим 8 наименее часто встречающихся символов без пробелов и запятых
print(''.join(least_common_chars))