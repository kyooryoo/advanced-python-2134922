# Demonstrate the usage of Counter objects

from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # TODO: Create a Counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)

    # TODO: How many students in class 1 named James?
    print(f"there are {c1['James']} James in class 1")

    # TODO: How many students are in class 1?
    print(f"there are {sum(c1.values())} students in class 1")

    # TODO: Combine the two classes
    c1.update(class2)
    print(f"there are {sum(c1.values())} students in class 1 after adding class 2")

    # TODO: What's the most common name in the two classes?
    print(f"the most common names in class 1 are {c1.most_common(3)}")

    # TODO: Separate the classes again
    c1.subtract(class2)
    print(f"the most common names in class 1 after substracting class 2: {c1.most_common(3)}")

    # TODO: What's common between the two classes?
    print(f"the names in both classes are {c1 & c2}")


if __name__ == "__main__":
    main()
