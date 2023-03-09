# This is the encode function.
def encode():
    pass


# Change
def func(x):
    print(x)


# This is the main function for the program.
def main():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise ValueError("Wrong number!")

    except ValueError as problem:
        print(problem)

    i_sum = 0
    for i in range(num):
        i_sum += 1


# This starts the program by calling the main function.
if __name__ == '__main__':
    main()
