from tkinter import *
import tkinter.messagebox
import hashlib
import csv

#check for usernames in the databse
def check_db(usernvalue,hashed_value):
    print("checking DB...")
    with open('file.csv','r',newline='') as database:
        read = csv.DictReader(database)
        for row in read:
            if usernvalue in row['username'] and hashed_value in row['hash']:
                print('successul login')
                tkinter.messagebox.showinfo(title='Info', message='Successful Login')
                return True
            elif usernvalue in row['username'] and hashed_value not in row['hash']:
                print('wrong password')
                tkinter.messagebox.showerror(title='Info', message='Wrong Password, Please try again')
                return True

#add Creds to Database
def add_db_data(my_dictionary):
    columns=['username','hash']
    with open('file.csv','a',newline='') as database:
        write = csv.DictWriter(database,columns)
        write.writerow(my_dictionary)

#Database already exists, check if it is empty
def is_db_empty():
    with open('file.csv','r',newline='') as database:
        read = csv.DictReader(database)
        mylist = list(read)
        if(len(mylist) == 0):
            return True
        else:
            return False

#Create a Database if one is not found
def create_db(my_dictionary):
    try:
        columns=['username','hash']
        with open('file.csv','x',newline='') as database:
            mywrite = csv.DictWriter(database,columns)
            mywrite.writeheader()
            mywrite.writerow(my_dictionary)
            return False
    except FileExistsError:
        print("Database has been previously created...")
        tkinter.messagebox.showwarning(title='Warning',message='Database has been previously created..')
        found_db = True
        return found_db

#hash values
def hash_value(wx,hvalue):
    encoded_value = hashlib.sha256(str.encode(hvalue))
    result = encoded_value.hexdigest()
    return result

#get username and password value
def display_delete(wx,uf,pf):
    usernvalue,passvalue = get_values(uf,pf)
    uf.delete(0,'end')
    pf.delete(0,'end')
    hashed_value = hash_value(wx,passvalue)
    print("creating database...")
    my_dictionary = {"username":usernvalue,"hash":hashed_value}
    found_db = create_db(my_dictionary)
    if(found_db):
        empty = is_db_empty()
        if(empty):
            print("DB is empty right now, Initializing...")
            add_db_data(my_dictionary)
        else:
            found_user=check_db(usernvalue,hashed_value)
            if(found_user != True):
                print('Adding new user')
                tkinter.messagebox.showinfo(title='window', message='Creds Added to DB')
                add_db_data(my_dictionary)

#get the values
def get_values(u,p):
    uvalue = u.get()
    pvalue = p.get()
    return uvalue,pvalue

#Main window GUI
def create_window():
    #main window
    window = Tk()
    window.title("Login Window")
    #window labels
    lbl1 = Label(window,text='Username:').place(x=100, y=50)
    lbl2 = Label(window,text='Password:').place(x=100, y=80)
    #window fields
    usrname_fld = Entry(bd=5)
    pswd_fld = Entry(bd=5,show='*')
    usrname_fld.place(x=200, y=50)
    pswd_fld.place(x=200, y=80)
    button = Button(window, text="Enter",command=lambda:display_delete(window,usrname_fld,pswd_fld))
    button.place(x=265,y=115)

    #bind the enter keyboard key
    window.bind('<Return>',lambda event:display_delete(window,usrname_fld,pswd_fld))

    #main window size
    window.geometry("500x300")
    window.mainloop()

create_window()
