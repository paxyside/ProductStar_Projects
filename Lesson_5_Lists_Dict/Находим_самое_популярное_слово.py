s = 'kafka python course stack flow dict list python stack course star product star product analytics flow star kafka stack flow ython list set ist fit predict dict list python ourse ython ourse star product ist fit predict analytics kafka stack flow product ist fit predict analytics star flow dict flow list python course stack flow dict list python stack course'
words = s.split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
 #находим слово с максимальной частотой и меньшее в лексикографическом порядке
max_word = ''
max_count = 0
for word in word_freq:
    if word_freq[word] > max_count:
        max_word = word
        max_count = word_freq[word]
    elif word_freq[word] == max_count and word < max_word:
        max_word = word
print(max_word)