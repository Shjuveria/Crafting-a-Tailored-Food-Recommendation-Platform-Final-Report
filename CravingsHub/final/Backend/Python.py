import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\irfan\Desktop\CravingsHut All-files\final\Database.accdb;')
cursor = conn.cursor()
cursor.execute('select * from Breakfast')
cursor.execute('select * from Lunch')
cursor.execute('select * from Dinner')
cursor.execute('select * from Beverages')

   
for row in cursor.fetchall():
    print (row)

import tkinter as tk

HEIGHT = 600
WIDTH = 700

root = tk.Tk()
tk.Tk.title(root, "Cravings Hub")


def button_1_clicked(first_name_entry, last_name_entry, username_entry, password_entry, reenter_password_entry):
    final_str = 'First Name: %s \nLast Name: %s \nUsername: %s \nPassword: %s \nRe-Enter Password:%s' % (
        first_name_entry, last_name_entry, username_entry, password_entry, reenter_password_entry)
    print(final_str)


def clicked():
    print("function works")
