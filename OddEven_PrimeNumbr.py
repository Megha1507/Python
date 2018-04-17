# -------------------------------------------------------
# Check if number is Odd or Even

x = float(input("Enter the Number: "))
if x % 2 == 0:
    print("Number is even")
else:
    print("Number is Odd")
# --------------------------------------------------
# number = input("Enter the number:")
number = 11
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("It is not an Prime Number")
            print(i, "times", number // i, "is", number)
            break
        else:
            print("Its a Prime Number")
else:
    print

