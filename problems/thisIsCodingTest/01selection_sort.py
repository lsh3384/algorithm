
array = [3, 4, 1, 5, 2, 6]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]