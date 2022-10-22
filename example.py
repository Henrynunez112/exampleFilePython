import csv
import hashlib
from tkinter import *


def check_database(dict):
    with open('file.csv', 'r', newline='') as database:
        read = csv.DictReader(database)
        print(dict)
        for row in read:
            print(dict)
            print(row['username'], row['hash'])
            print('nothing')


def create_db():
    try:
        columns = ['username', 'hash']
        with open('file.csv', 'x', newline='') as database:
            mywrite = csv.DictWriter(database, columns)
    except FileExistsError:
        print("Database has been previously created...")


def hash_value(wx, hvalue):
    encoded_value = hashlib.sha256(str.encode(hvalue))
    result = encoded_value.hexdigest()
    Label(wx, text=result).pack(pady=140)
    return result

# get username and password value


def display_delete(wx, uf, pf):
    usernvalue, passvalue = get_values(uf, pf)
    Label(wx, text=usernvalue).pack()
    Label(wx, text=passvalue).pack()
    uf.delete(0, 'end')
    pf.delete(0, 'end')
    hashed_value = hash_value(wx, passvalue)
    print("creating database...")
    create_db()
    my_dictionary = {"username": usernvalue, "hash": hashed_value}
    check_database(my_dictionary)


# get the values
def get_values(u, p):
    uvalue = u.get()
    pvalue = p.get()
    return uvalue, pvalue


def create_window():
    # main window
    window = Tk()
    window.title("Login Window")
    # window labels
    lbl1 = Label(text='Username:').place(x=100, y=50)
    lbl2 = Label(text='Password:').place(x=100, y=80)
    # window fields
    usrname_fld = Entry(bd=5)
    pswd_fld = Entry(bd=5, show='*')
    usrname_fld.place(x=200, y=50)
    pswd_fld.place(x=200, y=80)
    button = Button(text="Enter", command=lambda: display_delete(
        window, usrname_fld, pswd_fld))
    button.place(x=265, y=125)
    # window background color
    window.config(background="green")
    # main window size
    window.geometry("500x500")
    window.mainloop()


create_window()
