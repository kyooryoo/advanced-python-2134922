# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """ 
    myFunction(arg1, arg2=None) --> Doesn't really do anything, just print.

    Parameters:
    arg1: the first argument. What you want to pass and print.
    arg2: second argument to print. Default to None.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
