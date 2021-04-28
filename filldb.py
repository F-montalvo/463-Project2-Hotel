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

def create_room(conn,data):
    statement = "insert into Rooms(Number,Type,Status,Rate)VALUES(?,?,?,?)"
    cur = conn.cursor()
    cur.execute(statement,data)
    conn.commit()
    return cur.lastrowid

def get_type(conn,i):
    cur = conn.cursor()
    statement = "select Type from Rooms where Number = {0}".format(i)
    cur.execute(statement)
    data = cur.fetchall()
    return data[0][0]

def get_status(conn,i):
    cur = conn.cursor()
    statement = "select Status from Rooms where Number = {}".format(i)
    cur.execute(statement)
    data = cur.fetchall()
    return data[0][0]



def main():


    size = ["King","Double Queen","Double Queen with Kitchen", "Suite"]
    key = ["Available","Unavailable/Occupied", "Unavailable/Dirty","Unavailable/Maintenance"]

    conn = create_connection()
    with conn:
        for i in range(1,21):
            data = (i,size[random.randint(0,3)],key[random.randint(0,3)],0.0)
            create_room(conn,data)


if __name__ == '__main__':
    main()
