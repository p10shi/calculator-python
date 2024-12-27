def calculadora():
    print('Operations list.')
    print("----------------")
    print('1. Multiplication.')
    print('2. Addition.')
    print('3. Subtraction.')
    print('4. Division.')
    print('5. Power.')

def mult(x,y):
    print(f'{x} * {y} = {x * y}')
    return x * y

def sum(x,y):
    print(f'{x} + {y} = {x + y}')
    return x + y

def sub(x,y):
    print(f'{x} - {y} = {x - y}')
    return x - y

def div(x,y):
    if y == 0:
        print('Division by zero is not allowed.')
        return 'Error'
    print(f'{x} / {y} = {x / y}')
    return x / y

def pow(x,y):
    print(f'{x} ** {y} = {x ** y}')
    return x ** y

if __name__ == '__main__':

    firstRun = True

    while True:
        firstRun = False
        calculadora()
        
        operation = input('Please, enter 1, 2, 3, 4 or 5 to choose the operation: ')

        if operation not in ['1', '2', '3', '4', '5']:
            print('Invalid operation. Try again.')
            continue
    
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))

        if operation == '1':
            mult(num1, num2)
        elif operation == '2':
            sum(num1, num2)
        elif operation == '3':
            sub(num1, num2)
        elif operation == '4':
            div(num1, num2)
        elif operation == '5':
            pow(num1, num2)

        nextOperation = input('Do you want to do another operation? (yes/no) ')
        if nextOperation.lower() != 'yes':
            print('Thank you for using the calculator')
            break