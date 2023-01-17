import random
import re

# characters for the passwords and the strength checker
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*().,/;'
special_chars = '!@#$%^&*().,/;'
numbers = '1234567890'

# defines the password function
def password(number, length):
    
    # sets the amount of passwords wanted and the length of the passwords
    number_pass = int(number)
    length_pass = int(length)

    print('\nhere are your passwords!')

    # generates a random password or passwords with a random length that the user applies
    for pwd in range(number_pass):
        passwords = ''
        for c in range(length_pass):
            passwords += random.choice(chars)
        print(passwords)

    # checks the strength of the password
    def strength():
       
       # (only checks the strength of the password if there is only one password)
       if number_pass >= 2:
            return
       else:
            # checks to see if length of password is more than or equal to 12
            if len(passwords) >= 12:
                strength_l = 2.5
            else:
                strength_l = 0

            # checks to see if password contains special characters
            if any(c in special_chars for c in passwords):
                strength_sc = 2.5
            else:
                strength_sc = 0

            # checks for numbers in the password
            if any(c in numbers for c in passwords):
                strength_num = 2.5
            else:
                strength_num = 0

            # checks for uppercase characters in the password
            uppercase = re.search('[A-Z]', passwords)
            if(uppercase is None):
                strength_u = 0
            else:
                strength_u = 2.5

            avg_strength = (strength_l + strength_sc + strength_num + strength_u)
    
            print('the strength of your password is: ' + str(avg_strength) + '/10')

    strength()

password(1, 12)