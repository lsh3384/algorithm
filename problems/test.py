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

def binary_search_iterative(array, target, start, end):
    while start > end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True





def solution(id_list, report, k):
    dict_report = {}
    for i in id_list:
        dict_report[i] = set()

    for j in report:
        a, b = j.split()
        dict_report[b].add(a)

    answer = [0 for _ in range(len(id_list))]

    for key, v in dict_report.items():
        if len(v) >= k:
            for name in v:
                answer[id_list.index(name)] += 1

    return answer

def sequential_search(array, n, target):
    for i in range(n):
        if array[i] == target:
            return i + 1

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j - 1] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

def insertion_sort(array):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j-1] < array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break

def quick_sort(array, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end or array[pivot] > array[left]:
            left += 1
        while right > start or array[pivot] < array[right]:
            right += 1

        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
