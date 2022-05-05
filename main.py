
num1 = float(input('Enter your first number: '))
Operator = input('Enter operator: ')
num2 = float(input('Enter your second number: '))


if Operator == '+':
    print(num1 + num2)
elif Operator == '-':
    print(num1 - num2)
elif Operator == '/':
    print(num1 / num2)
elif Operator == '*':
    print(num1 * num2)


else:
    print('Not a valid operator')
