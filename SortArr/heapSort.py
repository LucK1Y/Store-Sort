def bubbleup(arr, node):
    if node == 0:
        return
    parent = (node-1)//2
    if arr[node] > arr[parent]:
        arr[node], arr[parent] = arr[parent], arr[node]
        bubbleup(arr, parent)


def bubbledown(arr, node, end):
    lci = 2*node+1
    if lci < end:
        gci = lci
        rci = lci+1
        if rci < end:
            if arr[rci] > arr[lci]:
                gci = rci
        if arr[gci] > arr[node]:
            arr[node], arr[gci] = arr[gci], arr[node]
            bubbledown(arr, gci, end)


def heapify(arr):
    end = len(arr)
    last = (end-1)//2
    for node in range(last, -1, -1):
        bubbledown(arr, node, end)

def heap_Sort(arr):
    last=len(arr)-1
    heapify(arr)
    for i in range(last,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        bubbledown(arr,0,i)
    return arr

