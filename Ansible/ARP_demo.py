import tkinter as tk
import mysql.connector
from tkinter import *


'''def submitact():
    user = Username.get()
    passw = password.get()

    print(f"The name entered by you is {user} {passw}")

    logintodb(user, passw)


def logintodb(user, passw):
    # If password is enetered by the
    # user
    if passw:
        db = mysql.connector.connect(host="localhost",
                                     user=root,
                                     password=root,
                                     db="db_student")
        cursor = db.cursor()

    # If no password is enetered by the
    # user
    else:
        db = mysql.connector.connect(host="localhost",
                                     user=root,
                                     db="db_student")
        cursor = db.cursor()

    # A Table in the database
    savequery = "select * from STUDENT"

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Executed successfully")

    except:
        db.rollback()
        print("Error occurred")

'''
root = tk.Tk()
root.geometry("500x600")
root.title("Registration Form")

# Defining the first row
lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.grid(row=0,column=1)

Username = tk.Entry(root, width=20)
Username.grid(row=0, column=2)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.grid(row=1,column=1)

password = tk.Entry(root, width=20)
password.grid(row=1,column=2)

submitbtn = tk.Button(root, text="Login")
submitbtn.grid(row=2,column=2)

root.mainloop()
