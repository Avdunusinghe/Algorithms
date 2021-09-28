def sum(_number):
    if _number == 1:
        return 1
    else:
        return sum(_number-1)+_number


while True:
    n = int(input("Enter the number: "))

    if n == -1:
        break

    print(sum(n))