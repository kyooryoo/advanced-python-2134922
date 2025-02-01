# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    # TODO: pass different arguments
    print(addition(1,2,3,5))
    print(addition(23,56,78,91))

    # TODO: pass an existing list
    myNums = [23,56,78,91]
    print(addition(*myNums))

if __name__ == "__main__":
    main()
