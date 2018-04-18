# Multiplication of any number using While Loop
Table = int(input("Enter the Table name "))
Ran = int(input("Enter the range "))
num = True
num1 = 1
while num:
    if num1 > Ran:
        num = False
    else:
        print(Table, " x ", num1, " = ", (Table * num1))
        num1 += 1


# Multiplication table of a Number using For Loop
num = int(input("Show the multiplication table of? "))
Ran = int(input("Enter the range "))
for i in range(1, Ran):
            print(num, 'x', i, '=', num*i)
