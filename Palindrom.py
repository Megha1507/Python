num = input("Enter any number: ")
rev_num = reversed(num)
# check if the string is equal to its reverse
if list(num) == list(rev_num):
    print(num, " is a Palindrome number")
else:
    print(num, " is not Palindrome number")