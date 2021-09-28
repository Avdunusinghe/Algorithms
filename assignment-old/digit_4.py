def fibnacci(n):
    if n <= 1:
        return n
    else:
        return (fibnacci(n - 1) + fibnacci(n - 2))


while True:

    n = int(input("Enter the number of element: "))

    if n == -1:
        break

    else:
        print(fibnacci(n))