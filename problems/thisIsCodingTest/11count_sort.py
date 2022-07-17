


def count_sort(array):
    count = [0] * (max(array) + 1)
    for i in range(len(array)):
        count[array[i]] += 1
    print(count)

array = [1, 2, 3, 1, 4, 5, 1, 2, 3, 4]
count_sort(array)

