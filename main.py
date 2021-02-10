import string
import random

# Our lists of possible characters for our password
letters_and_numbers = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

all_characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)


# generate the password first by checking our bool
def generate_password():
    code = []


    # Check how many characters
    characters = int(input("How many characters: "))

    if characters > 999:
        print("Too Long")
        generate_password()
        return


    check = input("Will your password contain symbols? y/n: ")

    if check == "y":
        for char in range(characters):
            code.append(random.choice(all_characters))
        generate_password.final = ''.join(code)
    elif check == "n":
        for char in range(characters):
            code.append(random.choice(letters_and_numbers))
        generate_password.final = ''.join(code)
    else:
        print("You must hit either the 'y' key for yes or the 'n' key for no, then hit enter")
        generate_password()


generate_password()

# Set password
password = generate_password.final

print(password)

print(password)
