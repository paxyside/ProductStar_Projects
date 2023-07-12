def find_sum_elements(nums, target):
    num_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index:
            return [complement, num]
        num_index[num] = i
    return []

print(find_sum_elements([1,5,7,44,32,112,66], 119))
print(find_sum_elements([15,1,12,155,2,30], 32)) 


 
def is_pangramm(s):
    letters = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    s = s.lower()
    for c in s:
        if (c >= "а" and c <= "я") or c == "ё":
            letters.discard(c)
    return len(letters) == 0
print(is_pangramm('Съешь же ещё этих мягких французских булок да выпей чаю'))

def is_pangram(stroke):
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return alphabet <= set(stroke.lower())
print(is_pangramm('Съешь же ещё этих мягких французских булок да выпей чаю'))

