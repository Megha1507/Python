"""Write a program to print a String using class and methods"""


class MyClass:

    def method1(self):
        print("Method1 no arguments")

    def method2(self, somestring):
        print("Software Testing:" + somestring)


def main(self):
        c = MyClass()
        c.method1()
        c.method2(" Testing is fun")


if __name__ == "__main__":
    main(self=object)


"""
Notes
1. Class names should use CamelCase convention
2. Method name should be lowercase.
3. Self
    -> refer to the specific instance of this object    
"""