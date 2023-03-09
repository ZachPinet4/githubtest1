# This is the encode function.
def encode(password):
    encoded_password = ''
    for x in str(password):
        x = int(x)
        x += 3
        encoded_password += str(x)

    print("Your password has been encoded and stored!")
    return int(encoded_password)


# This is the decode function.
def decode(encoded_password):
    pass


# This is the main function for the program.
def main():
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")

        menu_option = int(input("Please enter an option: "))
        encoded_password = ''

        if menu_option == 1:
            password = int(input("Please enter your password to encode: "))
            encoded_password = encode(password)
        elif menu_option == 2:
            password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}".)
        else:
            break


# This starts the program by calling the main function.
if __name__ == '__main__':
    main()
