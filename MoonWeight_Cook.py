'''
Moon Weight
Samantha Cook
5/18/2023
Python II
'''

import tkinter as tk

def calculate_weight():
    '''
    Calculates the moon weight of the person's earth weight
    '''
    
    earth_weight = float(ew_entry.get())
    moon_weight = float(earth_weight*9.81 / 1.622)
    mw_label.config(text="Moon Weight:" + str(moon_weight))



#GUI

window = tk.Tk()
window.title('Moon Weight')


# ew = Earth Weight
ew_frame = tk.Frame(window)
ew_label = tk.Label(ew_frame, text='Earth Weight:')
ew_entry = tk.Entry(ew_frame)
ew_label.pack(side=tk.LEFT, padx=5, pady=5)
ew_entry.pack(side=tk.LEFT, padx=5, pady=5)
ew_frame.pack()

calculate_button = tk.Button(window, text='Calculate Weight', command=calculate_weight)
calculate_button.pack(padx=5, pady=5)

# mw = moon weight
mw_label = tk.Label(window, text='Moon Weight: ')
mw_label.pack(padx=5, pady=5)
window.mainloop()