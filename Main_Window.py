from tkinter import *
import random
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import date
from functools import partial
from filldb import create_connection,get_type,get_status,get_report_data,search_data, get_guest, update_guest, get_booking, get_guest_1,get_payment,get_rooms, get_housekeeping, get_availiable_rooms, get_reservations
# download the file in command prompt go to where the file is located use python example.py

root = Tk()
#This sets the size of th window
root.geometry('1600x900')
#This sets up the Title of the Window
root.title("Hotel Transylvania")
root.resizable(True,True)


frame1 = Frame(root)
frame2 = Frame(root)
roomlist = []
schedulelist = []

class Room:
    def __init__(self,root,i,lock):
        #size = ["King","Double Queen","Double Queen with Kitchen", "Suite"]
        availability  = {"Available":"green","Unavailable/Occupied":"red", "Unavailable/Dirty":"blue", "Unavailable/Maintenance":"purple"}
        #key = ["Available","Unavailable/Occupied", "Unavailable/Dirty","Unavailable/Maintenance"]
        conn = create_connection()
        self.avail = get_status(conn,i+1)
        self.roomsize = get_type(conn,i+1)
        conn.close()
        self.color = availability.get(self.avail)
        self.schedule = ["None","Occupied"]
        self.week = [self.schedule[random.randint(0,1)],self.schedule[random.randint(0,1)],self.schedule[random.randint(0,1)],self.schedule[random.randint(0,1)],self.schedule[random.randint(0,1)],self.schedule[random.randint(0,1)],self.schedule[random.randint(0,1)]]
        self.root = root
        if lock == 1:
            roomlist.append(Button(self.root, text = "Room #" + str(i+1) + ' ' + self.roomsize, command = lambda: checkRoom(self,roomlist,i), font =("arial",12)))
        if lock == 2:
            roomlist.append(Label(self.root, text = "Room #" + str(i+1) + ' ' + self.roomsize, font =("arial",12)))
            for item in self.week:
                schedulelist.append(Label(self.root, text = item, font = ("arial,12")))

    def configure(self,i):
        roomlist[i].configure(fg = self.color)

def clear(frame):
    roomlist.clear()
    schedulelist.clear()
    for widget in frame.winfo_children():
        widget.destroy()


#Capability1
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

    legend.grid(row = 1, column = 0)
    legend2.grid(row = 1, column = 1)
    legend3.grid(row = 1, column = 2)
    legend4.grid(row = 1, column = 3)

    rowcounter = 2
    counter = 0
    i = 0
    while i < 20:
        Room(frame2,i,1)
        if counter > 3:
            counter = 0
            rowcounter = rowcounter + 1
        roomlist[i].grid(row = rowcounter, column = counter)
        counter = counter + 1
        i = i + 1
    frame2.grid(row=1,column=0,sticky = 'nwse')

def checkRoom(self,rooms,counter):
    self.configure(counter)

#Capability2
def roomSchedule():
    clear(frame2)
    #scrollbar = Scrollbar(frame2)
    #scrollbar.grid(row = 1, column = 0, sticky = "NWS")

    monday = Label(frame2, text = "Monday", font = ("arial", 14))
    tuesday = Label(frame2, text = "Tuesday", font = ("arial", 14))
    wednesday = Label(frame2, text = "Wednesday", font = ("arial", 14))
    thursday = Label(frame2, text = "Thursday", font = ("arial", 14))
    friday = Label(frame2, text = "Friday", font = ("arial", 14))
    saturday = Label(frame2, text = "Saturday", font = ("arial", 14))
    sunday = Label(frame2, text = "Sunday", font = ("arial", 14))

    monday.grid(row = 1, column = 2)
    tuesday.grid(row = 1, column = 3)
    wednesday.grid(row = 1, column = 4)
    thursday.grid(row = 1, column = 5)
    friday.grid(row = 1, column = 6)
    saturday.grid(row = 1, column = 7)
    sunday.grid(row = 1, column = 8)


    rowcounter = 2
    counter = 1
    i = 0
    while i < 20:
        Room(frame2,i,2)
        roomlist[i].grid(row = i+rowcounter, column = 0)
        i = i + 1
    j = 0
    while j < len(schedulelist):
        if j% 7 == 0 and j != 0:
            rowcounter = rowcounter + 1
            counter = 1
        schedulelist[j].grid(row = rowcounter, column = counter+1)
        j = j+1
        counter= counter +1
    frame2.grid(row=1,column=0, sticky = 'wsne')

