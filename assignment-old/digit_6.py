def sumcube(n):
    if n == 1:
        return 1
    else:
        return sumcube(n - 1) + n * n * n


while True:
    n = int(input("input number"))

    if n == -1:
        break
    else:
        print(sumcube(n))
