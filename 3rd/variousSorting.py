import random

#길이 n인 리스트 만들기
def make_arr(n):
    arr = [i for i in range(n)]
    random.shuffle(arr)
    return arr    

#버블정렬
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            #앞의 요소가 뒤의 요소보다 크면
            if arr[j] > arr[j+1]:
                #두 요소의 자리 교체
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

#선택정렬
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        least = i
        for j in range(i+1,n):
            if arr[j] < arr[least]:
                least = j
        arr[i], arr[least] = arr[least], arr[i]

    return arr

#삽입정렬
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        #key의 올바른 자리를 찾는 과정
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

#병합정렬
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = 0; h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr

#퀵정렬
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0] #첫 원소를 피벗으로 함
    tail = arr[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [y for y in tail if y > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

Arr = make_arr(20)
print(Arr)
# print(bubble_sort(Arr))
# print(insertion_sort(Arr))
# print(selection_sort(Arr))
# print(merge_sort(Arr))
# print(quick_sort(Arr))