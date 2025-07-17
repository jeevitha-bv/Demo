a = int(input('Enter num1: '))
b = int(input('Enter num2: '))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print(f'The sum is {add(a, b)}')
print(f'The difference is {subtract(a, b)}')
print(f'The product is {multiply(a, b)}')
print(f'The quotient is {divide(a, b)}')
