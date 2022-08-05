# -*- coding: utf-8 -*-
"""
@author: Mohamed
"""

import string
import PySimpleGUI as sg
import random

# Initialize the lists
validInput = ['yes', 'no', 'y', 'n']
characterTypes = {'digits': string.digits, 'lowercase': string.ascii_lowercase, 'uppercase': string.ascii_uppercase, 'special': string.punctuation}
passwordList = []



# Setting the application GUI up
sg.theme('SystemDefault1')

options = [[sg.Text("Password Generator")],      
          # This could be improved by using a for loop
          [sg.Text("How long should your password be?")],
          [sg.Text("Include lowercase characters?: ")],
          [sg.Text("Include uppercase characters?: ")],
          [sg.Text("Include numbers?: ")],
          [sg.Text("Include special characters?: ")],
          [sg.Button('Generate')]]

answers = [[sg.Input(default_text='8', size=(5, 2), enable_events=True, key='length')],
           [sg.Checkbox('e.g.: abcdefg', default=True, key='lowercase')],
          [sg.Checkbox('e.g.: ABCDEFG', default=False, key='uppercase')],
          [sg.Checkbox('e.g.: 123456', default=False, key ='digits')],
          [ sg.Checkbox('e.g.: !"£$%.>', default=False, key='special')]
    ]

layout = [
    [sg.Column(options),
     sg.Column(answers),]
]
window = sg.Window('password generator', layout)

def createPassword(length, lowercase, uppercase, digits, special):
    # Initialize password list
    password = []
    
    for type in characterTypes:
        if type:
            strtype = str(type)
            password.extend(random.choice(characterTypes[strtype]))
            passwordList.extend(characterTypes[strtype])
            length -= 1
            
    for i in range(length):
        x = random.choice(passwordList)
        password.append(x)

    
    random.shuffle(password)
    return ''.join(password)
         
    


# The main application
while True:                             # To run the application indefinitely or until the game is closed

    #Initialize the window
    event, values = window.read()   

    # Close the game
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    # Ensure the user only enters digits and less than 99
    if event == 'length' and values['length'] and values['length'][-1] not in ('0123456789') or len(values['length']) > 2:
        window['length'].update(values['length'][:-1])
        window['Generate'].update(disabled=True)
    if event == 'length' and values['length'] == '' or values['length'][-1] not in ('01234556789'):
        window['Generate'].update(disabled=True)
    else:
        window['Generate'].update(disabled=False)
    # Ensure the user only enters numbers are entered in length
        
    if event == 'Generate':
        if int(values['length']) < 4:
            window['length'].update(values['length'][:-1])
            sg.popup('Length must be longer than 4')
            continue
        
        length = int(values["length"])
        lowercase = values["lowercase"]
        uppercase = values["uppercase"]
        digits = values["digits"]
        special = values["special"]
        password = createPassword(length, lowercase, uppercase, digits, special)
        sg.popup('Your password is: ', password)
    

window.close()


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
        