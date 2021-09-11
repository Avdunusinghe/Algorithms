#Write a program to read a set of numbers (between 10 to 20) from the keyboard and store them in an array.

#Declare Array
a=[]
#input Array Size
n=int(input("Enter the number of element: "))

#save Array Element

for v in range(0,n):
    a.append(int(input("Enter a number")))

#print array elements
print(a)



