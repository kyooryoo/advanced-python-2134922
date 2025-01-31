# demonstrate built-in utility functions


def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]
    
    # TODO: any will return true if any of the sequence values are true
    print(f"any item in {list1[:4]} is true: {any(list1[:4])}")
    print(f"any item in {list1[3:4]} segment is true: {any(list1[3:4])}")
    
    # TODO: all will return true only if all values are true
    print(f"all items in {list1} are true: {all(list1)}")
    print(f"all items in {list1[:3]} are true: {all(list1[:3])}")
    
    # TODO: min and max will return minimum and maximum values in a sequence
    print("min:", min(list1))
    print("max:", max(list1))
    
    # TODO: Use sum() to sum up all of the values in a sequence
    print("sum:", sum(list1))
    
if __name__ == "__main__":
    main()
    