def execute():
    print("welcome")


#Capability 7
def Search():
    clear(frame2)
    frame3 = Frame(frame2)
    frame4 = Frame(frame2)
    frame5 = Frame(frame2)
    Label(frame3, text = "Guest First Name", font = ("arial", 12),height= 2).grid(row=0,column=0)
    FirstName = Entry(frame3,font = ("arial", 12))
    FirstName.grid(row=0,column=1)
    Label(frame3, text = "Guest Last Name", font = ("arial", 12),height= 2).grid(row=0,column=2)
    LastName = Entry(frame3, font = ("arial", 12))
    LastName.grid(row=0,column=3)
    Label(frame3, text = "Room Number", font = ("arial", 12),height= 2).grid(row=0,column=4)
    Room = Entry(frame3, font = ("arial", 12))
    Room.grid(row=0,column=5)
    Label(frame3, text = "Phone Number", font = ("arial", 12),height= 2).grid(row=0,column=6)
    Phone = Entry(frame3, font = ("arial", 12))
    Phone.grid(row=0,column=7)
    Label(frame4, text = "Street Address", font = ("arial", 12) ,height= 2).grid(row=1,column=0)
    Address = Entry(frame4, font = ("arial", 12))
    Address.grid(row=1,column=1)
    Label(frame4, text = "Check In Date", font = ("arial", 12) ,height= 2).grid(row=1,column=2)
    CheckIn = Calendar(frame4, selectmode = 'day',date_pattern ='y-mm-dd')
    CheckIn.selection_clear()
    CheckIn.grid(row=1,column=3)
    Label(frame4, text = "Check Out Date", font = ("arial", 12) ,height= 2).grid(row=1,column=4)
    CheckOut = Calendar(frame4,  selectmode = 'day',date_pattern ='y-mm-dd')
    CheckOut.selection_clear()
    CheckOut.grid(row=1,column=5)
    
    def check():
        search_result = search_data(FirstName.get(),LastName.get(),Room.get(),Phone.get(),Address.get(),CheckIn.get_date(),CheckOut.get_date())
        if search_result:
            clear(frame5)
            Label(frame5, text="Guest Name", font=("arial", 20), height=2,width= 18).grid(row=0, column=0)
            Label(frame5, text="Room Number", font=("arial", 20), height=2,width= 18).grid(row=0, column=1)
            Label(frame5, text="Check In Date", font=("arial", 20), height=2, width= 18).grid(row=0, column=2)
            Label(frame5, text="Check out Date", font=("arial", 20), height=2, width= 18).grid(row=0, column=3)
            for i in range(len(search_result)):
                B = Button(frame5, text=search_result[i][0]+' '+search_result[i][1], command=partial(GuestProfile,search_result[i][5]),font = ("arial", 15),height= 2, width= 24, borderwidth=1, relief="groove")
                B.grid(row=i+1, column=0)
                Label(frame5, text=search_result[i][2],font = ("arial", 15),height= 2, width= 24, borderwidth=1, relief="groove").grid(row=i+1, column=1)
                Label(frame5, text=search_result[i][3],font = ("arial", 15),height= 2, width= 24, borderwidth=1, relief="groove").grid(row=i+1, column=2)
                Label(frame5, text=search_result[i][4],font = ("arial", 15),height= 2, width= 24, borderwidth=1, relief="groove").grid(row=i+1, column=3)
        elif search_result == []:
            clear(frame5)
            Label(frame5, text="No Match Found", font=("arial", 25), height=2).grid(row=0, column=0)
        else:
            clear(frame5)
            Label(frame5, text="Please Enter Input(s)", font=("arial", 25), height=2).grid(row=0, column=0)
        CheckIn.selection_clear()
        CheckOut.selection_clear()
        
            
    Button1 = Button(frame4, text='Search',command=check,font=("arial", 14)).grid(row=1,column=6)
    frame3.grid(row=0,column=0)
    frame4.grid(row=1,column=0)
    frame5.grid(row=2,column=0)
    frame2.grid(row=1,column=0)
    
