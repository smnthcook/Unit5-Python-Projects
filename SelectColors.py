'''
SelectColors
Samantha Cook
5/22/2023
Python II
'''

import tkinter as tk

# -- Event Handles --
def red_bg():
    '''
    Changes the background of the color of the label to red.
    '''
    output_label.config(bg='red')

def green_bg():
    '''
    Changes the background of the color of the label to green.
    '''
    output_label.config(bg='green')

def blue_bg():
    '''
    Changes the background of the color of the label to blue.
    '''
    output_label.config(bg='blue')

def red_fg():
    '''
    Changes the foreground of the color of the label to red.
    '''
    output_label.config(fg='red')

def green_fg():
    '''
    Changes the foreground of the color of the label to green.
    '''
    output_label.config(fg='green')

def blue_fg():
    '''
    Changes the foreground of the color of the label to blue.
    '''
    output_label.config(fg='blue')


# -- GUI --
window = tk.Tk()
window.title("Select Colors")

#red
bg_frame = tk.Frame(window)
bg_red = tk.Button(bg_frame,
                   text='Red',
                   bg='red',
                   command=red_bg,
                   font=('ariel', 20))
bg_red.pack(side=tk.LEFT, padx=3)
#green
bg_green = tk.Button(bg_frame,
                     text='Green',
                     bg='green',
                     command=green_bg,
                     font=('ariel', 20))
bg_green.pack(side=tk.LEFT, padx=3)
#blue
bg_blue = tk.Button(bg_frame,
                    text='Blue',
                    bg='blue',
                    command=blue_bg,
                    font=('ariel', 20))
bg_blue.pack(side=tk.LEFT, padx=3)
bg_frame.pack(pady=3)

#Foreground
#red
fg_frame = tk.Frame(window)
fg_red = tk.Button(fg_frame, text='Red',
                   fg='red',
                   command=red_fg,
                   font=('ariel', 20))
fg_red.pack(side=tk.LEFT, padx=3)
#green
fg_green = tk.Button(fg_frame,
                     text='Green',
                     fg='green',
                     command=green_fg,
                     font=('ariel', 20))
fg_green.pack(side=tk.LEFT, padx=3)
#blue
fg_blue = tk.Button(fg_frame,
                    text='Blue',
                    fg='blue',
                    command=blue_fg,
                    font=('ariel', 20))
fg_blue.pack(side=tk.LEFT, padx=3)
fg_frame.pack(pady=3)

output_label = tk.Label(window,
                        text='Python + Tkinker = GUIs',
                        font=('ariel', 40))
output_label.pack(padx=3, pady=3)

window.mainloop()
