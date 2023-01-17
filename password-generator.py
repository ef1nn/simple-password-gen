import random
import re

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*().,/;'
special_chars = '!@#$%^&*().,/;'
numbers = '1234567890'


def password(number, length):
    number_pass = int(number)
    length_pass = int(length)

    print('\nhere are your passwords!')

    for pwd in range(number_pass):
        passwords = ''
        for c in range(length_pass):
            passwords += random.choice(chars)
        print(passwords)

    
    def strength():
       
        #checks to see if length of password is more than or equal to 12
        if len(passwords) >= 12:
            strength_l = 2.5
        else:
            strength_l = 0

        #checks to see if password contains special characters
        if any(c in special_chars for c in passwords):
            strength_sc = 2.5
        else:
            strength_sc = 0

        if any(c in numbers for c in passwords):
            strength_num = 2.5
        else:
            strength_num = 0

        #checks for uppercase characters in password
        uppercase = re.search('[A-Z]', passwords)
        if(uppercase is None):
            strength_u = 0
        else:
            strength_u = 2.5

        avg_strength = (strength_l + strength_sc + strength_num + strength_u)
    
        print('the strength of your password is: ' + str(avg_strength) + '/10')

    strength()

password(1, 12)