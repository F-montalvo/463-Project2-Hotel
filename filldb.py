import sqlite3
from sqlite3 import Error
import random


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("hotel.db")
    except Error as e:
        print(e)

    return conn


def create_room(conn, data):
    statement = "insert into Rooms(Number,Type,Status,Rate)VALUES(?,?,?,?)"
    cur = conn.cursor()
    cur.execute(statement, data)
    conn.commit()
    return cur.lastrowid


def get_type(conn, i):
    cur = conn.cursor()
    statement = "select Type from Rooms where Number = {0}".format(i)
    cur.execute(statement)
    data = cur.fetchall()
    return data[0][0]


def get_status(conn, i):
    cur = conn.cursor()
    statement = "select Status from Rooms where Number = {}".format(i)
    cur.execute(statement)
    data = cur.fetchall()
    return data[0][0]


def get_report_data():
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT B.Room_number, G.First_name|| ' '||G.Last_name, B.CheckIn, B.CheckOut, sum(P.Payment_amount) from Booking as B JOIN Guest as G on B.Guest_Id = G.Guest_Id JOIN Payment as P on P.Booking_id= B.Booking_id WHERE P.Payment_date = date('now') GROUP by P.Booking_id;"
    cur.execute(statement)
    data = cur.fetchall()
    conn.close()
    return data


def get_housekeeping():
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT * from Housekeeping"
    cur.execute(statement)
    data = cur.fetchall()
    return data

def get_availiable_rooms():
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT * from Rooms as R where R.Status = 'Available'"
    cur.execute(statement)
    data = cur.fetchall()
    return data

def get_reservations():
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT G.First_name, G.Last_name, B.CheckIn, B.CheckOut, R.Type from Booking as B join Guest as G on B.Guest_Id = G.Guest_Id join Rooms as R on R.number = B.room_number"
    cur.execute(statement)
    data = cur.fetchall()
    return data

# Capability 5-6
def get_guest(Guest_Id):
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT * FROM Guest WHERE Guest_Id = " + str(Guest_Id)
    cur.execute(statement)
    data = cur.fetchall()
    conn.close()
    return data

def update_guest(Guest_Id):
    conn = create_connection()
    cur = conn.cursor()
    statement = "UPDATE Guest SET First_Name = :first, Last_Name = :last, Phone = :phone, State_Id = :state_id, License_plate = :license_plate, Email = :email  Address = :address,   WHERE Guest_Id =" + str(Guest_Id)
    conn.commit()
    data = cur.fetchall()
    conn.close()
    return data

def get_booking():
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT * FROM Booking WHERE Guest_Id = 1"
    cur.execute(statement)
    data = cur.fetchall()
    conn.close()
    return data

def get_guest_1():
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT * FROM Guest WHERE Guest_Id = 1" 
    cur.execute(statement)
    data = cur.fetchall()
    conn.close()
    return data

def get_payment():
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT * FROM Booking WHERE Booking_id= 2" 
    cur.execute(statement)
    data = cur.fetchall()
    conn.close()
    return data

def get_rooms():
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT * FROM Rooms WHERE Number= 6" 
    cur.execute(statement)
    data = cur.fetchall()
    conn.close()
    return data
#CAP 7 & 8
def get_report_data():
    conn = create_connection()
    cur = conn.cursor()
    statement = "SELECT B.Room_number, G.First_name|| ' '||G.Last_name, B.CheckIn, B.CheckOut, sum(P.Payment_amount) from Booking as B JOIN Guest as G on B.Guest_Id = G.Guest_Id JOIN Payment as P on P.Booking_id= B.Booking_id WHERE P.Payment_date = date('now') GROUP by P.Booking_id;"
    cur.execute(statement)
    data = cur.fetchall()
    conn.close()
    return data

def search_data(FirstName,LastName,Room,Phone,Address,CheckIn,CheckOut):
    '''
    Select G.First_name, G.Last_name, B.Room_number, B.CheckIn, B.CheckOut from Booking as B
JOIN Guest AS G ON B.Guest_Id = G.Guest_Id
where G.First_name = 'Dhruv' and G.Last_name = 'Patel' and B.Room_number=6 and G.Phone = 1231231234 and G.Address Like '%CA%' and B.CheckIn='2021-05-02' and B.CheckOut='2021-05-03';
    '''
    statement = "Select G.First_name, G.Last_name, B.Room_number, B.CheckIn, B.CheckOut,B.Guest_Id from Booking as B JOIN Guest AS G ON B.Guest_Id = G.Guest_Id "
    if FirstName or LastName or Room or Phone or Address or CheckIn or CheckOut:
        statement+= "where"
    else:
        return None
    if FirstName:
        statement+= " lower(G.First_name) = lower('" +str(FirstName) + str("') and")
    if LastName:
        statement+=" G.Last_name = '" +str(LastName) + str("' and")
    if Room:
        statement+=" B.Room_number = '"+ str(Room) + str("' and")
    if Phone:
        statement+=" G.Phone = '" +str(Phone)+ str("' and")
    if Address:
        statement+=" lower(G.Address) Like lower("+str("'%")+str(Address)+str("%')") + str(" and")
    if CheckIn:
        statement+=" B.CheckIn = '"+str(CheckIn) +str("' and")
    if CheckOut:
        statement+=" B.CheckOut = '"+str(CheckOut) + str("' and")
    if statement.endswith('and'):
        run_statement = statement[:len(statement)-3]
    run_statement+=' ;'
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(run_statement)
    data = cur.fetchall()
    conn.close()
    return data
def main():
    size = ["King", "Double Queen", "Double Queen with Kitchen", "Suite"]
    key = ["Available", "Unavailable/Occupied", "Unavailable/Dirty", "Unavailable/Maintenance"]

    conn = create_connection()
    '''
    with conn:
        for i in range(1,21):
            data = (i,size[random.randint(0,3)],key[random.randint(0,3)],0.0)
            create_room(conn,data)
    '''
    


if __name__ == '__main__':
    main()
