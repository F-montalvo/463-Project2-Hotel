from tkinter import *
import random
from tkinter import ttk
from filldb import create_connection, get_type, get_status, get_housekeeping, get_availiable_rooms, get_reservations
from tkinter.messagebox import showinfo
# download the file in command prompt go to where the file is located use python example.py

root = Tk()
# This sets the size of th window
root.geometry('1250x700')
# This sets up the Title of the Window
root.title("Hotel Transylvania")
root.resizable(False, False)

frame1 = Frame(root)
frame2 = Frame(root)
roomlist = []
schedulelist = []
dirtyrooms = []

class Room:
    def __init__(self, root, i, lock):
        # size = ["King","Double Queen","Double Queen with Kitchen", "Suite"]
        availability = {"Available": "green", "Unavailable/Occupied": "red", "Unavailable/Dirty": "blue",
                        "Unavailable/Maintenance": "purple"}
        # key = ["Available","Unavailable/Occupied", "Unavailable/Dirty","Unavailable/Maintenance"]
        conn = create_connection()
        self.avail = get_status(conn, i + 1)
        self.roomsize = get_type(conn, i + 1)
        conn.close()
        self.color = availability.get(self.avail)
        self.schedule = ["None", "Occupied"]
        self.week = [self.schedule[random.randint(0, 1)], self.schedule[random.randint(0, 1)],
                     self.schedule[random.randint(0, 1)], self.schedule[random.randint(0, 1)],
                     self.schedule[random.randint(0, 1)], self.schedule[random.randint(0, 1)],
                     self.schedule[random.randint(0, 1)]]
        self.root = root
        if lock == 1:
            roomlist.append(Button(self.root, text="Room #" + str(i + 1) + ' ' + self.roomsize,
                                   command=lambda: checkRoom(self, roomlist, i), font=("arial", 12)))
        if lock == 2:
            roomlist.append(Label(self.root, text="Room #" + str(i + 1) + ' ' + self.roomsize, font=("arial", 12)))
            for item in self.week:
                schedulelist.append(Label(self.root, text=item, font=("arial,12")))

    def configure(self, i):
        roomlist[i].configure(fg=self.color)


def clear(frame):
    roomlist.clear()
    schedulelist.clear()
    for widget in frame.winfo_children():
        widget.destroy()


# Capability1
def ShowRooms():
    clear(frame2)
    legend = Label(frame2, text="Available", font=("arial", 18))
    legend.configure(fg="green")
    legend2 = Label(frame2, text="Unavailable/Occupied", font=("arial", 18))
    legend2.configure(fg="red")
    legend3 = Label(frame2, text="Unavailable/Dirty", font=("arial", 18))
    legend3.configure(fg="blue")
    legend4 = Label(frame2, text="Unavailable/Maintenance", font=("arial", 18))
    legend4.configure(fg="purple")

    legend.grid(row=1, column=0)
    legend2.grid(row=1, column=1)
    legend3.grid(row=1, column=2)
    legend4.grid(row=1, column=3)

    rowcounter = 2
    counter = 0
    i = 0
    while i < 20:
        Room(frame2, i, 2)

        if counter > 3:
            counter = 0
            rowcounter = rowcounter + 1
        roomlist[i].grid(row=rowcounter, column=counter)
        counter = counter + 1
        i = i + 1
    frame2.grid(row=1, column=0, sticky='nwse')


def checkRoom(self, rooms, counter):
    self.configure(counter)


# Capability2
def roomSchedule():
    clear(frame2)
    # scrollbar = Scrollbar(frame2)
    # scrollbar.grid(row = 1, column = 0, sticky = "NWS")

    monday = Label(frame2, text="Monday", font=("arial", 14))
    tuesday = Label(frame2, text="Tuesday", font=("arial", 14))
    wednesday = Label(frame2, text="Wednesday", font=("arial", 14))
    thursday = Label(frame2, text="Thursday", font=("arial", 14))
    friday = Label(frame2, text="Friday", font=("arial", 14))
    saturday = Label(frame2, text="Saturday", font=("arial", 14))
    sunday = Label(frame2, text="Sunday", font=("arial", 14))

    monday.grid(row=1, column=2)
    tuesday.grid(row=1, column=3)
    wednesday.grid(row=1, column=4)
    thursday.grid(row=1, column=5)
    friday.grid(row=1, column=6)
    saturday.grid(row=1, column=7)
    sunday.grid(row=1, column=8)

    rowcounter = 2
    counter = 1
    i = 0
    while i < 20:
        Room(frame2, i, 2)
        roomlist[i].grid(row=i + rowcounter, column=0)
        i = i + 1
    j = 0
    while j < len(schedulelist):
        if j % 7 == 0 and j != 0:
            rowcounter = rowcounter + 1
            counter = 1
        schedulelist[j].grid(row=rowcounter, column=counter + 1)
        j = j + 1
        counter = counter + 1
    frame2.grid(row=1, column=0, sticky='wsne')


