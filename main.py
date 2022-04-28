#Calculator
#logo
from art import logo
#Add
def add(n1, n2):
    return n1 + n2
#Substract
def substract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2
#operations dictionary
operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
} 
#recursion function to do the calculator
def calculator():
    #logo
    print(logo)
    #input number 1
    num1 = float(input("What is the first number?"))
    #for loop to print operations
    for symbol in operations:
        print (symbol)
    #create a loop to run calculations as long as we type 'y'    
    exit = False
    while exit is False:    
        #variable input to chose the operatipn    
        operation_symbol = input("Pick an operation from the line above: ")
        #input next number
        num2 = float(input("What is the next number?"))
        #find the answer based on the operation_symbol input and the dictionary
        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)
        #print the answer
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        #if input where we choose if we keep the loop running 
        if input(f"Type 'y' to continue calculating with {first_answer}, or type  'n' to exit: ") == "y": 
            num1 = first_answer
        else:
            exit = True
            calculator()
calculator()

#variable input to chose another operation    
#operation_symbol = input("Pick another operation: ")
#input number 3
#num3 = int(input("What is the next number?"))
#find the next answer based on the operation_symbol input and the dictionary
#calculation_function = operations[operation_symbol]
#second_answer = calculation_function(first_answer, num3)
#print the next answer
#print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
