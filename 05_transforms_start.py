# use transform functions like sorted, filter, map


def filterFunc1(x):
    return x % 2 != 0


def filterFunc2(x):
    return x.islower()


def squareFunc(x):
    return x**2


def toGrade(x):
    if x > 90:
        return 'A'
    elif x > 80:
        return 'B'
    elif x > 70:
        return 'C'
    elif x > 60:
        return 'D'
    else:
        return 'F'


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    odds = list(filter(filterFunc1, nums))
    print(f"the odds in nums are: {odds}")

    # TODO: use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(f"the lower chars are: {lowers}")

    # TODO: use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(f"squares of nums: {squares}")

    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(f"grades in letters: {letters}")


if __name__ == "__main__":
    main()
