# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk

#This sets up the TK inter
root = tk.Tk()
#This sets the size of th window
root.geometry("650x500")
#This sets up the Title of the Window
root.title("Login")

def execute():
    print("Welcome!")

#Label object think of this as just displaying the text on the GUI
lUsername = tk.Label(root, text='This is a Label', font=("arial", 12))
lPassword = tk.Label(root, text='Password', font=("arial", 12))


 # Variables to Store Data think of this as like cin in c++
user = tk.StringVar()

passwd = tk.StringVar()

#entry object
eUsername = tk.Entry(root, textvariable=user, font=("arial", 12))

ePassword = tk.Entry(root, textvariable=passwd, show='*', font=("arial", 12))


bLogin = tk.Button(root, text='Login', command=execute, height=1, width=8, font=("arial", 12))


# placing in GUI
#this is the simplest way of placing it on the GUI but for more pecise placing
#we prolly have to use something else
lUsername.pack()

eUsername.pack()

lPassword.pack()

ePassword.pack()

bLogin.pack()

root.mainloop()
