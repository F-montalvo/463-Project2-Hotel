from tkinter import *
import random

#download the file in command prompt go to where the file is located use python example.py

#This sets up the TK inter
root = Tk()
#This sets the size of th window
root.geometry('1250x700')
#This sets up the Title of the Window
root.title("Hotel Transylvania")
root.resizable(1,1)


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
    
#Capability 5
def GuestProfile():
    clear(frame2)
    #Guest
    Guestlabel = Label(frame2, text="Guest1", font=("arial", 12), height=2).grid(row=1, column=1)
    Guestlabel2 = Label(frame2, text="Guest2", font=("arial", 12), height=2).grid(row=1, column=2)
    Guestlabel3 = Label(frame2, text="Guest3", font=("arial", 12), height=2).grid(row=1, column=3)
    #Customer Information
    label1 = Label(frame2, text="First Name:", font=("arial", 12), height=2 ).grid(row=2, column=0)
    
    label2 = Label(frame2, text="Last Name:", font=("arial", 12), height=2 ).grid(row=3, column=0)
  
    label3 = Label(frame2, text="Phone:", font=("arial", 12), height=2 ).grid(row=4, column=0)
   
    label4 = Label(frame2, text="Address", font=("arial", 12), height=2 ).grid(row=5, column=0)

    label5 = Label(frame2, text="E-mail", font=("arial", 12), height=2 ).grid(row=6, column=0)
 
    label6 = Label(frame2, text="ID info(State,ID#)", font=("arial", 12), height=2 ).grid(row=7, column=0)
    
    label7 = Label(frame2, text="Vehicle License Plate", font=("arial", 12), height=2 ).grid(row=8, column=0)
    
    #Guest1
    name1 = Entry(frame2,  font = ("arial", 12)).grid(row=2,column=1)
    lname1 = Entry(frame2,  font = ("arial", 12)).grid(row=3,column=1)
    phone1 = Entry(frame2,  font = ("arial", 12)).grid(row=4,column=1)
    address1 = Entry(frame2,  font = ("arial", 12)).grid(row=5,column=1)
    Email1 = Entry(frame2,  font = ("arial", 12)).grid(row=6,column=1)
    IDinfo1 = Entry(frame2,  font = ("arial", 12)).grid(row=7,column=1)
    Vehiclelicense1 = Entry(frame2,  font = ("arial", 12)).grid(row=8,column=1)

    #Guest2
    name2 = Entry(frame2,  font = ("arial", 12)).grid(row=2,column=2)
    lname2 = Entry(frame2,  font = ("arial", 12)).grid(row=3,column=2)
    phone2 = Entry(frame2,  font = ("arial", 12)).grid(row=4,column=2)
    address2 = Entry(frame2,  font = ("arial", 12)).grid(row=5,column=2)
    Email2 = Entry(frame2,  font = ("arial", 12)).grid(row=6,column=2)
    IDinfo2 = Entry(frame2,  font = ("arial", 12)).grid(row=7,column=2)
    Vehiclelicense2 = Entry(frame2,  font = ("arial", 12)).grid(row=8,column=2)

    #Guest3
    name3 = Entry(frame2,  font = ("arial", 12)).grid(row=2,column=3)
    lname3 = Entry(frame2,  font = ("arial", 12)).grid(row=3,column=3)
    phone3 = Entry(frame2,  font = ("arial", 12)).grid(row=4,column=3)
    address3 = Entry(frame2,  font = ("arial", 12)).grid(row=5,column=3)
    Email3 = Entry(frame2,  font = ("arial", 12)).grid(row=6,column=3)
    IDinfo3 = Entry(frame2,  font = ("arial", 12)).grid(row=7,column=3)
    Vehiclelicense3 = Entry(frame2,  font = ("arial", 12)).grid(row=8,column=3)
    
    frame2.grid(row=1,column=0)


