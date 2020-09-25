'''This program accept word from user and provides meaning from JSON file. Following scenarios covered with possible errors. 
- User mistakenly entered wrong spelling. Possible proximity word displayed on screen for user to confirm with Y/N
- Covered lowercase, uppercase, capital letter format of input
- User friendly messages displayed if word doesn't exist or user input is not valid. '''

import json
data = json.load(open("data.json"))

import difflib # nn
from difflib import get_close_matches

def returnval(key):
    key = key.lower()
    if (key in data):
        return data[key]
    elif (key.title() in data):
        key = key.title()
        return data[key]
    elif (key.upper() in data):
        key = key.upper()
        return data[key]
    elif len(get_close_matches(key, data.keys())) > 0:  # check count if entered values are invalid
        revised_val = get_close_matches(key, data.keys())[0]
        choice = input("do you mean to type:{}. if yes then type Y/N:".format(revised_val))
        if choice.lower() == 'y':
            return data[get_close_matches(key, data.keys())[0]]
        elif choice.lower() == 'n': 
            return "no matching record found. Please try entering other word next time"
        else:
            return "Valid values are Y/N so request is not processed" 
    else:
        return "no record exist"

val =  input ('Enter a word to get meaning:')
output = returnval(val)
if type (output) == list:
    for oneline in output:
        print (oneline)
else:
    print (output)