import tkinter as tk
import random

#download the file in command prompt go to where the file is located use python example.py

#This sets up the TK inter
root = tk.Tk()
#This sets the size of th window
root.geometry('1250x700')
#This sets up the Title of the Window
root.title("Hotel Transylvania")
root.resizable(False,False)

isClicked = False

def ShowRooms():
    counter = 0
    size = ["King","Double Queen","Double Queen with Kitchen", "Suite"]
    roomlist = [0 for i in range(20)]
    rooms = list()
    i = 0
    while i < 20:
        randsize = size[random.randint(0,3)]
        roomlist[i] = tk.Button(root, text= "Room #" + str(i+1) + " " + randsize)
        rooms.append([roomlist[i],isClicked])
        roomlist
        roomlist[i].config(command = lambda: checkRoom(rooms), font=("arial", 12))
        roomlist[i].place(x = 500, y = counter + 30)
        counter = counter + 30
        i = i + 1

def checkRoom(rooms):
    for i in rooms:
        if rooms[1] == True
    availability  = ["Available","Unavailable/Occupied", "Unavailable/Dirty", "Unavailable/Maintenance"]
    color = ["green","red","yellow", "purple"]
    rand = random.randint(0,3)
    if rand == 0:
        pick = color[0]
    elif rand== 1:
        pick = color[1]
    elif  rand== 2:
        pick = color[2]
    elif rand== 3:
        pick = color[3]
    roomlist[id].configure(fg= pick)



def execute():
    print("welcome")


Capability1 = tk.Button(root, text='Show Rooms and Status', command=ShowRooms,font=("arial", 12))
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
