import random


def dice_roller():
    """Generates two random numbers between 1 and 6, and its addition"""
    repeat = input('Do you want to roll the dice? ').capitalize()
    
    while True:
        if repeat == 'Yes':
            number = random.randint(1, 6)
            number_2 = random.randint(1, 6)
            addition = number + number_2
            print(f'Dice 1: {number}\nDice 2: {number_2}\nAddition: {addition}')
            repeat = input('Do you want to roll the dice again? ').capitalize()
        elif repeat == 'No':
            print('Goodbye')
            break
        else:
            print('You did not enter a proper answer')
            repeat = input('Do you want to roll the dice? ').capitalize()
            
            
dice_roller() 
