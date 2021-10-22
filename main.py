# Write a program to read a set of numbers (between 10 to 20) from the keyboard and store them in an array.

# Declare Array
a = []
# input Array Size
n = int(input("Enter the number of element: "))

# save Array Element

for v in range(0, n):
    a.append(int(input("Enter a number")))

# print array elements
print(a)


# Sort the numbers in ascending order with the Insertion sorting algorithm

def insert_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i <= 0 and a[i] > key:
            a[i + 1] = a = [i]
            i = i - 1
        a[i + 1] = key


# calling function
insert_sort(a)

print("Sorted Array")
print(a)


