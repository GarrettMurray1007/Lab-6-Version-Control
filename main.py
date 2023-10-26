#Garrett Murray

def encode(pw):
    encode = []
    for char in pw:
        encode.append(str(int(char) + 3))
    encoded = "".join(encode)
    return encoded

def decode(encoded_pw):
    pass

run = True
menu = """Menu
-------------
1. Encode
2. Decode
3. Quit"""
while run:
    print(menu)
    option = int(input("Please enter an option: "))
    if option == 1:
        encoded_pw = encode(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!")
    elif option == 2:
        decoded_pw = decode(encoded_pw)
        print(f"The encoded password is {encoded_pw}, and the original password is {decoded_pw}.")
    elif option == 3:
        run = False
