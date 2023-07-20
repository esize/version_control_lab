from encode import encode


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        if option == 1:
            #  Encode
            encoded_password = ''
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
        elif option == 2:
            #  Decode
            break
        elif option == 3:
            #  Exit program
            break


if __name__ == '__main__':
    main()
