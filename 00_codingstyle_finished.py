# imports go on their own lines
import sys
import os


# two blank lines separate classes from other functions
class MyClass():
    """ a placeholder for construction method"""
    def __init__(self):
        self.prop1 = "my class"

    # within classes, one blank line separates methods
    def method1(self, arg1):
        """ a placeholder for a method in class """


def main():
    """ Long comments, like this one that flow across several lines, 
    are limited to 72 characters instead of 79 for lines of code"""
    cls1 = MyClass()
    print(cls1.prop1)
    cls1.prop1 = "hello world"
    print(cls1.prop1)

    print(os.environ["HOMEPATH"])
    print(sys.argv)


if __name__ == "__main__":
    main()
