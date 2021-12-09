# Madlibs is a game where the user has to enter substitutes for blanks in the text without knowing said text

def madlib():   
    question = input('Would you like to play?(Yes/No) ').capitalize()
    
    while True:
        if question == 'Yes':
            adj = input('Adjetive: ')
            verb1 = input('Verb: ')
            verb2 = input('Verb: ')
            famous_person = input('Celebrity: ')
            text = f'Computer programing is so {adj}! It makes me so excited all the time\
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}'
            print(text)
            question = input('Would you like to play again?(Yes/No) ').capitalize()
        elif question == 'No':
            print('Goodbye!')
            break
        else:             
            print('You did not enter a correct answer.')
            question = input('Would you like to play again?(Yes/No) ').capitalize()
