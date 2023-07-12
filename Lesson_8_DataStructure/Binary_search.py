# Бинарный поиск

def binary_search(array, target, low, high):
    # Центральный элемент
    mid = (high + low) // 2
    if high >= low and mid < len(array):
        # Центральный элемент равен target, который мы ищем
        if array[mid] == target:
            return mid
        # target меньше, чем центральный элемент, поэтому мы будем искать в левом подмассиве
        elif array[mid] > target:
            return binary_search(array,target,low,mid - 1)
        # target больше, чем центральный массив, поэтому ищем в правом подмассиве
        else:
            return binary_search(array, target, mid + 1, high)
    else:
        # Lov > High, мы уже посмотрели весь массив и не нашли искомый элемент
        return None
    
l = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 20, 21, 23, 24, 47, 90]
print(binary_search(l, 4, 0, len(l)))
print(binary_search(l, 100, 0, len(l)))