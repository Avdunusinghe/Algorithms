# function starts here
def genarate_numbers(_number):
    # base condition
    if _number == 1:
        return _number
    else:
        return genarate_numbers(_number - 1) * 2 + 1


# Termination loop starts here
while True:
    _number = int(input("Enter the number:"))

    if _number == -1:
        print("Finished")
        break

    print(genarate_numbers(_number))