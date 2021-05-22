# 병합정렬
# 순서가 뒤죽박죽인 배열이 있을 때 정렬하기 위해 분할과 정복방식을 이용한다

# 1. 데이터를 절반씩 나누어 끝까지 갔다가(분할했다가)
# 2. 다시 절반씩 합치면서 그 안에서 정렬한다.(정복한다)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 재귀함수를 이용해서 끝까지 분할
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = 0
    j = 0
    k = 0

    # 분할된 배열끼리 비교하기
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # 먼저 끝났을 경우
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    return arr
