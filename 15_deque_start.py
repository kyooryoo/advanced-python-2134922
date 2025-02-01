# deque objects are like double-ended queues
# it has memory efficient for operations on both ends

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # TODO: deques support the len() function
    print(f"item count: {str(len(d))}")

    # TODO: deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # TODO: manipulate items from either end
    print()
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    # TODO: rotate the deque
    d.rotate(5)
    print(d)
    d.rotate(-10)
    print(d)


if __name__ == "__main__":
    main()
