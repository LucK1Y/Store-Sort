def quick_Part(arr, low, high):
    pivotindex = (low+high)/2
    pivotvalue = arr[pivotindex]
    arr[high], arr[pivotindex] = arr[pivotindex], arr[high]
    sp = low
    for su in range(low, high):
        if arr[su] < pivotvalue:
            arr[sp], arr[su] = arr[su], arr[sp]
            sp = sp+1
    arr[sp], arr[high] = arr[high], arr[sp]
    return sp


def quick_Sort(arr, lo, hi):
    if lo < hi:
        pivotindex = quick_Part(arr, lo, hi)
        quick_Sort(arr, lo, pivotindex-1)
        quick_Sort(arr, pivotindex+1, hi)


def merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    arr1 = arr[:len(arr)/2]
    arr2 = arr[len(arr)/2:]
    arr1 = merge_Sort(arr1)
    arr2 = merge_Sort(arr2)
    e1 = 0
    e2 = 0
    for i in range(len(arr)):
        if e1 >= len(arr1):
            arr[i] = arr2[e2]
            e2 = e2+1
        elif e2 >= len(arr2):
            arr[i] = arr1[e1]
            e1 = e1+1
        elif arr1[e1] <= arr2[e2]:
            arr[i] = arr1[e1]
            e1 = e1+1
        else:
            arr[i] = arr2[e2]
            e2 = e2+1
    return arr

def Button_UP_merge_Sort():
    print("not implemented yet")