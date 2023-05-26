'''
Count Change
Samantha Cook
5/19/2023
Python II
'''

import tkinter as tk
#Event Handlers
def calculate_change():
    '''
    Calculates the change given the number of pennies,
    nickles, dimes and quarters.
    '''
    pennies = int(pennies_entry.get())
    nickles =  int(nickles_entry.get())
    dimes = int(dimes_entry.get())
    quarters = int(quarters_entry.get())
    total = 0.01 * pennies + 0.05 * nickles + 0.1 * dimes + 0.25 * quarters
    change_label.config(text='Total Change: $' + str(total))
    
    
# GUI

#Window Creation
window = tk.Tk()
window.title('Count Change')

# -- setup frames

#pennies
pennies_frame = tk.Frame(window)
pennies_label = tk.Label(pennies_frame, text='Pennies:')
pennies_entry = tk.Entry(pennies_frame)
pennies_label.pack(side=tk.LEFT, padx=5, pady=5)
pennies_entry.pack(side=tk.LEFT, padx=5, pady=5)
pennies_frame.pack()

#nickles
nickles_frame = tk.Frame(window)
nickles_label = tk.Label(nickles_frame, text='Nickles:')
nickles_entry = tk.Entry(nickles_frame)
nickles_label.pack(side=tk.LEFT, padx=5, pady=5)
nickles_entry.pack(side=tk.LEFT, padx=5, pady=5)
nickles_frame.pack()

#dimes
dimes_frame = tk.Frame(window)
dimes_label = tk.Label(dimes_frame, text='Dimes:')
dimes_entry = tk.Entry(dimes_frame)
dimes_label.pack(side=tk.LEFT, padx=5, pady=5)
dimes_entry.pack(side=tk.LEFT, padx=5, pady=5)
dimes_frame.pack()

#quarters
quarters_frame = tk.Frame(window)
quarters_label = tk.Label(quarters_frame, text='Quarters:')
quarters_entry = tk.Entry(quarters_frame)
quarters_label.pack(side=tk.LEFT, padx=5, pady=5)
quarters_entry.pack(side=tk.LEFT, padx=5, pady=5)
quarters_frame.pack()


calculate_button = tk.Button(window, text='Calculate Change', command=calculate_change)
calculate_button.pack(padx=5, pady=5)

change_label = tk.Label(window, text='Total Change:')
change_label.pack(padx=5, pady=5)
window.mainloop()