#Capability 8
def report():
    clear(frame2)
    todays_report = get_report_data()
    frame3 = Frame(frame2)
    frame4 = Frame(frame2)
    total = 0
    Label(frame3, text = "Today's report: "+str(date.today()), font = ("arial", 25),height= 2).grid(row=0,columnspan=3)
    Label(frame4, text="Room Number", font=("arial", 20), height=2,width= 18).grid(row=1, column=0)
    Label(frame4, text="Guest Name", font=("arial", 20), height=2,width= 18).grid(row=1, column=1)
    Label(frame4, text="Check In Date", font=("arial", 20), height=2, width= 18).grid(row=1, column=2)
    Label(frame4, text="Check out Date", font=("arial", 20), height=2, width= 18).grid(row=1, column=3)
    Label(frame4, text="Amount", font=("arial", 20), height=2,width= 18).grid(row=1, column=4)
    #print(todays_report)
    if todays_report:
        for i in range(len(todays_report)):
            Label(frame4, text=todays_report[i][0],font = ("arial", 15),height= 2, width= 24, borderwidth=1, relief="groove").grid(row=i+2, column=0)
            Label(frame4, text=todays_report[i][1],font = ("arial", 15),height= 2, width= 24, borderwidth=1, relief="groove").grid(row=i+2, column=1)
            Label(frame4, text=todays_report[i][2],font = ("arial", 15),height= 2, width= 24, borderwidth=1, relief="groove").grid(row=i+2, column=2)
            Label(frame4, text=todays_report[i][3],font = ("arial", 15),height= 2, width= 24, borderwidth=1, relief="groove").grid(row=i+2, column=3)
            Label(frame4, text=todays_report[i][4],font = ("arial", 15),height= 2, width= 24, borderwidth=1, relief="groove").grid(row=i+2, column=4)
            total+= todays_report[i][4]
        Label(frame4, text="Today's Total",font = ("arial", 15),height= 4, width= 24).grid(row=i+2+1, column=3)
        Label(frame4, text=total,font = ("arial", 15),height= 4, width= 24, borderwidth=1, relief="groove").grid(row=i+2+1, column=4)
    else:
        Label(frame4, text="No Earnings today", font=("arial", 25), height=2).grid(row=2, column=0)
    frame3.grid(row=0,column=0)
    frame4.grid(row=1,column=0)
    frame2.grid(row=1,column=0)

#capability 4
def housekeeping():
    clear(frame2)
    hRoomNum = Label(frame2, text="Room Number", font=("arial", 12), height=2).grid(row=1, column=0)
    hHousekeeper = Label(frame2, text="Housekeeper", font=("arial", 12), height=2).grid(row=1, column=1)
    hRoomStatus = Label(frame2, text="Room Status", font=("arial", 12), height=2).grid(row=1, column=2)
    hRoomType = Label(frame2, text="Room Type", font=("arial", 12), height=2).grid(row=1, column=3)
    hBathroom = Label(frame2, text="Bathroom", font=("arial", 12), height=2).grid(row=1, column=4)
    hTowels = Label(frame2, text="Towels", font=("arial", 12), height=2).grid(row=1, column=5)
    hBedSheets = Label(frame2, text="Bed Sheets", font=("arial", 12), height=2).grid(row=1, column=6)
    hVacuum = Label(frame2, text="Vacuum", font=("arial", 12), height=2).grid(row=1, column=7)
    hDusting = Label(frame2, text="Dusting", font=("arial", 12), height=2).grid(row=1, column=8)
    hElectronics = Label(frame2, text="Electronics", font=("arial", 12), height=2).grid(row=1, column=9)

    dirtyrooms = get_housekeeping()

    for rooms in dirtyrooms:
        i = 0
        j = 0
        for x in dirtyrooms:
            j = 0
            for y in dirtyrooms[i]:
                droom = Label(frame2, text=str(dirtyrooms[i][j]), font=("arial", 12))
                droom.grid(row=i + 2, column=j)
                j += 1
            i += 1
        frame2.grid(row=1, column=0, sticky='nwse')

