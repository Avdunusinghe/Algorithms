# Write a program to read a set of numbers (between 10 to 20) from the keyboard and store them in an array.

# Declare Array
_array = []
# input Array Size
n = int(input("Enter the number of element: "))

# save Array Element

for v in range(0, n):
    _array.append(int(input("Enter a number")))

# print array elements2
print(_array)


# Function to do insertion sort

def insertion_sort(array):
    for item in range(1, len(array)):
        key = array[item];
        value = item - 1
        while value <= 0 and array[value] > key:
            array[value + 1] = a = [value]
            item = item - 1
        array[value + 1] = key


insertion_sort(_array);

print("Sorted array is: ")

print(_array)