def execute():
    print("welcome")


# Capability 7
def Search():
    clear(frame2)
    label1 = Label(frame2, text="Guest First Name", font=("arial", 12), height=2).grid(row=0, column=0)
    FirstName = Entry(frame2, font=("arial", 12)).grid(row=0, column=1)
    label2 = Label(frame2, text="Guest Last Name", font=("arial", 12), height=2).grid(row=0, column=2)
    LastName = Entry(frame2, font=("arial", 12)).grid(row=0, column=3)
    label3 = Label(frame2, text="Room Number", font=("arial", 12), height=2).grid(row=0, column=4)
    Room = Entry(frame2, font=("arial", 12)).grid(row=0, column=5)
    label4 = Label(frame2, text="Phone Number", font=("arial", 12), height=2).grid(row=0, column=6)
    Phone = Entry(frame2, font=("arial", 12)).grid(row=0, column=7)
    label5 = Label(frame2, text="Street Address", font=("arial", 12), height=2).grid(row=1, column=0)
    Address = Entry(frame2, font=("arial", 12)).grid(row=1, column=1)
    label5 = Label(frame2, text="Check In Date", font=("arial", 12), height=2).grid(row=1, column=2)
    CheckIn = Entry(frame2, font=("arial", 12)).grid(row=1, column=3)
    label6 = Label(frame2, text="Check Out Date", font=("arial", 12), height=2).grid(row=1, column=4)
    CheckOut = Entry(frame2, font=("arial", 12)).grid(row=1, column=5)
    Button1 = Button(frame2, text='Search', font=("arial", 14)).grid(row=1, column=6)
    frame2.grid(row=1, column=0)


# Capability 8
def report():
    clear(frame2)

    label1 = Label(frame2, text="Today's report", font=("arial", 20), height=2).grid(row=0, column=0)
    hRoomNum = Label(frame2, text="Room Number", font=("arial", 12), height=2).grid(row=1, column=0)
    hHousekeeper = Label(frame2, text="Guest Name", font=("arial", 12), height=2).grid(row=1, column=1)
    hRoomStatus = Label(frame2, text="Check In Date", font=("arial", 12), height=2).grid(row=1, column=2)
    hRoomType = Label(frame2, text="Check out Date", font=("arial", 12), height=2).grid(row=1, column=3)
    hBathroom = Label(frame2, text="Amount", font=("arial", 12), height=2).grid(row=1, column=4)

    for i in range(2, 8):
        for j in range(5):
            b = Entry(frame2, text="------")
            b.grid(row=i, column=j)
    frame2.grid(row=1, column=0)

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

    for rooms in dirtyrooms:
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

