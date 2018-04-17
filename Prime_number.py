# Find all Prime number between an interval like(10 to 50)

low = int(input("Enter the lower number : "))
high = int(input("Enter The upper range : "))

for num in range(low, high+1):
    if num > 1:
        for i in range(2, num):
                if (num % i) == 0:
                    break
        else:
                print(num)
