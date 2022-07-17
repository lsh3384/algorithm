
def quick_sort(array, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

def binary_search_recursive(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid

    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