#capability 3
def Customer_Reservation():
    clear(frame2)
    roomList = ["Suite", "King", "Double Queen", "Double Queen with Kitchen"]
    crGFirst = StringVar()
    crGLast = StringVar()
    crCheckIn = StringVar()
    crCheckOut = StringVar()
    lGuestFirstName = Label(frame2, text="Enter First Name", font=("arial", 12), height=2).grid(row=1, column=0)
    lGuestLastName = Label(frame2, text="Enter Last Name", font=("arial", 12), height=2).grid(row=2, column=0)
    lCheckInDate = Label(frame2, text='Enter Check In Date', font=("arial", 12)).grid(row=3, column=0)
    lCheckOutDate = Label(frame2, text='Enter Check Out Date', font=("arial", 12)).grid(row=4, column=0)
    lRoomType = Label(frame2, text='Pick a Room Type', font=("arial", 12)).grid(row=5, column=0)
    # lRoomType.set("Pick a room type")

    eGuestFirstName = Entry(frame2, textvariable=crGFirst, font=("arial", 12)).grid(row=1, column=1)
    eGuestLastName = Entry(frame2, textvariable=crGLast, show='*', font=("arial", 12)).grid(row=2, column=1)
    eCheckInDate = Entry(frame2, textvariable=crCheckIn, font=("arial", 12)).grid(row=3, column=1)
    eCheckOutDate = Entry(frame2, textvariable=crCheckOut, font=("arial", 12)).grid(row=4, column=1)
    cbRoomType = ttk.Combobox(frame2, values=roomList)
    cbRoomType.current(0)
    cbRoomType.grid(row=5, column=1)
    bCheckAvailability = Button(frame2, text='Check Availability', command=lambda: Check_Availiable(cbRoomType.get()), height=1, width=14,
                                font=("arial", 12)).grid(row=6, column=0)
    bCheckAllReservations = Button(frame2, text='Check Reservations', command=Check_Reservations, height=1, width=15,
                                font=("arial", 12)).grid(row=7, column=0)
    frame2.grid(row=1, column=0)
def Check_Availiable(roomType):
    avail_rooms = get_availiable_rooms()
    avail = False
    for x in avail_rooms:
        if x[1] == roomType:
            avail = True
            tempRoom = x[0]

    if avail:
        window = Toplevel()
        label = Label(window, text="Room " + str(tempRoom) + " Avaliable")
        label.pack(side="top", fill="x", padx=20, pady=20)
        button_close = Button(window, text="Close", command=window.destroy)
        button_close.pack()
        window.mainloop()

def Check_Reservations():
    clear(frame2)
    reservations = get_reservations()
    lGuestFirstName = Label(frame2, text="Guest First Name", font=("arial", 12), height=2).grid(row=1, column=0)
    lGuestLastName = Label(frame2, text="Guest Last Name", font=("arial", 12), height=2).grid(row=1, column=1)
    lCheckInDate = Label(frame2, text='Check In Date', font=("arial", 12)).grid(row=1, column=2)
    lCheckOutDate = Label(frame2, text='Check Out Date', font=("arial", 12)).grid(row=1, column=3)
    lRoomType = Label(frame2, text='Room Type', font=("arial", 12)).grid(row=1, column=4)

    i = 0
    j = 0
    for x in reservations:

        j = 0
        for y in reservations[i]:

            reserved = Label(frame2, text=str(reservations[i][j]), font=("arial", 12))
            reserved.grid(row=i + 2, column=j)
            j += 1
        i += 1
    frame2.grid(row=1, column=0, sticky='nwse')
	
	
#Capability 5
def update(Guest_Id):
    results = update_guest(Guest_Id)

