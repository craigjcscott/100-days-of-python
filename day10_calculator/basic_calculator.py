import os
import art

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

operations_dict = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculator():
    os.system('clear')
    print(art.logo)
    calc_running = True

    num1 = float(input('What is the first number? '))


    while calc_running:
        oper = input(f'What is the operation? Chose from ' + str(list(operations_dict.keys())) + ': ')
        num2 = float(input('What is the next number? '))
            
        function = operations_dict[oper]
        solution = function(num1, num2)
        
        print(f'{num1} {oper} {num2} = {solution}')
        
        if input(f'Perform another operation using {solution}? Y/N: ').lower() == 'y':
            num1 = solution
        else:
            calculator()

calculator()
            