#  Evan Sizemore
def encode(password):
    encoded_str = ''
    for char in password:
        encoded_str += str((int(char) + 3))

    return encoded_str