def edit(Guest_Id):
    Edit = Tk()
    Edit.title("Edit Record")
    Edit.geometry("700x700")
    result = get_guest(Guest_Id)
    #print(result[0][1])
    #print(result)

    label1 = Label(Edit, text="First Name:", font=("arial", 12), height=2 )
    label1.grid(row=1, column=0)
    label2 = Label(Edit, text="Last Name:", font=("arial", 12), height=2 )
    label2.grid(row=2, column=0)
    label3 = Label(Edit, text="Phone:", font=("arial", 12), height=2 )
    label3.grid(row=3, column=0)
    label4 = Label(Edit, text="ID info(State,ID#)", font=("arial", 12), height=2 )
    label4.grid(row=4, column=0)
    label5 = Label(Edit, text="Vehicle License Plate", font=("arial", 12), height=2 )
    label5.grid(row=5, column=0)
    label6 = Label(Edit, text="E-mail", font=("arial", 12), height=2 )
    label6.grid(row=6, column=0)
    label7 = Label(Edit, text="Address", font=("arial", 12), height=2 )
    label7.grid(row=7, column=0)

    fname = Entry(Edit, font = ("arial", 12))
    fname.grid(row=1,column=1)
    fname.insert(0, result[0][1])
    lname = Entry(Edit,  font = ("arial", 12))
    lname.grid(row=2,column=1)
    lname.insert(0, result[0][2])
    phone = Entry(Edit,  font = ("arial", 12))
    phone.grid(row=3,column=1)
    phone.insert(0, result[0][3])
    address = Entry(Edit,  font = ("arial", 12))
    address.grid(row=4,column=1)
    address.insert(0, result[0][4])
    email = Entry(Edit,  font = ("arial", 12))
    email.grid(row=5,column=1)
    email.insert(0, result[0][5])
    state_id = Entry(Edit,  font = ("arial", 12))
    state_id .grid(row=6,column=1)
    state_id.insert(0, result[0][6])
    license_number = Entry(Edit,  font = ("arial", 12))
    license_number.grid(row=7,column=1)
    license_number.insert(0, result[0][7])


    Button3 = Button(Edit, text='Update', command=update(Guest_Id), font=("arial", 14)).grid(row=8, column=1)
  

def GuestProfile(Guest_Id = None):
    #print(Guest_Id)
    result = get_guest(Guest_Id)
    #print(result)
    clear(frame2)
    
    
    #Guest
    Guestlabel = Label(frame2, text="Guest Profile", font=("arial", 20), height=2)
    Guestlabel.grid(row= 1 , column = 1)
   
    #Customer Information
    label1 = Label(frame2, text="First Name:", font=("arial", 12), height=2 )
    label1.grid(row=2, column=0)
    label2 = Label(frame2, text="Last Name:", font=("arial", 12), height=2 )
    label2.grid(row=3, column=0)
    label3 = Label(frame2, text="Phone:", font=("arial", 12), height=2 )
    label3.grid(row=4, column=0)
    label4 = Label(frame2, text="ID info(State,ID#)", font=("arial", 12), height=2 )
    label4.grid(row=5, column=0)
    label5 = Label(frame2, text="Vehicle License Plate", font=("arial", 12), height=2 )
    label5.grid(row=6, column=0)
    label6 = Label(frame2, text="E-mail", font=("arial", 12), height=2 )
    label6.grid(row=7, column=0)
    label7 = Label(frame2, text="Address", font=("arial", 12), height=2 )
    label7.grid(row=8, column=0)
 
    
    #Guest1
    name = Label(frame2, text=result[0][1], font=("arial", 12), height=2)
    name.grid(row=2,column=1)
    lname = Label(frame2, text=result[0][2], font=("arial", 12), height=2)
    lname.grid(row=3,column=1)
    phone = Label(frame2, text=result[0][3], font=("arial", 12), height=2)
    phone.grid(row=4,column=1)
    id_info = Label(frame2, text=result[0][4], font=("arial", 12), height=2)
    id_info.grid(row=5,column=1)
    vehicle_license = Label(frame2, text=result[0][5], font=("arial", 12), height=2)
    vehicle_license.grid(row=6,column=1)
    email = Label(frame2, text=result[0][6], font=("arial", 12), height=2)
    email.grid(row=7,column=1)
    address = Label(frame2, text=result[0][7], font=("arial", 12), height=2)
    address.grid(row=8,column=1)

    Button2 = Button(frame2, text='Edit', command=edit(Guest_Id), font=("arial", 14))
    Button2.grid(row=9, column = 1)

