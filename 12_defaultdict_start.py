# Demonstrate the usage of defaultdict objects

from collections import defaultdict

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruit_counter = {}
    # use the default dictionary
    fruit_counter_x = defaultdict(int)

    # Count the elements in the list
    for fruit in fruits:
        if fruit in fruit_counter:
            fruit_counter[fruit] += 1
        else:
            fruit_counter[fruit] = 1
    # Save the effert to initialize a dictionary
    for fruit in fruits:
        fruit_counter_x[fruit] += 1

    # print the result
    for (k, v) in fruit_counter.items():
        print(k + ": " + str(v))
    # the results are the same
    for (k, v) in fruit_counter_x.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
