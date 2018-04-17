# -------------------------------------------------------
# Check if number is Odd or Even

x = float(input("Enter the Number: "))
if x % 2 == 0:
    print("Number is even")
else:
    print("Number is Odd")
# --------------------------------------------------
# To check Prime numbers
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
