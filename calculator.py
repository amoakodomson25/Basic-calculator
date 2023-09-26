def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        return "Cannot divde by 0"
    return x / y


def multiply(x, y):
    return x * y


_operations = {"a": add, "s": subtract, "d": divide, "m": multiply}


def main():
    while True:
        print("************************************")
        print("**        Basic Calculator        **")
        print("************************************")
        print(" ")
        print("Options: ")
        print(" 'a' to add")
        print(" 's' to subtract")
        print(" 'd' to divide")
        print(" 'm' to multiply")
        print(" 'q' to close the program")

        input_user = input("... ")

        if input_user == "q":
            break
        elif input_user in _operations:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("")
            operation = _operations[input_user]
            result = operation(num1, num2)
            print("Result: ", result)
            print(" ")
            print(" ")
        else:
            print("Invalid Input")


main()
