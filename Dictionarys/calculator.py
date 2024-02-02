logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add(n1, n2):
    """Takes in two numbers and returns the sum"""
    return n1 + n2


def subtract(n1, n2):
    """Takes in two numbers and returns the difference"""
    return n1 - n2


def multiply(n1, n2):
    """"Takes in two numbers and returns the product"""
    return n1 * n2


def divide(n1, n2):
    """Takes in two numbers and returns the quotient"""
    return n1 / n2


def power(n1, n2):
    """Takes in two numbers and returns n1 to the power of n2"""
    return n1 ** n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power
}

cont_calculation = "y"


def calculator():
    global cont_calculation

    num1 = int(input("Enter a number: "))
    for key in operations:
        print(key)
    operation = input("Pick an operation: ")
    num2 = int(input("Enter a second number:"))
    ans = 0
    for key in operations:
        if key == operation:
            ans = operations[operation](num1, num2)

    print(f"{num1} {operation} {num2} = {ans}")

    cont_calculation = input(
        f"Do you want to continue calculating with {ans}, 'n' to stop, y to continue or c to start a new calculation: ")

    while cont_calculation.lower() == "y":
        num1 = int(input("Enter a number: "))
        for key in operations:
            print(key)
        operation = input("Pick an operation: ")
        num2 = ans
        for key in operations:
            if key == operation:
                ans = operations[operation](num2, num1)

        print(f"{num1} {operation} {num2} = {ans}")

        cont_calculation = input(
            f"Do you want to continue calculating with {ans}, 'n' to stop, y to continue or c to start a new calculation: ")
    if cont_calculation == "c":
        calculator()
    else:
        return


calculator()
