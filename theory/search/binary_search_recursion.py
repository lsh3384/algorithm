def binary_search(array, target, start, end):
    # 재귀 함수 종료 조건
    if start > end:
        return None

    # 중간점 지정
    mid = (start + end) // 2

    #중간점에 찾는 값이 있는지 체크
    if array[mid] == target:
        return mid

    # 중간점이 찾는 값보다 큰 경우 끝값을 중간값-1로 변경
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    # 중간점이 찾는 값보다 작은 경우 처음값을 중간값+1 로 변경
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)