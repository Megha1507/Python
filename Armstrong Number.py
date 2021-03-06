"""A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3."""

# to check 3 digit number only
num = str(input("Enter a number: "))
p1 = num[0]
p2 = num[1]
p3 = num[2]

num1 = ((int(p1)**3) + (int(p2)**3) + (int(p3)**3))
num1 = str(num1)
if num == num1:
    print(num)
    print(num1, " is Armstrong number ")
else:
    print(num1, " is not Armstrong number ")

# 5 ** 2 = 25 (5 to the power of 2)
# 3//2 = 1 ( but actual is 1.5) rounds down the answer to the nearest whole number)

# To check any number for Armstrong number
n = int(input("Enter the number: "))
c = 0
temp = n

while n < 0:
    a = n % 10
    n = n/10
    c = c + (a**3)
if temp == n:
    print(n, " is Armstrong number")
else:
    print(n, "is not an Armstrong Number")



