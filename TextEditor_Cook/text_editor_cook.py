'''
Text editor
Samantha Cook
5/25/2023
Python II
'''

import tkinter as tk
import tkinter.filedialog as fdia

# global variables

file_path = 'Untitled'

# event handlers
def new_file():
    '''
    Creates a new text file.
    '''
    global file_path
    file_path = 'Untitled'
    window.title(file_path + ' - Text Editor')
    text_editor.delete('0.0', 'end')

def open_file():
    '''
    Opens an existing file.
    '''
    global file_path
    file = fdia.askopenfile(filetypes=[('Text File', '.txt')])
    if file:
        file_path = file.name
        window.title(file_path + ' - Text Editor')
        text_editor.delete('0.0', 'end')
        text_editor.insert(tk.END, file.read())
        file.close()
        
def save_as():
    '''
    Saves file as a new name.
    '''
    global file_path
    file = fdia.asksaveasfile(filetypes=[('Text File', '.txt')], defaultextension='.txt')
    if file:
        file_path = file.name
        file.write(text_editor.get('0.0','end'))
        file.close()
        window.title(file_path + ' - Text Editor')
        
def save():
    '''
    Saves the currently opened file.
    '''
    global file_path
    if file_path == 'Untitled':
        save_as()
    else:
        file = open(file_path, 'w')
        file.write(text_editor.get('0.0', 'end'))
        file.close()

def close():
    '''
    Closes the application.
    '''
    window.destroy()

# -- GUI --

#window
window = tk.Tk()
window.title('Untitled - Text Editor')
window.minsize(300, 300)

#frame
controls_frame = tk.Frame(window)

#new button
new_button = tk.Button(controls_frame, text='New', command=new_file)
new_button.pack(side=tk.LEFT, padx=3)

#open button
open_button = tk.Button(controls_frame, text='Open', command=open_file)
open_button.pack(side=tk.LEFT, padx=3)

#save as button
save_as_button = tk.Button(controls_frame, text='Save As', command=save_as)
save_as_button.pack(side=tk.LEFT, padx=3)

#save button
save_button = tk.Button(controls_frame, text='Save', command=save)
save_button.pack(side=tk.LEFT, padx=3)

#exit button
exit_button = tk.Button(controls_frame, text='Exit', command=close)
exit_button.pack(side=tk.LEFT, padx=3)

controls_frame.pack(fill=tk.X, pady=3)


text_editor = tk.Text(window)
text_editor.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
window.mainloop()