# Capability 5
def search():
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    search = Tk()
    search.title("Search")
    search.geometry("900x800")

    def update():
        return
    def edit_now(id, index):
        sql2 = "SELECT * FROM Guest WHERE Guest_Id = ?"
        name2 = id 
        result2 = c.execute(sql2, name2)
        result2 = c.fetchall()
        print(result2)


        index += 1
        fname_label = Label(search, text="First Name:", font=("arial", 12), height=2 ).grid(row=index+1, column=0)
        lname_label = Label(search, text="Last Name:", font=("arial", 12), height=2 ).grid(row=index+2, column=0)
        phone_label = Label(search, text="Phone:", font=("arial", 12), height=2 ).grid(row=index+3, column=0)
        sid_label = Label(search, text="Address", font=("arial", 12), height=2 ).grid(row=index+4, column=0)
        license_label = Label(search, text="E-mail", font=("arial", 12), height=2 ).grid(row=index+5, column=0)
        email_label = Label(search, text="ID info(State,ID#)", font=("arial", 12), height=2 ).grid(row=index+6, column=0)
        address_label = Label(search, text="Vehicle License Plate", font=("arial", 12), height=2 ).grid(row=index+7, column=0)
        id_label = Label(search, text="id", font=("arial", 12), height=2 ).grid(row=index+8, column=0)

    
        name = Entry(search,  font = ("arial", 12)).grid(row=index+1,column=1)
        name.insert(0, result2[0][1])
        lname = Entry(search,  font = ("arial", 12)).grid(row=index+2,column=1)
        lname.insert(0, result2[0][2])
        phone = Entry(search,  font = ("arial", 12)).grid(row=index+3,column=1)
        phone.insert(0, result2[0][3])
        sid = Entry(search,  font = ("arial", 12)).grid(row=index+4,column=1)
        sid.insert(0, result2[0][3])
        license = Entry(search,  font = ("arial", 12)).grid(row=index+5,column=1)
        license.insert(0 ,result2[0][4])
        email = Entry(search,  font = ("arial", 12)).grid(row=index+6,column=1)
        email.insert(0, result2[0][5])
        address = Entry(search,  font = ("arial", 12)).grid(row=index+7,column=1)
        address.insert(0, result2[0][6])
        id = Entry(search,  font = ("arial", 12)).grid(row=index+8,column=1)
        id.insert(0, result2[0][0])

        update_customer = Button(search, text="Update", command=update)
        update_customer.grid(row=index+10, column=2)

        search.grid(row=1,column=0)

    def search_now():
        conn = sqlite3.connect("hotel.db")
        c = conn.cursor()
        searched = search_box.get()
        lname = last_name.get()
        sql = "SELECT * FROM Guest WHERE First_Name = ? AND Last_Name = ?"
        first_name = (searched, lname )
        result = c.execute(sql, first_name)
        result = c.fetchall()

        if not result:
            result = "Not found"
        else:
            for index, x in enumerate(result):
                num = 0
                index += 2
                id_reference = str(x[0])
                edit_button= Button(search, text="Edit", command=lambda: edit_now(id_reference, index))
                edit_button.grid(row=index, column=num)
                for y in x:
                    searched_label = Label(search, text=y)
                    searched_label.grid(row=index, column = num+1)
                    num += 1


    #Search Entry 
    search_box = Entry(search)
    search_box.grid(row=0, column=1)
    last_name = Entry(search)
    last_name.grid(row=1, column=1)
    #Search Entry label
    search_box_label = Label(search, text="First name")
    search_box_label.grid(row=0, column = 0)
    search_box_label = Label(search, text="Last name")
    search_box_label.grid(row=1, column = 0)
    #Search Entry button
    search_button = Button(search, text="Search Guest", command=search_now)
    search_button.grid(row=3, column=0)

