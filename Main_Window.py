import tkinter as tk

#download the file in command prompt go to where the file is located use python example.py

#This sets up the TK inter
root = tk.Tk()
#This sets the size of th window
root.geometry('1250x700')
#This sets up the Title of the Window
root.title("Main Window")
root.resizable(True,True)

def ShowRooms():
    



Capability1 = tk.Button(root, text='Show Rooms and Status', command=execute,font=("arial", 12))
Capability2 = tk.Button(root, text='Show Room Availability', command=execute,font=("arial", 12))
Capability3 = tk.Button(root, text='Customer Reservation', command=execute,font=("arial", 12))
Capability4 = tk.Button(root, text='Housekeeping', command=execute,font=("arial", 12))
Capability5 = tk.Button(root, text='Guest Profile', command=execute,font=("arial", 12))
Capability6 = tk.Button(root, text='Current Stay', command=execute,font=("arial", 12))
Capability7 = tk.Button(root, text='Search', command=execute,font=("arial", 12))
Capability8 = tk.Button(root, text='Daily Report', command=execute,font=("arial", 12))


Capability1.place(x = 0,y = 0)
Capability2.place(x = 0,y = 30)
Capability3.place(x = 0,y = 60)
Capability4.place(x = 0,y = 90)
Capability5.place(x = 0,y = 120)
Capability6.place(x = 0,y = 150)
Capability7.place(x = 0,y = 180)
Capability8.place(x = 0,y = 210)

root.mainloop()
