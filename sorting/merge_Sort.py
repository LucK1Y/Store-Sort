


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