# Capability 6
def GuestInfo():
    clear(frame2)
    Guestlabel = Label(frame2, text="Guest1", font=("arial", 12), height=2).grid(row=1, column=1)
    Guestlabel2 = Label(frame2, text="Guest2", font=("arial", 12), height=2).grid(row=1, column=2)
    Guestlabel3 = Label(frame2, text="Guest3", font=("arial", 12), height=2).grid(row=1, column=3)
    # Customer Information
    label1 = Label(frame2, text="Guest Name:", font=("arial", 12), height=2).grid(row=2, column=0)

    label2 = Label(frame2, text="Check In Date and Time", font=("arial", 12), height=2).grid(row=3, column=0)

    label3 = Label(frame2, text="Expected Check Out Date and Time", font=("arial", 12), height=2).grid(row=4, column=0)

    label4 = Label(frame2, text="Room Type", font=("arial", 12), height=2).grid(row=5, column=0)

    label5 = Label(frame2, text="Room Number", font=("arial", 12), height=2).grid(row=6, column=0)

    label6 = Label(frame2, text="Room Rate ($/Day", font=("arial", 12), height=2).grid(row=7, column=0)

    label7 = Label(frame2, text="Total Charge", font=("arial", 12), height=2).grid(row=8, column=0)

    label8 = Label(frame2, text="Payments Made", font=("arial", 12), height=2).grid(row=9, column=0)

    label9 = Label(frame2, text="Balance", font=("arial", 12), height=2).grid(row=10, column=0)

    # Guest1
    guest1 = Entry(frame2, font=("arial", 12)).grid(row=2, column=1)
    checkin1 = Entry(frame2, font=("arial", 12)).grid(row=3, column=1)
    checkout1 = Entry(frame2, font=("arial", 12)).grid(row=4, column=1)
    roomtype1 = Entry(frame2, font=("arial", 12)).grid(row=5, column=1)
    roomnum1 = Entry(frame2, font=("arial", 12)).grid(row=6, column=1)
    roomrate1 = Entry(frame2, font=("arial", 12)).grid(row=7, column=1)
    totalcharge1 = Entry(frame2, font=("arial", 12)).grid(row=8, column=1)
    paymentsmade1 = Entry(frame2, font=("arial", 12)).grid(row=9, column=1)
    balance1 = Entry(frame2, font=("arial", 12)).grid(row=10, column=1)

    # Guest2
    guest2 = Entry(frame2, font=("arial", 12)).grid(row=2, column=2)
    checkin2 = Entry(frame2, font=("arial", 12)).grid(row=3, column=2)
    checkout2 = Entry(frame2, font=("arial", 12)).grid(row=4, column=2)
    roomtype2 = Entry(frame2, font=("arial", 12)).grid(row=5, column=2)
    roomnum2 = Entry(frame2, font=("arial", 12)).grid(row=6, column=2)
    roomrate2 = Entry(frame2, font=("arial", 12)).grid(row=7, column=2)
    totalcharge2 = Entry(frame2, font=("arial", 12)).grid(row=8, column=2)
    paymentsmade2 = Entry(frame2, font=("arial", 12)).grid(row=9, column=2)
    balance2 = Entry(frame2, font=("arial", 12)).grid(row=10, column=2)

    # Guest3
    guest3 = Entry(frame2, font=("arial", 12)).grid(row=2, column=3)
    checkin3 = Entry(frame2, font=("arial", 12)).grid(row=3, column=3)
    checkout3 = Entry(frame2, font=("arial", 12)).grid(row=4, column=3)
    roomtype3 = Entry(frame2, font=("arial", 12)).grid(row=5, column=3)
    roomnum3 = Entry(frame2, font=("arial", 12)).grid(row=6, column=3)
    roomrate3 = Entry(frame2, font=("arial", 12)).grid(row=7, column=3)
    totalcharge3 = Entry(frame2, font=("arial", 12)).grid(row=8, column=3)
    paymentsmade3 = Entry(frame2, font=("arial", 12)).grid(row=9, column=3)
    balance3 = Entry(frame2, font=("arial", 12)).grid(row=10, column=3)
    frame2.grid(row=1, column=0)


Capability1 = Button(frame1, text='Show Rooms and Status', command=ShowRooms, font=("arial", 12), width=20, height=5)
Capability1.grid(row=0, column=0)
Capability2 = Button(frame1, text='Show Room Availability', command=roomSchedule, font=("arial", 12), width=20,
                     height=5)
Capability2.grid(row=0, column=1)
Capability3 = Button(frame1, text='Customer Reservation', command=Customer_Reservation, font=("arial", 12), width=20,
                     height=5)
Capability3.grid(row=0, column=2)
Capability4 = Button(frame1, text='Housekeeping', command=housekeeping, font=("arial", 12), width=20, height=5)
Capability4.grid(row=0, column=3)
Capability5 = Button(frame1, text='Guest Profile', command=GuestProfile, font=("arial", 12), width=20, height=5)
Capability5.grid(row=0, column=4)
Capability6 = Button(frame1, text='Current Stay', command=GuestInfo, font=("arial", 12), width=20, height=5)
Capability6.grid(row=0, column=5)
Capability7 = Button(frame1, text='Search', command=Search, font=("arial", 12), width=20, height=5)
Capability7.grid(row=0, column=6)
Capability8 = Button(frame1, text='Daily Report', command=report, font=("arial", 12), width=20, height=5)
Capability8.grid(row=0, column=7)
frame1.grid(row=0, column=0)

root.mainloop()
