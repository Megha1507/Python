# Fibonacci series will start at 0 and travel upto below number
Number = int(input("\nPlease Enter the Range Number: "))

# Initializing First and Second Values of a Series
First_Value = 0
Second_Value = 1

# Find & Displaying Fibonacci series using For loop
for Num in range(0, Number):
    if Num <= 1:
        Next = Num
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    print(Next)
# =======================

# Fibonacci series will start at 0 and travel upto below number
Number = int(input("\nPlease Enter the Range Number: "))

# Initializing First and Second Values of a Series
i = 0
First_Value = 0
Second_Value = 1

# Find & Displaying Fibonacci series using while loop

while i < Number:
    if i <= 1:
        Next = i
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    print(Next)
    i = i + 1






