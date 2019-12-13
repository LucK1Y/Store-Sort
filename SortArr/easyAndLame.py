
def selection_Sort(arr):
    arrlen = len(arr)
    for i in range(arrlen-1):
        min_i = i
        for j in range(i+1, arrlen):
            if arr[j] < arr[min_i]:
                min_i = j

        arr[min_i], arr[i] = arr[i], arr[min_i]
    return arr


def insertion_Sort(arr):
    arrlen = len(arr)

    for i in range(1, arrlen):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j-1
    return arr


