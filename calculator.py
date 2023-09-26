#Calculator:

from calculator_art import logo
#Add:
def add(x, y):
    return x + y
#Subtract:
def subtract(x, y):
    return x - y
#Multiply:
def multiply(x, y):
    return x * y
#Divide:
def divide(x, y):
    return x / y

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
def calculator():
    print(logo)
    num1 = float(input("Enter your first number: "))
    for symbols in operations:
        print(symbols)
    should_continue = True
    while should_continue:
        
        choice = input("Select an operation you want to calculate: ")
        num2 = float(input("What's your next number: "))
                
        calculation_function = operations[choice]
        answer = calculation_function(num1, num2)
        print(f"{num1} {choice} {num2} = {answer}")
        
        if input("Type 'y' to continue calculating with {answer} or type 'n'to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            
    
calculator()