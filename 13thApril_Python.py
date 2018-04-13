class MyClass:

    "This is a Python Program"

    a = 50


def func():
    print('Hello Java')


print(MyClass.a)
print(MyClass.__doc__)

""".......................Program for Area of Triangle........................"""
# __doc__ attribute. It is used to fetch the docstring of that class.


def triangle():

    print("\nTo find Area of the Triangle:-")
    base = float(input("Please enter value of the BASE : "))
    height = float(input("Please enter value of the HEIGHT : "))
    print("area ", ((1 / 2) * base * height))
    again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    if calc_again.upper() == 'Y':
        triangle()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


triangle()

