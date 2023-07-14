#sentence = input("Введите предложение: ")
#word = sentence.split()
#print("Количество слов в предложении:")
#print(len(word))
# Пример операции на подсчет слов в предложении

sentence = input("Введите предложение: ")

word_count = {}
for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1    

num_unique_words = len(word_count)

most_frequent_word = ""
max_count = 0
for word, count in word_count.items():
    if count > max_count:
        most_frequent_word = word
        max_count = count
        
print("Предложение имеет ", num_unique_words, " слов")
print("Самые частые слова: ", most_frequent_word)
        