#Capability 6
def edit2():
    return

def CurrentStay():
    #need booking, guest, payment, rooms table
    clear(frame2)
    result = get_booking()
    result2 = get_guest_1()
    result3 = get_payment()
    result4 = get_rooms()
    #result2 = get_guest()
    #print(result)
    #print(result3)
    #print(result4)
    Guestlabel = Label(frame2, text="Current Stay", font=("arial", 20), height=2)
    Guestlabel.grid(row= 1 , column = 1)
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
    guest1 = Entry(frame2,  font = ("arial", 12))
    guest1.grid(row=2,column=1)
    guest1.insert(0, result2[0][1])
    checkin1 = Entry(frame2,  font = ("arial", 12))
    checkin1.grid(row=3,column=1)
    checkin1.insert(0, result[0][3])
    checkout1 = Entry(frame2,  font = ("arial", 12))
    checkout1.grid(row=4,column=1)
    checkout1.insert(0, result[0][4])
    roomtype1 = Entry(frame2,  font = ("arial", 12))
    roomtype1.grid(row=5,column=1)
    roomtype1.insert(0, result4[0][1])
    roomnum1 = Entry(frame2,  font = ("arial", 12))
    roomnum1.grid(row=6,column=1)
    roomnum1.insert(0, result4[0][0])
    roomrate1 = Entry(frame2,  font = ("arial", 12))
    roomrate1.grid(row=7,column=1)
    roomrate1.insert(0, result4[0][3])
    totalcharge1 = Entry(frame2,  font = ("arial", 12))
    totalcharge1.grid(row=8,column=1)
    totalcharge1.insert(0, result[0][6])
    paymentsmade1 = Entry(frame2,  font = ("arial", 12))
    paymentsmade1.grid(row=9,column=1)
    paymentsmade1.insert(0, result3[0][6])
    balance1 = Entry(frame2,  font = ("arial", 12))
    balance1.grid(row=10,column=1)
    balance1.insert(0, 0)

    Button2 = Button(frame2, text='Edit', command=edit2(), font=("arial", 14))
    Button2.grid(row=11, column = 1)
    Button3 = Button(frame2, text="Look up Guest", command= lambda: GuestProfile(1),font = ("arial", 15))
    Button3.grid(row=12, column=1)




Capability1 = Button(frame1, text='Show Rooms and Status', command=ShowRooms, font=("arial", 12), width=20, height=5)
Capability1.grid(row=0, column=0)
Capability2 = Button(frame1, text='Show Room Availability', command=roomSchedule, font=("arial", 12), width=20, height=5)
Capability2.grid(row=0, column=1)
Capability3 = Button(frame1, text='Customer Reservation', command=Customer_Reservation, font=("arial", 12), width=20, height=5)
Capability3.grid(row=0, column=2)
Capability4 = Button(frame1, text='Housekeeping', command=housekeeping, font=("arial", 12), width=20, height=5)
Capability4.grid(row=0, column=3)
Capability5 = Button(frame1, text='Guest Profile', command=GuestProfile,font=("arial", 12), width=20,height=5)
Capability5.grid(row = 0, column=4)
Capability6 = Button(frame1, text='Current Stay', command=CurrentStay,font=("arial", 12), width=20,height=5)
Capability6.grid(row = 0, column=5)
Capability7 = Button(frame1, text='Search', command=Search, font=("arial", 12), width=20, height=5)
Capability7.grid(row=0, column=6)
Capability8 = Button(frame1, text='Daily Report', command=report, font=("arial", 12), width=20, height=5)
Capability8.grid(row=0, column=7)
frame1.grid(row=0, column=0)

root.mainloop()
