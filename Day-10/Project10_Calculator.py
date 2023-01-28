from Project10_art import logo
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations={
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1=int(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue=True
    while should_continue:
        operation_symbol=input("Pick an operation: ")
        num2 = int(input("What's the next number? "))
        calculation=operations[operation_symbol]
        result=calculation(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")
        continue_calculation= input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
        if continue_calculation=='y':
            num1=result
        else:
            should_continue==False
            # Recursion-Calling the function in itself,here it'll take the new input from the beginning.
            calculator()

calculator()