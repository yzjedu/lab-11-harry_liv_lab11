# Programmers: Harry Li, Liv Oakes
# Course:  CS151*06
# Due Date: 11/20/2024
# Lab Assignment: Lab 11
# Problem Statement: 
# Data In: 
# Data Out: 

def check_file(file_name):
    try:
        with open(file_name, 'r') as file:
            morse_file = []
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    morse_file.append(stripped_line)
        return morse_file
    except FileNotFoundError:  
        print(f'Error: File {file_name} not found.')
        return []
def morse_key(file_name):
    key = []
    with open(file_name, 'r') as file:

def morse_code_translation():
