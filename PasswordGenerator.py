# -*- coding: utf-8 -*-
"""
@author: Mohamed
"""

import string
import random

# Initialize the variables needed to create the password
validInput = ['yes', 'no', 'y', 'n']
characterTypes = {'digits': string.digits, 'lowercase': string.ascii_lowercase, 'uppercase': string.ascii_uppercase, 'special': string.punctuation}
passwordList = []

def createPassword():
    # Initialize password and password length
    length = 0
    password = []
    
    # Obtain length of password
    while True:
        try:
            length = int(input("How long should your password be? "))
            
            if length < 4:
                print("Password length must be at least 4")
                continue
            break
        except ValueError:
            print("Please enter a numer")

    # Obtain types of charaters to include
    for type in characterTypes:
        addCharacters = getCharacteristic(type)
        if addCharacters:
            passwordList.extend(characterTypes[type])

    for i in range(length):
        x = random.choice(passwordList)
        password.append(x)
        
    print(''.join(password))
         
    

def getCharacteristic(x):
        characteristic = str(x)
        while True:
            value = input(f"Should your password contain {characteristic} characters? Yes or No \n")
            if value.lower() not in validInput:
                print("Please enter yes or no")
            else:
                if value.lower() == 'yes' or value.lower() == 'y':
                    return True
                else:
                    return False
        
        
        
createPassword()
