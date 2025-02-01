# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def clearFunction(arg1, arg2, *, SuppressExceptions=False):
    print(f"received arg1={arg1}, arg2={arg2}, \
and SuppressExceptions={SuppressExceptions}")

def unclearFunction(arg1, arg2, SuppressExceptions=False):
    print(f"received arg1={arg1}, arg2={arg2}, \
and SuppressExceptions={SuppressExceptions}")

def main():
    # try to call the function without the keyword
    clearFunction(1, 2, SuppressExceptions=True)
    unclearFunction(1, 2, True)


if __name__ == "__main__":
    main()
