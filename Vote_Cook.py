'''
Pet Vote
Samantha Cook
5/23/2023
Python II
'''

import tkinter as tk

# -- Global Variables --

votes_for_dogs = 0
votes_for_cats = 0

# -- Event Handlers --

def place_vote():
    '''
    Adds a ote to the desired choice.
    '''
    global votes_for_cats, votes_for_dogs
    
    if selection.get() == 'dog':
        votes_for_dogs += 1
        
    else:
        votes_for_cats += 1
        
    
    
def tabulate_results():
    '''
    Writies the results of the poll to a file.
    '''
    file = open('results.txt', 'w')
    file.write('Vote for dogs: ' + str(votes_for_dogs))
    file.write('Votes for cats: ' + str(votes_for_cats))
    

# -- GUI --
window = tk.Tk()
window.title('Vote')

selection = tk.StringVar()

label = tk.Label(window, text='Select your favorite pet.')
label.pack(padx=3, pady=3)

#dog radio button
dog_radio_button = tk.Radiobutton(window,
                                  text='Dogs',
                                  variable=selection,
                                  value='dog')
dog_radio_button.pack(padx=3, pady=3)
dog_radio_button.select()

#cat radio button
cat_radio_button = tk.Radiobutton(window,
                                  text='Cats',
                                  variable=selection,
                                  value='cat')
cat_radio_button.pack(padx=3, pady=3)

# vote button
vote_button = tk.Button(window,
                        text='Place Vote',
                        command=place_vote)
vote_button.pack(padx=3, pady=3)

# tabulate button
tabulate_button = tk.Button(window,
                        text='Tabulate Results',
                        command=tabulate_results)
tabulate_button.pack(padx=3, pady=3)


window.mainloop()