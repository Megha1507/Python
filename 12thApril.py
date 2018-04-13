"""-------------------Strings Operators---------------------"""
# Operator[] > Printing the letter from the given index
x="Guru"
print("Printing letter only:", x[1])

# Operator [ : ] > To print characters from the range of strings
x="Guru"
print(x[0:4])

# Operator "in" > Membership-returns true if a letter exist in the given string
x = "Guru"
print("G" in x)

# Operator "not in" > Membership-returns true if a letter exist is not in the given string
x="Guru"
print("l" not in x)

# Operator "r/R"
print(R'\n')
print(r"\n")

# Operator % - Used for string format
name = 'guru'
number = 99
print('%s %d' % (name, number ))

# Operator * > Repeat and Prints the character twice
x = "Guru"
y = "99"
print(x * 2)


# # "join" function for the string. String Reversing
string="12345"
print(''.join(reversed(string)))
print(":".join("Python"))
