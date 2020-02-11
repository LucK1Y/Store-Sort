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