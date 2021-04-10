
from tkinter import *
import random

#download the file in command prompt go to where the file is located use python example.py

#This sets up the TK inter
root = Tk()
#This sets the size of th window
root.geometry('1250x700')
#This sets up the Title of the Window
root.title("Hotel Transylvania")
root.resizable(False,False)


frame1 = Frame(root)
frame2 = Frame(root)

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
        roomlist.append(Button(self.root, text = "Room #" + str(counter+1) + ' ' + self.roomsize, command = lambda: checkRoom(self,roomlist,counter), font =("arial",12)))

    def configure(self,counter):
        roomlist[counter].configure(fg = self.color)

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
def ShowRooms():
    clear(frame2)
    legend = Label(frame2, text = "Available", font = ("arial", 18))
    legend.configure(fg = "green")
    legend2 = Label(frame2, text = "Unavailable/Occupied", font = ("arial", 18))
    legend2.configure(fg = "red")
    legend3 = Label(frame2, text = "Unavailable/Dirty", font = ("arial", 18))
    legend3.configure(fg = "blue")
    legend4 = Label(frame2, text = "Unavailable/Maintenance", font = ("arial", 18))
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


def Search():
    clear(frame2)
    label1 = Label(frame2, text = "Guest First Name", font = ("arial", 12),height= 2).grid(row=0,column=0)
    field1 = Entry(frame2,  font = ("arial", 12)).grid(row=0,column=1)
    label2 = Label(frame2, text = "Guest last Name", font = ("arial", 12),height= 2).grid(row=0,column=2)
    field2 = Entry(frame2, font = ("arial", 12)).grid(row=0,column=3)
    label3 = Label(frame2, text = "Room Number", font = ("arial", 12),height= 2).grid(row=0,column=4)
    field3 = Entry(frame2, font = ("arial", 12)).grid(row=0,column=5)
    label4 = Label(frame2, text = "Phone Number", font = ("arial", 12),height= 2).grid(row=0,column=6)
    field4 = Entry(frame2, font = ("arial", 12)).grid(row=0,column=7)
    label5 = Label(frame2, text = "Street Address", font = ("arial", 12) ,height= 2).grid(row=1,column=0)
    field5 = Entry(frame2, font = ("arial", 12)).grid(row=1,column=1)
    label5 = Label(frame2, text = "Check In Date", font = ("arial", 12) ,height= 2).grid(row=1,column=2)
    field5 = Entry(frame2, font = ("arial", 12)).grid(row=1,column=3)
    label6 = Label(frame2, text = "Check In Date", font = ("arial", 12) ,height= 2).grid(row=1,column=4)
    field6 = Entry(frame2, font = ("arial", 12)).grid(row=1,column=5)
    Button1 = Button(frame2, text='Search',font=("arial", 14)).grid(row=1,column=6)
    frame2.grid(row=1,column=0)
    

def report():
    clear(frame2)
    
    label1 = Label(frame2, text = "Today's report", font = ("arial", 20),height= 2).grid(row=0,column=0)
    for i in range(1,6):
        for j in range(1,5):
            b = Entry(frame2, text="------")
            b.grid(row=i, column=j)
    frame2.grid(row=1,column=0)
    

Capability1 = Button(frame1, text='Show Rooms and Status', command=ShowRooms,font=("arial", 12), width=20,height=5)
Capability1.grid(row = 0, column=0)
Capability2 = Button(frame1, text='Show Room Availability', command=execute,font=("arial", 12), width=20,height=5)
Capability2.grid(row = 0, column=1)
Capability3 = Button(frame1, text='Customer Reservation', command=execute,font=("arial", 12), width=20,height=5)
Capability3.grid(row = 0, column=2)
Capability4 = Button(frame1, text='Housekeeping', command=execute,font=("arial", 12), width=20,height=5)
Capability4.grid(row = 0, column=3)
Capability5 = Button(frame1, text='Guest Profile', command=execute,font=("arial", 12), width=20,height=5)
Capability5.grid(row = 0, column=4)
Capability6 = Button(frame1, text='Current Stay', command=execute,font=("arial", 12), width=20,height=5)
Capability6.grid(row = 0, column=5)
Capability7 = Button(frame1, text='Search', command=Search,font=("arial", 12), width=20,height=5)
Capability7.grid(row = 0, column=6)
Capability8 = Button(frame1, text='Daily Report', command=report,font=("arial", 12), width=20,height=5)
Capability8.grid(row = 0, column=7)
frame1.grid(row=0,column=0)

root.mainloop()
