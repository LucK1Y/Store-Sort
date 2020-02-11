def selection_Sort(arr):
    arrlen = len(arr)
    for i in range(arrlen-1):
        min_i = i
        for j in range(i+1, arrlen):
            if arr[j] < arr[min_i]:
                min_i = j

        arr[min_i], arr[i] = arr[i], arr[min_i]
    return arr
