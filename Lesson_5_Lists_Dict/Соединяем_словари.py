#Соединяем словари и находим самые популярные значения в них
from collections import Counter
dict1={1:10, 2:20, 3901:11, 384:13, 8489:1, 48:10}

dict2={3:30, 4:40, 93:12, 91:41, 95:1, 841:11, 584:11}

dict3={5:50, 6:60, 9:90, 3:13, 7:11}
merged_dict = {**dict1, **dict2, **dict3}
print(len(merged_dict))
value_counts = Counter(merged_dict.values())
most_common_value = max(value_counts, key=value_counts.get)
print(most_common_value)