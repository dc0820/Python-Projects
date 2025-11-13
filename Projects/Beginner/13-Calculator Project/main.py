import art



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def modular(n1, n2):
    return n1 % n2

operations = { "+" : add,
               "-" : subtract,
               "*" : multiply,
               "/" : divide,
               "%" : modular
}


def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("What is the first number: "))
    while should_continue:
        for operator in operations:
            print(operator)

        symbol = input("what is the operation: ")
        num2 = float(input("What is the second number: "))
        answer = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = answer
        else:
            print("\n" * 20)
            calculator()

calculator()