import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        temp = i
        for j in range(i, n):
            if arr[j] < arr[temp]:
                temp = j
        arr[i], arr[temp] = arr[temp], arr[i]

# insertion sort


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1

# bubble sort


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]


# merge sort
def merge(arr, start, end, mid):
    rt = []
    i = start
    j = mid+1
    k = 0
    while i <= mid and j <= end:

        if arr[i] < arr[j]:
            rt.append(arr[i])
            i = i+1
        else:
            rt.append(arr[j])
            j = j+1

    while i <= mid:
        rt.append(arr[i])
        i = i+1

    while j <= end:
        rt.append(arr[j])
        j = j+1

    for i1 in range(start, end+1):
        arr[i1] = rt[k]
        k += 1


def merge_sort(arr, start, end):
    if start < end:
        mid = (start+end)//2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, end, mid)


# quick sort
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left, right = start + 1, end

    while left <= right:

        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))

quick_sort(arr, 0, len(arr)-1)
for elem in arr:
    print(elem)
