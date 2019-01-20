import sqlite3
import csv
import os

db_file = 'inventory.sqlite'

# Connecting to the database file.
def connect_db():
    conn = sqlite3.connect(db_file)
    return conn

# Create table
def create_table():
    try:
        conn = connect_db()
        c = conn.cursor()
        create_query = '''CREATE TABLE PRODUCTS
           (TITLE           VARCHAR(100)    NOT NULL,
           PRICE            DOUBLE,
           INV_COUNT        INT);'''

        c.execute(create_query)
        conn.commit()
    except sqlite3.Error as e:
        print( "SQL error encountered when creating table: \n" + e.args[0])
    finally:
        if conn:
            conn.close()

# Insert data from csv into table
def insert_table():
    try:
        conn = connect_db()
        c = conn.cursor()
        with open('inventory.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')

            for row in reader:
                #print(row)
                c.execute("INSERT INTO PRODUCTS  VALUES( ?, ?, ? )", (row['TITLE'], row['PRICE'], row['INV_COUNT']));

        conn.commit()
    except sqlite3.Error as e:
        # Messages should be logged. Printed here for the project.
        print( "SQL error encountered when inserting into table: \n" + e.args[0])
    finally:
        if conn:
            conn.close()

def select_from_table(query):
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
    except sqlite3.Error as e:
        # Messages should be logged. Printed here for the project.
        print( "SQL error encountered when selecting from table: \n" + e.args[0])
        raise
    finally:
        if conn:
            conn.close()

    return rows

# Update Table
def update_table(query):
    flag = "Success"
    try:
        conn = connect_db()
        c = conn.cursor()

        c.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        # Messages should be logged. Printed here for the project.
        print( "SQL error encountered when updating table: \n" + e.args[0])
        flag = "Fail"
    finally:
        if conn:
            conn.close()

    return flag

if not os.path.isfile(db_file):
    conn = connect_db()
    create_table()
    insert_table()

