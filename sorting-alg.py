from random import randint

def randomize(arr):
    res = []
    while len(arr) > 0:
        ind = randint(0, len(arr)-1)
        res.append(arr[ind])
        arr.pop(ind)
    return res

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def bubble_sort(array):
    arr = array[:] # Copy of the list
    n   = len(arr)-1  
    for i in range(n): 
        for j in range(0, n-i): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

def insertion_sort(array):
    arr = array[:]
    n   = len(arr)
    for i in range(1, n):
        val = arr[i]
        j = i-1
        while j >=0 and val < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = val
    return arr

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    less, equal, greater = [], [pivot], []
    for num in arr[0:-1]:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    return quick_sort(less) + equal + quick_sort(greater)

def test_algs():
    algs = {
        'bubble_sort': None, 
        'insertion_sort': None,
        'quick_sort': None
    }
    arr = randomize(list(range(1000)))
    algs['bubble_sort'] = is_sorted(bubble_sort(arr))
    
    arr = randomize(list(range(1000)))
    algs['insertion_sort'] = is_sorted(insertion_sort(arr))

    arr = randomize(list(range(1000)))
    algs['quick_sort'] = is_sorted(quick_sort(arr))
    
    return algs

print(test_algs())