# Programmers: Harry Li, Liv Oakes
# Course:  CS151*06
# Due Date: 11/20/2024
# Lab Assignment: Lab 11
# Problem Statement: 
# Data In: 
# Data Out: 

import os 

def check_file(file_name):
    #See if file exists and store in a table
    if os.path.isfile(file_name):
        exist = 0
    else:
        exist = 1
    return exist 
    
def morse_key(file_name):
    #Create a dictionary to store the corresponding translations
    key_dictionary = {}
    #Open the file for reading, and for each line store the key and letter or charater to the dictionary
    with open(file_name, 'r') as file:
        for line in file:
            key = line.strip().split('\t')
            key_dictionary[key[1]] = key[0]
    #Return the dictionary 
    return key_dictionary
    
def morse_code_translation():
    

def main():
    
    morse_dictionary = morse_key(morsecode.txt)
    
    translate_file = input('Enter the file name you want to translate: ')
    exist = check_file(translate_file)
    while exist != 0:
        translate_file = input('Please enter a valid file name you want to translate: ')
        exist = check_file(translate_file)
        
