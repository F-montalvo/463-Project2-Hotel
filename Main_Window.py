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

roomlist = []

class Room:
    def __init__(self,root,counter):
        size = ["King","Double Queen","Double Queen with Kitchen", "Suite"]
        availability  = {"Available":"green","Unavailable/Occupied":"red", "Unavailable/Dirty":"blue", "Unavailable/Maintenance":"purple"}
        key = ["Available","Unavailable/Occupied", "Unavailable/Dirty","Unavailable/Maintenance"]
        self.avail = key[random.randint(0,3)]
        self.roomsize = size[random.randint(0,3)]
        self.color = availability.get(self.avail)
        self.root = root
        roomlist.append(tk.Button(self.root, text = "Room #" + str(counter+1) + ' ' + self.roomsize, command = lambda: checkRoom(self,roomlist,counter), font =("arial",12)))

    def configure(self,counter):
        roomlist[counter].configure(fg = self.color)

def ShowRooms():
    legend = tk.Label(root, text = "Available", font = ("arial", 18))
    legend.configure(fg = "green")
    legend2 = tk.Label(root, text = "Unavailable/Occupied", font = ("arial", 18))
    legend2.configure(fg = "red")
    legend3 = tk.Label(root, text = "Unavailable/Dirty", font = ("arial", 18))
    legend3.configure(fg = "blue")
    legend4 = tk.Label(root, text = "Unavailable/Maintenance", font = ("arial", 18))
    legend4.configure(fg = "purple")

    legend.place(x = 300, y = 25)
    legend2.place(x = 420, y = 25)
    legend3.place(x = 680, y = 25)
    legend4.place(x = 880, y = 25)

    counter = 50
    i = 0
    while i < 20:
        Room(root,i)
        roomlist[i].place(x = 500, y = counter + 30)
        counter = counter + 30
        i = i + 1

def checkRoom(self,rooms,counter):
    self.configure(counter)



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
