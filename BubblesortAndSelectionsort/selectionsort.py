# Declare Array
_array = []
# input Array Size
n = int(input("Enter the number of element: "))

# save Array Element

for v in range(0, n):
    _array.append(int(input("Enter a number")))

# print array elements2
print(_array)


def selection_sort(array):
    n = len(array)
    for j in range(0, n - 1):
        smallest = j
        for i in range(j + 1, n):
            if array[i] < array[smallest]:
                smallest = i
            array[j], array[smallest] = array[smallest], array[j]


# call the selectionsort

selection_sort(_array)
print("Sorted array:")
print(_array)
