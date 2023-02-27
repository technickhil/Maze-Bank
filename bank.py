#imports
from tkinter import messagebox
import os
import mysql.connector
from tkinter import *
import os
from PIL import ImageTk, Image
#Main Screen
root = Tk()
root.title('Maze Bank')
root.iconbitmap('favicon.ico')
root.geometry('1005x578')
root.resizable(width=False, height=False)

# sql
conn = mysql.connector.connect(user='root',
                               passwd='123456',
                               host='localhost',
                               auth_plugin='mysql_native_password',
                               database='bank'
                               )

cursor = conn.cursor(buffered=True)
# Add image file
bg = ImageTk.PhotoImage(Image.open("bg1.jpg"))


# Show image using label
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)



# mazebank_logo = ImageTk.PhotoImage(Image.open("mazebank_logo.png"))
# logo_label = Label(root, image=mazebank_logo,)
# logo_label.grid(row=0, column=1)

# wlc_maze_bank = Label(root,text="Welcome to Maze Bank", font="comicsansms 30 bold")
# wlc_maze_bank.grid(row=6,column=2)
# # wlc_maze_bank.bg('-alpha',0.5)

def insert_sub():
        Account_No = temp_acc_no.get()
        Name = temp_name.get()
        Mobile = temp_mobile.get()
        Email = temp_email.get()
        Address = temp_address.get()
        City = temp_city.get()
        Country = temp_country.get()
        Balance = temp_balance.get()
        Rec = (Account_No, Name.upper(), Mobile, Email, Address.upper(), City.upper(), Country.upper(), Balance)
        # for acc_check in all_accounts:
        #     if name == name_check:
        #         notif.config(fg="red", text="Account already exists")
        #         return
        #     else:
        #         new_file = open(name, "w")
        #         new_file.write(name + '\n')
        #         new_file.write(password + '\n')
        #         new_file.write(age + '\n')
        #         new_file.write(gender + '\n')
        #         new_file.write('0')
        #         new_file.close()
        #         notif.config(fg="green", text="Account has been created")
        sql = 'insert into bankinfo values (%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, Rec)
        conn.commit()
        messagebox.showinfo("Successfull","Account has been created")
        notif.config(fg="green", text="Click on exit to close")
        # ch = input("Do you want to Enter more records : ")
        # if ch == "N" or ch == "n":
        #     break


def insert():
#Insert Screen
    insert_screen = Toplevel(root)
    insert_screen.title('Insert Record')
    insert_screen.geometry('600x360')
    insert_screen.resizable(width=False, height=False)

    #Vars
    global temp_acc_no
    global temp_name
    global temp_mobile
    global temp_email
    global temp_address
    global temp_city
    global temp_country
    global temp_balance
    global notif

    temp_acc_no = StringVar()
    temp_name = StringVar()
    temp_mobile = StringVar()
    temp_email = StringVar()
    temp_address = StringVar()
    temp_city = StringVar()
    temp_country = StringVar()
    temp_balance = IntVar()

#Labels
    Label(insert_screen, text="Please enter your details below to Insert Record", font=('Calibri',12)).grid(pady=10)
    Label(insert_screen, text="Account No : ", font=('Calibri',12)).grid(row=1,column=0)
    Label(insert_screen, text="Name : ", font=('Calibri',12)).grid(row=2,column=0)
    Label(insert_screen, text="Mobile : ", font=('Calibri',12)).grid(row=3,column=0)
    Label(insert_screen, text="Email : ", font=('Calibri',12)).grid(row=4,column=0)
    Label(insert_screen, text="Address : ", font=('Calibri',12)).grid(row=5,column=0)
    Label(insert_screen, text="City : ", font=('Calibri',12)).grid(row=6,column=0)
    Label(insert_screen, text="Country : ", font=('Calibri',12)).grid(row=7,column=0)
    Label(insert_screen, text="Balance : ", font=('Calibri',12)).grid(row=8,column=0)
    notif = Label(insert_screen, font=('Calibri', 12))
    notif.grid(row=10,column=1,pady=10)

