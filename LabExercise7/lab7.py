# Declare Array
_array = []
# input Array Size
n = int(input("Enter the number of element: "))

# save Array Element

for v in range(0, n):
    _array.append(int(input("Enter a number")))

# print array elements2
print(_array)


# implementation of bubblesort
def bubble_sort(a):
    n = len(a)
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]


# call the bubble sort
bubble_sort(_array)

print('sorted array:')

print(a)
