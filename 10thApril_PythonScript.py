# Spliting the words
print("Hello:Everyone".split(":"))

print("Hello:World:again".split(":"))

# Selecting and printing the value
print("Lets do the " + "Hello:World:Program".split(":")[0])

# Printing only the letter
print("Lets do the " + "Hello:World:Program".split(":")[0][1])

"""------------------------BOOLEAN OPERATORS---------------------------"""

print(5 == 5)
print(5 is not 5)
print("True" is "True")
print("True" is str(False))

"""------------------------Arrays---------------------------"""

v = ["Movies", "Games", "Dance"]
print(v[1])

print({"name": "Megha", "age": "27"}['name'])

x = 10
y = 2
print(x*y+y-x)


print(int("5"))
print(float("2.6"))
print(bool("True"))

#  counting length of the word "Hell"
print(len("HELL"))

# counting length of the variables in the function
print(len([1, 2, 3, 4]))

# Here "len" function counts the number of Item
print(len(["Hello", "Nick"]))

# Number sorting
print(sorted([2, 0, 23, 19, 8, 3]))

# String sort
print(sorted(["X", "U", "D", "R", "i", "a", "2", "1", "2.3"]))


# creating function and passing arguments
# def <functionname()>
def my_world(str1, str2):
    print(str1)
    print(str2)


my_world("my", "world")


# passing values(string and integer) to the arguments
def my_details(name, age):
    print("My name is ", name, " and I am ", age, "years old")


my_details("Nicky", 27)


# Function with default arguments
def my_details(name="xyz", age="22"):
    print("My name is ", name, " and I am ", age, "years old")


my_details()
my_details("Abc")
my_details(None, "22")
my_details(age="23")
my_details(name="Megha", age="27")
my_details(age="23")


# Passing infinite numbers to the arguments. * is used to define ALL
def p_details(*all):
    for item in all:
        print("This is ", item)


p_details("abc", "ABC", "DEF", "XSV")


# Passing all numbers to the arguments. * is used to define ALL
def p_details(*all):
    for item in all:
        print("This is ", *all)


p_details("abc", "ABC", "DEF", "XSV")


# returning a value in a function
def do(num1, num2):
    return num1 + num2


math1 = do(10, 2)
math2 = do(12, 20)


print("First sum result ", math1, "Second sum result is ", math2)


# If else statements in Python
check = True
if check == False:
    print("This is False")
elif check == "Hammer":
    print("Hammer is True")
else:
    print("This is True")

""".........For and while Loop........."""

# Listing the values by using FOR loop
numbers=[1,2,3,4,5]

for item in numbers:
    print(item)

# Printing numbers by using While Loop
run = True
current = 91

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1
