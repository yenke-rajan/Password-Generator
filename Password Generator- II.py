#For generating password

import string
import random
from csv import writer #For writing and reading data from CSV file

def passgen():
    s1=string.ascii_lowercase #For Lowercase letters
    s2=string.ascii_uppercase #For Uppercase letters
    s3=string.digits #For digits
    s4=string.punctuation #For special characters
    platform=input("Enter The Name Of The Platform: ")
    length=int(input("\nEnter Length Of Password: ")) #Taking length of password user wants

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

    #Creating two columns Plaform and Password
    passdata=[platform,password]
    with open('pass.csv','a') as f: #Open CSV file and write the data into this file
        writedata=writer(f)
        writedata.writerow(passdata)

passgen()