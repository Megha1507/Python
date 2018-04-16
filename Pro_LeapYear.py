# Check if number is negative or positive
num1 = float(input("Enter the number : "))

if num1 < 0:
    print("Num1 is negative")
elif num1 > 0:
    print("Num1 is positive")
else:
    print("Zero")

# -----------------------------
# WAP to check leap year

x = float(input("Enter the Number: "))
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap year")
    else:
        print("Leap Year")
else:
    print("Yes it tis")

