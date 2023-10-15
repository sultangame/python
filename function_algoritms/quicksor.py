from functools import reduce


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
b = [10, 5, 2, 4]   
b2 = [i * 3 for i in b]

# c = reduce((lambda x, y: x * y), b)

print(quicksort(b2))