#For generating password

import string
import random

def passgen():
    s1=string.ascii_lowercase #For Lowercase letters
    s2=string.ascii_uppercase #For Uppercase letters
    s3=string.digits #For digits
    s4=string.punctuation #For special characters
    length=int(input("Enter Length Of Password: ")) #Taking length of password user wants

    #Taking all the uppercase, lowercase, digits, special symbols as list
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4)) 

    random.shuffle(s) #Shuffles list in random order

    password=("".join(s[0:length])) 
    #Join joins all the character in the password

    print(password)

passgen()