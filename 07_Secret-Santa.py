# Secret Santa Code Challenge!
# Store the participants' names in an array/list.
# Pair participants and output the pairs.


import random

santas_helpers = ['Michael Scott',
                 'Dwight Schrute',
                 'Jim Halpert',
                 'Pam Beesly',
                 'Jan Levinson',
                 'Kevin Malone',
                 'Toby Flenderson',
                 'Angela Martin',
                 'Andy Bernard',
                 'Stanley Hudson',
                 'Ryan Howard',
                 'Kelly Kapoor']


def santas_elves(santa_list):
    """Recieves a list of nice people and 
    gives the elves a little help on Christmas
    """
    gift_receivers = santa_list.copy()  
    print('Santa\'s nice list:')
    print()
    
    # shuffles gift_receivers until all the matches aren't with the same person
    while any(santa_list[i] == gift_receivers[i] for i in range(len(santa_list))):
        random.shuffle(gift_receivers)
        
    # pairs people with the gift receivers 
    for f in range(len(santa_list)):
        print(f'{santa_list[f]} gives a gift to --> {gift_receivers[f]}')

        
santas_elves(santas_helpers)
