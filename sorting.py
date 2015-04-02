#!/usr/bin/env python3

def _swapInArray(array, i, j):
    array[i], array[j] = array[j], array[i]

def _heapify(array, count):
    start = int((count-2)/2)
    
    while start >= 0:
        _siftDown(array,start, count-1)
        start = start - 1
        
def _siftUp(array, start, end):
    child = end
    
    while child > start:
        parent = int((child-1)/2)
        if array[parent] < array[child]:
            _swapInArray(array, parent, child)
            child = parent
        else:
            return
            
            
def _siftDown(array, start, end):
    root = start
    
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        
        if child + 1 <= end and array[child] < array[child+1]:
            child = child + 1
            
        if array[root] < array[child]:
            _swapInArray(array, root, child)
            root = child
        else:
            return
            
    return
    
    # not working
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap = root
        
        if array[swap] < array[child]:
            swap = child
        
        if child + 1 <= end and array[swap] < array[swap+1]:
            swap = child + 1
            
        if swap == root:
            return
        else:
            _swapInArray(array, root, swap)
            root = swap
            

def heapSort(array):
    _heapify(array, len(array))
    
    end = len(array) - 1
    while end > 0:
        _swapInArray(array, end, 0)
        end = end - 1
        _siftDown(array, 0, end)
        print(array)
        
    
def heapPrint(heap):
    i = 0
    for i in range(int(len(heap)/2)):
        try:
            print("{}: ".format(heap[i]), end="")
            print("{}".format(heap[i*2+1]), end="")
            print(" x {}".format(heap[i*2+2]),end="")
            print("") #newline
        except IndexError:
            print("") #newline
            return


def _merge(left, right):
    array = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i = i + 1
        else:
            array.append(right[j])
            j = j + 1
            
    array.extend(left[i:])
    array.extend(right[j:])
    
    return array


def mergeSort(array):
    left = []
    right = []
    middle = int(len(array)/2)
    
    if len(array) == 1:
        return array
        
    left = array[:middle]
    right = array[middle:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    return _merge(left, right)
    

if __name__ == "__main__":
    array = [5,6,7,1,1,2,3,8,8,9,4,10,14,12,13,11]
    #array = mergeSort(array)
    #print(array)
    #heapify(array)
    
    #array = [3, 1, 2, 1]
    print(array)
    heapSort(array)
    print(array)
    