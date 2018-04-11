def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)
    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)
    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)
    again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


calculate()