#Entries
    Entry(insert_screen,textvariable=temp_acc_no).grid(row=1,column=1 ,padx="15")
    Entry(insert_screen,textvariable=temp_name).grid(row=2,column=1)
    Entry(insert_screen,textvariable=temp_mobile).grid(row=3,column=1)
    Entry(insert_screen,textvariable=temp_email).grid(row=4,column=1)
    Entry(insert_screen,textvariable=temp_address).grid(row=5,column=1)
    Entry(insert_screen,textvariable=temp_city).grid(row=6,column=1)
    Entry(insert_screen,textvariable=temp_country).grid(row=7,column=1)
    Entry(insert_screen,textvariable=temp_balance).grid(row=8,column=1)

#Buttons
    Button(insert_screen, text="Submit", command = insert_sub , font=('Calibri',12)).grid(row=9,column=1,pady=10)

    Button(insert_screen, text="Exit",width=5, height=1,highlightbackground="red", highlightthickness="2", command = insert_screen.destroy, font=('Calibri',12)).grid(row=9,column=7,pady=10)




    insert_screen.mainloop()

def update_sub():
    Account_No = temp1_acc_no.get()
    Name = temp1_name.get()
    Mobile = temp1_mobile.get()
    Email = temp1_email.get()
    # print(Email)
    Address = temp1_address.get()
    City = temp1_city.get()
    Country = temp1_country.get()
    # Balance = temp1_balance.get()
    try:
        cmd = "select * from bankinfo"
        cursor.execute(cmd)
        # A = input("Enter the Account No. whose details to be changed : ")
        for i in cursor:
            i = list(i)
            if i[0] == Account_No:
                # ch = input("Change Name (Y/N) ")
                # if ch == 'Y' or ch == 'y':
                if Name!="":
                    i[1] = Name
                    i[1] = i[1].upper()

                # ch = input("Change Mobile (Y/N) ")
                # if ch == 'Y' or ch == 'y':
                if Mobile!="":
                    i[2] = Mobile

                # ch = input("Change Email (Y/N) ")
                # if ch == "Y" or ch == 'y':
                if Email!="":
                    i[3] = Email
                    # i[3]=i[3].upper()

                # ch = input("Change Address (Y/N) ")
                # if ch == "Y" or ch == 'y':
                if Address!="":
                    i[4] = Address
                    # i[4]=i[4].upper()

                # ch == input("Change City (Y/N) ")
                # if ch == "Y" or ch == "y":
                if City!="":
                    i[5] = City
                    # i[5]=i[5].upper()

                # ch == input("Change Country (Y/N) ")
                # if ch == "Y" or ch == "y":
                if Country!="":
                    i[6] = Country
                    # i[6]=i[6].upper()

                # ch == input("Change Balance (Y/N) ")
                # if ch == "Y" or ch == "y":
                # if Balance=0:
                #     i[7] = float(Balance)

                cmd = "update bankinfo set Name=%s, Mobile=%s, Email=%s, Address=%s, City=%s, Country=%s, Balance=%s where Account_No=%s"
                val = (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
                cursor.execute(cmd, val)
                conn.commit()
                messagebox.showinfo("Successfull", "Account has been updated")
                notif1.config(fg="green", text="Click on exit to close")
                break
        else:
            messagebox.showinfo("Error","Record not found")
            notif1.config(fg="green", text="Click on exit to close")
    except:
        messagebox.showinfo("Error","No such table")
        notif1.config(fg="green", text="Click on exit to close")

def update():
    # Insert Screen
    update_screen = Toplevel(root)
    update_screen.title('Update Record')
    update_screen.geometry('600x360')
    update_screen.resizable(width=False, height=False)

    # Vars
    global temp1_acc_no
    global temp1_name
    global temp1_mobile
    global temp1_email
    global temp1_address
    global temp1_city
    global temp1_country
    global temp1_balance
    global notif1

    temp1_acc_no = StringVar()
    temp1_name = StringVar()
    temp1_mobile = StringVar()
    temp1_email = StringVar()
    temp1_address = StringVar()
    temp1_city = StringVar()
    temp1_country = StringVar()
    # temp1_balance = IntVar()

    # Labels
    Label(update_screen, text="Please enter your details below to Update Record", font=('Calibri', 12)).grid(pady=10)
    Label(update_screen, text="Account No(To Update) : ", font=('Calibri', 12)).grid(row=1, column=0)
    Label(update_screen, text="Name : ", font=('Calibri', 12)).grid(row=2, column=0)
    Label(update_screen, text="Mobile : ", font=('Calibri', 12)).grid(row=3, column=0)
    Label(update_screen, text="Email : ", font=('Calibri', 12)).grid(row=4, column=0)
    Label(update_screen, text="Address : ", font=('Calibri', 12)).grid(row=5, column=0)
    Label(update_screen, text="City : ", font=('Calibri', 12)).grid(row=6, column=0)
    Label(update_screen, text="Country : ", font=('Calibri', 12)).grid(row=7, column=0)
    # Label(update_screen, text="Balance : ", font=('Calibri', 12)).grid(row=8, column=0)
    notif1 = Label(update_screen, font=('Calibri', 12))
    notif1.grid(row=9, column=1, pady=10)

    # Entries
    Entry(update_screen, textvariable=temp1_acc_no).grid(row=1, column=1, padx="15")
    Entry(update_screen, textvariable=temp1_name).grid(row=2, column=1)
    Entry(update_screen, textvariable=temp1_mobile).grid(row=3, column=1)
    Entry(update_screen, textvariable=temp1_email).grid(row=4, column=1)
    Entry(update_screen, textvariable=temp1_address).grid(row=5, column=1)
    Entry(update_screen, textvariable=temp1_city).grid(row=6, column=1)
    Entry(update_screen, textvariable=temp1_country).grid(row=7, column=1)
    # Entry(update_screen, textvariable=temp1_balance).grid(row=8, column=1)

    # Buttons
    Button(update_screen, text="Submit", command=update_sub, font=('Calibri', 12)).grid(row=8, column=1, pady=10)

    Button(update_screen, text="Exit",width=5, height=1,highlightbackground="red", highlightthickness="2", command=update_screen.destroy, font=('Calibri', 12)).grid(row=8, column=7,
                                                                                                 pady=10)

    update_screen.mainloop()

def display():
    display_screen = Toplevel(root)
    display_screen.title('Display Record')
    display_screen.geometry('818x500')
    display_screen.resizable(width=False, height=False)

    Label(display_screen, text="Account No", font=('Calibri', 12)).grid(row=0, column=0)
    Label(display_screen, text="Name", font=('Calibri', 12)).grid(row=0, column=1)
    Label(display_screen, text="Mobile", font=('Calibri', 12)).grid(row=0, column=2)
    Label(display_screen, text="Email", font=('Calibri', 12)).grid(row=0, column=3)
    Label(display_screen, text="Address", font=('Calibri', 12)).grid(row=0, column=4)
    Label(display_screen, text="City", font=('Calibri', 12)).grid(row=0, column=5)
    Label(display_screen, text="Country", font=('Calibri', 12)).grid(row=0, column=6)
    Label(display_screen, text="Balance", font=('Calibri', 12)).grid(row=0, column=7)
    my_conn = conn.cursor()
    ####### end of connection ####
    my_conn.execute("SELECT * FROM bankinfo;")
    i = 1
    for student in my_conn:
        for j in range(len(student)):
            e = Entry(display_screen, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    display_screen.mainloop()

def delete_sub():
    Account_No = temp2_acc_no.get()
    try:
        cmd = "select * from bankinfo"
        cursor.execute(cmd)
        A = Account_No
        for i in cursor:
            i = list(i)
            if i[0] == A:
                cmd = "delete from bankinfo where Account_No=%s"
                val = (i[0],)
                cursor.execute(cmd, val)
                conn.commit()
                messagebox.showinfo("Deleted","Account deleted")
                notif2.config(fg="green", text="Click on exit to close")
                break
        else:
            messagebox.showinfo("Error","Record not found")
            notif2.config(fg="green", text="Click on exit to close")
    except:
        messagebox.showinfo("Error","No such table")
        notif2.config(fg="green", text="Click on exit to close")

def delete():
    delete_screen = Toplevel(root)
    delete_screen.title('Delete Record')
    delete_screen.geometry('300x150')
    delete_screen.resizable(width=False, height=False)

    global temp2_acc_no
    global notif2
    temp2_acc_no = StringVar()

    Label(delete_screen, text="Account No", font=('Calibri', 12)).grid(row=0, column=0)
    Entry(delete_screen, textvariable=temp2_acc_no).grid(row=0, column=1, padx="15")
    notif2 = Label(delete_screen, font=('Calibri', 12))
    notif2.grid(row=2, column=1, pady=10)

    Button(delete_screen, text="Submit", command=delete_sub, font=('Calibri', 12)).grid(row=1, column=0, pady=10)

    Button(delete_screen, text="Exit",width=5, height=1,highlightbackground="red", highlightthickness="2", command=delete_screen.destroy, font=('Calibri', 12)).grid(row=1, column=1,
                                                                                                 pady=10)
    delete_screen.mainloop()

def search_sub():

    Account_No = temp3_acc_no.get()
    try:
        cmd = 'select * from bankinfo'
        cursor.execute(cmd)
        ch = Account_No
        for i in cursor:
            if i[0] == ch:
                search_sub_screen = Toplevel(root)
                search_sub_screen.title('Displaying...')
                search_sub_screen.geometry('270x300')
                search_sub_screen.resizable(width=False, height=False)
                Label(search_sub_screen, text="Account No : ", font=('Calibri', 12)).grid(row=0, column=0)
                Label(search_sub_screen, text="Name : ", font=('Calibri', 12)).grid(row=1, column=0)
                Label(search_sub_screen, text="Mobile : ", font=('Calibri', 12)).grid(row=2, column=0)
                Label(search_sub_screen, text="Email : ", font=('Calibri', 12)).grid(row=3, column=0)
                Label(search_sub_screen, text="Address : ", font=('Calibri', 12)).grid(row=4, column=0)
                Label(search_sub_screen, text="City : ", font=('Calibri', 12)).grid(row=5, column=0)
                Label(search_sub_screen, text="Country : ", font=('Calibri', 12)).grid(row=6, column=0)
                Label(search_sub_screen, text="Balance : ", font=('Calibri', 12)).grid(row=7, column=0)
                Label(search_sub_screen, text=i[0], font=('Calibri', 12)).grid(row=0, column=1)
                Label(search_sub_screen, text=i[1], font=('Calibri', 12)).grid(row=1, column=1)
                Label(search_sub_screen, text=i[2], font=('Calibri', 12)).grid(row=2, column=1)
                Label(search_sub_screen, text=i[3], font=('Calibri', 12)).grid(row=3, column=1)
                Label(search_sub_screen, text=i[4], font=('Calibri', 12)).grid(row=4, column=1)
                Label(search_sub_screen, text=i[5], font=('Calibri', 12)).grid(row=5, column=1)
                Label(search_sub_screen, text=i[6], font=('Calibri', 12)).grid(row=6, column=1)
                Label(search_sub_screen, text=i[7], font=('Calibri', 12)).grid(row=7, column=1)
                Button(search_sub_screen, text="Exit", width=5, height=1, highlightbackground="red",
                       highlightthickness="2", command=search_sub_screen.destroy, font=('Calibri', 12)).grid(row=8,
                                                                                                             column=1,
                                                                                                             pady=10)
                notif3.config(fg="green", text="Click on exit to close")
                search_sub_screen.mainloop()

                # print("=" * 125)
                # F = "%15s %15s %15s %15s %15s %15s %15s %15s"
                # print(F % ("Account_No", "Name", "Mobile", "Email", "Address", "City", "Country", "Balance"))
                # print("=" * 125)
                # for j in i:
                #
                #     print('%14s' % j, end=' ')
                # print()
                break
        else:
            messagebox.showinfo("Error", "Record not found")
            notif3.config(fg="green", text="Click on exit to close")
    except:
        messagebox.showinfo("Error", "Table doesn't exits!!")
        notif2.config(fg="green", text="Click on exit to close")




def search():
    search_screen = Toplevel(root)
    search_screen.title('Search Record')
    search_screen.geometry('300x150')
    search_screen.resizable(width=False, height=False)

    global temp3_acc_no
    global notif3
    temp3_acc_no = StringVar()

    Label(search_screen, text="Account No", font=('Calibri', 12)).grid(row=0, column=0)
    Entry(search_screen, textvariable=temp3_acc_no).grid(row=0, column=1, padx="15")
    notif3 = Label(search_screen, font=('Calibri', 12))
    notif3.grid(row=2, column=1, pady=10)

    Button(search_screen, text="Search", command=search_sub, font=('Calibri', 12)).grid(row=1, column=0, pady=10)

    Button(search_screen, text="Exit",width=5, height=1,highlightbackground="red", highlightthickness="2", command=search_screen.destroy, font=('Calibri', 12)).grid(row=1, column=1,pady=10)
    search_screen.mainloop()


def debit_sub():
    Account_No = temp4_acc_no.get()
    Withdraw = temp4_withdraw.get()
    cmd = "select * from bankinfo"
    cursor.execute(cmd)
    Acc = Account_No
    for i in cursor:
        i = list(i)
        if i[0] == Acc:
            Amt = Withdraw
            if i[7] - Amt > 5000:
                i[7] -= Amt
                cmd = "update bankinfo set Balance=%s where Account_No=%s"
                val = (i[7], i[0])
                cursor.execute(cmd, val)
                conn.commit()
                messagebox.showinfo("Successfull", "Amount Debited!!")
                notif4.config(fg="green", text="Click on exit to close")
                break
            else:
                messagebox.showinfo("Error", "There must be min balance of 5000")
                notif4.config(fg="green", text="Click on exit to close")
                break
        else:
            messagebox.showinfo("Error", "Record not found")
            notif4.config(fg="green", text="Click on exit to close")

def debit():
    debit_screen = Toplevel(root)
    debit_screen.title('Debit Money')
    debit_screen.geometry('450x200')
    debit_screen.resizable(width=False, height=False)

    global temp4_acc_no
    global temp4_withdraw
    global notif4
    temp4_acc_no = StringVar()
    temp4_withdraw = IntVar()

    Label(debit_screen, text="Account No", font=('Calibri', 12)).grid(row=0, column=0)
    Label(debit_screen, text="Withdraw Amount : ", font=('Calibri', 12)).grid(row=1, column=0)
    Entry(debit_screen, textvariable=temp4_acc_no).grid(row=0, column=1, padx="15")
    Entry(debit_screen, textvariable=temp4_withdraw).grid(row=1, column=1, padx="15")
    notif4 = Label(debit_screen, font=('Calibri', 12))
    notif4.grid(row=3, column=1, pady=10)
    notif4.config(fg="green", text="Minimum Balance Required : 5000 Rs")

    Button(debit_screen, text="Debit", command=debit_sub, font=('Calibri', 12)).grid(row=2, column=0, pady=10)

    Button(debit_screen, text="Exit", width=5, height=1, highlightbackground="red", highlightthickness="2",
           command=debit_screen.destroy, font=('Calibri', 12)).grid(row=2, column=1, pady=10)

    debit_screen.mainloop()
def credit_sub():
    try:
        Account_No = temp5_acc_no.get()
        Deposit = temp5_deposit.get()
        cmd = "select * from bankinfo"
        cursor.execute(cmd)
        Acc = Account_No
        for i in cursor:
            i = list(i)
            if i[0] == Acc:
                Amt = Deposit
                i[7] += Amt
                cmd = "update bankinfo set Balance=%s where Account_No=%s"
                val = (i[7], i[0])
                cursor.execute(cmd, val)
                conn.commit()
                messagebox.showinfo("Successfull", "Amount Credited!!")
                notif5.config(fg="green", text="Click on exit to close")
                break
            else:
                messagebox.showinfo("Error", "Record not found!!")
                notif5.config(fg="green", text="Click on exit to close")
                break
    except:
        messagebox.showinfo("Error", "Table doesn't exists!!")
        notif5.config(fg="green", text="Click on exit to close")

def credit():
    credit_screen = Toplevel(root)
    credit_screen.title('Credit Money')
    credit_screen.geometry('350x150')
    credit_screen.resizable(width=False, height=False)

    global temp5_acc_no
    global temp5_deposit
    global notif5
    temp5_acc_no = StringVar()
    temp5_deposit = IntVar()

    Label(credit_screen, text="Account No", font=('Calibri', 12)).grid(row=0, column=0)
    Label(credit_screen, text="Deposit Amount : ", font=('Calibri', 12)).grid(row=1, column=0)
    Entry(credit_screen, textvariable=temp5_acc_no).grid(row=0, column=1, padx="15")
    Entry(credit_screen, textvariable=temp5_deposit).grid(row=1, column=1, padx="15")
    notif5 = Label(credit_screen, font=('Calibri', 12))
    notif5.grid(row=3, column=1, pady=10)
    # notif4.config(fg="green", text="Minimum Balance Required : 5000 Rs")

    Button(credit_screen, text="Credit", command=credit_sub, font=('Calibri', 12)).grid(row=2, column=0, pady=10)

    Button(credit_screen, text="Exit", width=5, height=1, highlightbackground="red", highlightthickness="2",
           command=credit_screen.destroy, font=('Calibri', 12)).grid(row=2, column=1, pady=10)

    credit_screen.mainloop()

def transaction():
    transaction_screen = Toplevel(root)
    transaction_screen.title('Credit/Debit')
    transaction_screen.geometry('200x270')
    transaction_screen.resizable(width=False, height=False)

    Label(transaction_screen, text="Select Transaction", font=('Calibri', 12)).grid(row=0, column=0)
    Button(transaction_screen, text="Credit", width=15, height=2, command=credit, font=('Calibri', 12)).grid(row=1, column=0, pady=10,padx=10)

    Button(transaction_screen, text="Debit", width=15, height=2, command=debit, font=('Calibri', 12)).grid(row=2, column=0,
                                                                                                 pady=10,padx=10)
    Button(transaction_screen, text="Exit", width=5, height=1,highlightbackground="red", highlightthickness="2",fg="black", command=transaction_screen.destroy, font=('Calibri', 12)).grid(row=3,
                                                                                                           column=0,
                                                                                                           pady=10,padx=10)

    transaction_screen.mainloop()



Insert = Button(root, width=15, height=1, text="INSERT RECORD",
              highlightbackground="red", highlightthickness="5", fg="black", font="comicsansms 15 bold",command=insert).grid(row=5,
                                                         column=0, padx="50", pady=(220,30))
Display = Button(root, width=15, height=1, text="DISPLAY RECORD",
              highlightbackground="red", highlightthickness="5", fg="black", font="comicsansms 15 bold",command=display).grid(row=6,
                                                         column=0, padx="50", pady="30")
Search = Button(root, width=15, height=1, text="SEARCH RECORD",
              highlightbackground="red", highlightthickness="5", fg="black", font="comicsansms 15 bold",command=search).grid(row=8,
                                                         column=0, padx="50", pady="30")
Update = Button(root, width=15, height=1, text="UPDATE RECORD",
              highlightbackground="red", highlightthickness="5", fg="black", font="comicsansms 15 bold",command=update).grid(row=5,
                                                         column=10, padx=(430,0), pady=(220,30))
Delete = Button(root, width=15, height=1, text="DELETE RECORD",
              highlightbackground="red", highlightthickness="5", fg="black", font="comicsansms 15 bold",command=delete).grid(row=6,
                                                         column=10, padx=(430,0), pady="30")
Transaction = Button(root, width=15, height=1, text="TRANSACTION",
              highlightbackground="red", highlightthickness="5", fg="black", font="comicsansms 15 bold",command=transaction).grid(row=8,
                                                         column=10, padx=(430,0), pady="30")



root.mainloop()