# Declare Array
_array = []
# input Array Size
n = int(input("Enter the number of element: "))

# save Array Element

for v in range(0, n):
    _array.append(int(input("Enter a number")))

# print array elements2
print(_array)


def partition(array, low, high):
    pivot = array[high]
    i = array[low] - 1

    for item in range(low, high):
        if array[item] <= pivot:
            i = i + 1
            array[i], array[item] = array[item], item[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 2


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


quicksort(_array, 0, n-1)
print(_array)


