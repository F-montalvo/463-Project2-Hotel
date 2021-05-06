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
    statement = "SELECT * from Reservations"
    cur.execute(statement)
    data = cur.fetchall()
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
    print(len(get_report(conn)))


if __name__ == '__main__':
    main()
