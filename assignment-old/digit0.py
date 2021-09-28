def multiply(_number01, _number02):
    if _number01 == 1:
        return _number01
    else:
        return _number01 * multiply(_number01, _number02 - 1)


while True:
    n = int(input("Enter the number of element: "))
    m = int(input("Enter the number of element: "))

    if m == -1 or n == -1:
        break
        print(multiply(m, n))
