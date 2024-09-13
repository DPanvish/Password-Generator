
# Importing required library

import random
import string

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image


# Colors

Col1 = "#444466" # Black
Col2 = "#feffff" # White
Col3 = "#6f9fbd" # Blue
Col4 = "#f05a43" # Red

bg_color = Col1

root = Tk()
root.title("")
root.geometry("300x360")
root.configure(bg = bg_color)


# Creating Frames

frame_main = Frame(root, width = 300, height = 110, bg = bg_color)
frame_main.grid(row = 0, column = 0)

frame_box = Frame(root, width = 300, height = 220, bg = bg_color)
frame_box.grid(row = 1, column = 0)


# Working with frame main


# Define Image

img = Image.open("Logo.png")
img = img.resize((35, 35))
img = ImageTk.PhotoImage(img)

app_img = Label(frame_main, height = 60, image = img, compound = LEFT, padx = 10, anchor = "nw", font = ("Ivy 16 bold"), bg = Col1, fg = Col4)
app_img.place(x = 2, y = 0)

app_name = Label(frame_main, text = "PASSWORD GENERATOR", width = 20, height = 1, padx = 0, anchor = "nw", font = ("Ivy 14 bold"), bg = Col1, fg = Col2)
app_name.place(x = 40, y = 2)

app_line = Label(frame_main, width = 400, height = 1, padx = 0, anchor = "nw", font = ("Arial 1"), bg = Col4, fg = Col2)
app_line.place(x = 0, y = 35)


# Function to generate password

def generate_password():
    lowercase_alphabets = string.ascii_lowercase
    uppercase_alphabets = string.ascii_uppercase
    numbers = "1234567890"
    symbols = "{}[]()!@#$%^&*;_-~"
    
    global combine
    combine = ""
    
    # Uppercase letters condition
    
    if state_1.get() == uppercase_alphabets:
        combine += uppercase_alphabets
    else:
        pass
    
    # Lowercase letters condition
    
    if state_2.get() == lowercase_alphabets:
        combine += lowercase_alphabets
    else:
        pass
    
    # Numbers condition
    
    if state_3.get() == numbers:
        combine += numbers
    else:
        pass
    
    # Symbols condition
    
    if state_4.get() == symbols:
        combine += symbols
    else:
        pass
        
    
    # Password length
    
    length = int(spin.get())
    
    
    # Password
    
    password = "".join(random.sample(combine, length))
    
    app_password["text"] = password
    
    
    # Function to copy the password
    
    def copy_password():
        info = password
        frame_box.clipboard_clear()
        frame_box.clipboard_append(info)
        messagebox.showinfo("Success", "The password has been copied successfully")
    
    copy_btn = Button(frame_box, command = copy_password, text = "Copy", width = 7, overrelief = SOLID, bg = bg_color, fg = Col2, font = ("Ivy 10 bold"), anchor = "center", relief = RAISED)
    copy_btn.grid(row = 0, column = 2, sticky = NSEW, pady = 10, columnspan = 2)

# Defining Variables

lowercase_alphabets = string.ascii_lowercase
uppercase_alphabets = string.ascii_uppercase
numbers = "1234567890";
symbols = "{}[]()!@#$%^&*;_-~"


# Working on spin box

var = IntVar()
var.set(8)
app_info = Label(frame_main, text = "Total number of characters in the password", height = 1, padx = 0, anchor = "nw", font = ("Ivy 10 bold"), bg = Col1, fg = Col2)
app_info.place(x = 15, y = 60)
spin = Spinbox(frame_main, width = 5, from_ = 0, to = 20, textvariable = var)
spin.place(x = 20, y = 90)


# Working with frame box

app_password = Label(frame_box, text = "- - -", width = 20, height = 2, relief = "solid", padx = 0, anchor = "center", font = ("Ivy 10 bold"), bg = Col1, fg = Col2)
app_password.grid(row = 0, column = 0, columnspan = 2, sticky = NSEW, pady = 10, padx = 2)


# Uppercase letters

app_info = Label(frame_box, text = "ABC Uppercase letters", height = 1, padx = 0, anchor = "nw", justify = "center", font = ("Ivy 10 bold"), bg = Col1, fg = Col2)
app_info.grid(row = 1, column = 1, sticky = NSEW, pady = 5, padx = 2)

state_1 = StringVar()
state_1.set(False) # Set check state

check_1 = Checkbutton(frame_box, width = 1, var = state_1, onvalue = uppercase_alphabets, offvalue = "off", bg = bg_color)
check_1.grid(row = 1, column = 0, sticky = NSEW, pady = 5, padx = 2)


# Lowercase letters

app_info = Label(frame_box, text = "abc Lowercase letters", height = 1, padx = 0, anchor = "nw", justify = "center", font = ("Ivy 10 bold"), bg = Col1, fg = Col2)
app_info.grid(row = 2, column = 1, sticky = NSEW, pady = 5, padx = 2)

state_2 = StringVar()
state_2.set(False) # Set check state

check_2 = Checkbutton(frame_box, width = 1, var = state_2, onvalue = lowercase_alphabets, offvalue = "off", bg = bg_color)
check_2.grid(row = 2, column = 0, sticky = NSEW, pady = 5, padx = 2)


# Numbers

app_info = Label(frame_box, text = "123 Numbers", height = 1, padx = 0, anchor = "nw", justify = "center", font = ("Ivy 10 bold"), bg = Col1, fg = Col2)
app_info.grid(row = 3, column = 1, sticky = NSEW, pady = 5, padx = 2)

state_3 = StringVar()
state_3.set(False) # Set check state

check_3 = Checkbutton(frame_box, width = 1, var = state_3, onvalue = numbers, offvalue = "off", bg = bg_color)
check_3.grid(row = 3, column = 0, sticky = NSEW, pady = 5, padx = 2)


# Symbols

app_info = Label(frame_box, text = "@#$ Symbols", height = 1, padx = 0, anchor = "nw", justify = "center", font = ("Ivy 10 bold"), bg = Col1, fg = Col2)
app_info.grid(row = 4, column = 1, sticky = NSEW, pady = 5, padx = 2)

state_4 = StringVar()
state_4.set(False) # Set check state

check_4 = Checkbutton(frame_box, width = 1, var = state_4, onvalue = symbols, offvalue = "off", bg = bg_color)
check_4.grid(row = 4, column = 0, sticky = NSEW, pady = 5, padx = 2)


# Generate password button

generate_password_btn = Button(frame_box, command = generate_password, text = "Generate Password", width = 32, overrelief = SOLID, bg = Col4, fg = Col2, font = ("Ivy 10 bold"), anchor = "center", relief = FLAT)
generate_password_btn.grid(row = 5, column = 0, sticky = NSEW, pady = 20, padx = 0, columnspan = 5)


root.mainloop()