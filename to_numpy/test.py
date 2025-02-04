# import re

# li = 'Рас, раса, матрас,90 2 22 3 33растование'

# math = re.findall(r']\d',li)

# print(math)

def check_greeting(message):
    greetings = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    message = message.lower()  # Convert the message to lowercase to make the check case-insensitive
    for greeting in greetings:
        if greeting in message:
            return True
    return False

def validate_hello(message):
    greetings = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    message = message.lower()  # Преобразуем в нижний регистр для независимости от регистра
    for greeting in greetings:
        if greeting in message:
            return True
    return False



def validate_hello(greetings):
    greetings = greetings.lower() 
    if 'hello' or'ciao' or 'salut' or 'hallo' or 'hola' or 'ahoj' or 'czesc ' in greetings:
        return True
    return False 


def validate_hello(greetings):
    greetings = greetings.lower() 
    return True if 'hello' or'ciao' or 'salut' or 'hallo' or 'hola' or 'ahoj' or 'czesc ' in greetings else False
    #     return True
    # return False 