#Capability 6
def GuestInfo():
    clear(frame2)
    Guestlabel = Label(frame2, text="Guest1", font=("arial", 12), height=2).grid(row=1, column=1)
    Guestlabel2 = Label(frame2, text="Guest2", font=("arial", 12), height=2).grid(row=1, column=2)
    Guestlabel3 = Label(frame2, text="Guest3", font=("arial", 12), height=2).grid(row=1, column=3)
    #Customer Information
    label1 = Label(frame2, text="Guest Name:", font=("arial", 12), height=2 ).grid(row=2, column=0)
    
    label2 = Label(frame2, text="Check In Date and Time", font=("arial", 12), height=2 ).grid(row=3, column=0)
  
    label3 = Label(frame2, text="Expected Check Out Date and Time", font=("arial", 12), height=2 ).grid(row=4, column=0)
   
    label4 = Label(frame2, text="Room Type", font=("arial", 12), height=2 ).grid(row=5, column=0)

    label5 = Label(frame2, text="Room Number", font=("arial", 12), height=2 ).grid(row=6, column=0)
 
    label6 = Label(frame2, text="Room Rate ($/Day", font=("arial", 12), height=2 ).grid(row=7, column=0)
    
    label7 = Label(frame2, text="Total Charge", font=("arial", 12), height=2 ).grid(row=8, column=0)

    label8 = Label(frame2, text="Payments Made", font=("arial", 12), height=2 ).grid(row=9, column=0)

    label9 = Label(frame2, text="Balance", font=("arial", 12), height=2 ).grid(row=10, column=0)
    
    #Guest1
    guest1 = Entry(frame2,  font = ("arial", 12)).grid(row=2,column=1)
    checkin1 = Entry(frame2,  font = ("arial", 12)).grid(row=3,column=1)
    checkout1 = Entry(frame2,  font = ("arial", 12)).grid(row=4,column=1)
    roomtype1 = Entry(frame2,  font = ("arial", 12)).grid(row=5,column=1)
    roomnum1 = Entry(frame2,  font = ("arial", 12)).grid(row=6,column=1)
    roomrate1 = Entry(frame2,  font = ("arial", 12)).grid(row=7,column=1)
    totalcharge1 = Entry(frame2,  font = ("arial", 12)).grid(row=8,column=1)
    paymentsmade1 = Entry(frame2,  font = ("arial", 12)).grid(row=9,column=1)
    balance1 = Entry(frame2,  font = ("arial", 12)).grid(row=10,column=1)

    #Guest2
    guest2 = Entry(frame2,  font = ("arial", 12)).grid(row=2,column=2)
    checkin2 = Entry(frame2,  font = ("arial", 12)).grid(row=3,column=2)
    checkout2 = Entry(frame2,  font = ("arial", 12)).grid(row=4,column=2)
    roomtype2 = Entry(frame2,  font = ("arial", 12)).grid(row=5,column=2)
    roomnum2 = Entry(frame2,  font = ("arial", 12)).grid(row=6,column=2)
    roomrate2 = Entry(frame2,  font = ("arial", 12)).grid(row=7,column=2)
    totalcharge2 = Entry(frame2,  font = ("arial", 12)).grid(row=8,column=2)
    paymentsmade2 = Entry(frame2,  font = ("arial", 12)).grid(row=9,column=2)
    balance2 = Entry(frame2,  font = ("arial", 12)).grid(row=10,column=2)

    #Guest3
    guest3 = Entry(frame2,  font = ("arial", 12)).grid(row=2,column=3)
    checkin3 = Entry(frame2,  font = ("arial", 12)).grid(row=3,column=3)
    checkout3 = Entry(frame2,  font = ("arial", 12)).grid(row=4,column=3)
    roomtype3 = Entry(frame2,  font = ("arial", 12)).grid(row=5,column=3)
    roomnum3 = Entry(frame2,  font = ("arial", 12)).grid(row=6,column=3)
    roomrate3 = Entry(frame2,  font = ("arial", 12)).grid(row=7,column=3)
    totalcharge3 = Entry(frame2,  font = ("arial", 12)).grid(row=8,column=3)
    paymentsmade3 = Entry(frame2,  font = ("arial", 12)).grid(row=9,column=3)
    balance3 = Entry(frame2,  font = ("arial", 12)).grid(row=10,column=3)
    

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
    frame2.grid(row=1,column=0)

Capability1 = Button(frame1, text='Show Rooms and Status', command=ShowRooms,font=("arial", 12), width=20,height=5)
Capability1.grid(row = 0, column=0)
Capability2 = Button(frame1, text='Show Room Availability', command=execute,font=("arial", 12), width=20,height=5)
Capability2.grid(row = 0, column=1)
Capability3 = Button(frame1, text='Customer Reservation', command=execute,font=("arial", 12), width=20,height=5)
Capability3.grid(row = 0, column=2)
Capability4 = Button(frame1, text='Housekeeping', command=execute,font=("arial", 12), width=20,height=5)
Capability4.grid(row = 0, column=3)
Capability5 = Button(frame1, text='Guest Profile', command=GuestProfile,font=("arial", 12), width=20,height=5)
Capability5.grid(row = 0, column=4)
Capability6 = Button(frame1, text='Current Stay', command=GuestInfo,font=("arial", 12), width=20,height=5)
Capability6.grid(row = 0, column=5)
Capability7 = Button(frame1, text='Search', command=Search,font=("arial", 12), width=20,height=5)
Capability7.grid(row = 0, column=6)
Capability8 = Button(frame1, text='Daily Report', command=report,font=("arial", 12), width=20,height=5)
Capability8.grid(row = 0, column=7)
frame1.grid(row=0,column=0)

root.mainloop()