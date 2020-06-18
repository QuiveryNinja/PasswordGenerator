import string, random

num = int(input("How long should your password be? it must be more than 6 characters long: "))

def generatePassword(num):
    password = ''

    if num < 6:
        print("That password is too short, it needs more than 6 characters")
        return
    for n in range(num):
        x = random.randrange(6, 94)
        password += string.printable[x]

    return password

print(generatePassword(num))