
#imports
import mysql.connector
from tkinter import *
import os
from PIL import ImageTk, Image

#Main Screen
master = Tk()
master.title('Banking App')
master.geometry('500x700')





# cursor.execute('create database bank')

def menu():
    print("*" * 140)
    print('WELCOME TO MAZE BANK'.center(140))
    print("*" * 140)
    print("1. Insert Record".center(140))
    print("2. Display Record".center(140))
    print("3. Search Record".center(140))
    print("4. Update Record".center(140))
    print("5. Delete Record".center(140))
    print("6. Transaction (Debit/Credit)".center(140))
    print("  a. Debit/Withdraw".center(140))
    print("  b. Credit ".center(140))
    print("7. Exit".center(140))
    print("*" * 140)


def MenuTransaction():
    print("   a. Debit/Withdraw from Account".center(140))
    print("   b. Credit into the Account".center(140))
    print("   c. Back".center(140))


def create():
    try:
        cursor.execute(
            'create table bankinfo(Account_No varchar(10), Name varchar(20), Mobile varchar(10), Email varchar(20), Address varchar(20), City varchar(10), Country varchar(10), Balance INT)')
        print("Table Created")
    except:
        print("Table Exist")


def insert():
    while True:
        Account_No = input("Enter Account No. : ")
        Name = input("Enter Name : ")
        Mobile = input("Enter Mobile No. : ")
        Email = input("Enter Email No. : ")
        Address = input("Enter Address : ")
        City = input("Enter City : ")
        Countey = input("Enter Country : ")
        Balance = input("Enter Balance : ")
        Rec = (Account_No, Name.upper(), Mobile, Email, Address.upper(), City.upper(), Countey.upper(), Balance)
        sql = 'insert into bankinfo values (%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, Rec)
        conn.commit()
        ch = input("Do you want to Enter more records : ")
        if ch == "N" or ch == "n":
            break


def DispAcc():
    try:
        cmd = "select * from bankinfo order by Name"
        cursor.execute(cmd)
        F = "%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("Account_No", "Name", "Mobile", "Email", "Address", "City", "Country", "Balance"))
        print("=" * 125)
        for i in cursor:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("=" * 125)
    except:
        print("Table doesn't exist")


def search():
    try:
        cmd = 'select * from bankinfo'
        cursor.execute(cmd)
        ch = input("Enter the Account No. to be Searched : ")
        for i in cursor:
            if i[0] == ch:
                print("=" * 125)
                F = "%15s %15s %15s %15s %15s %15s %15s %15s"
                print(F % ("Account_No", "Name", "Mobile", "Email", "Address", "City", "Country", "Balance"))
                print("=" * 125)
                for j in i:
                    print('%14s' % j, end=' ')
                print()
                break
        else:
            print("Record Not Found")
    except:
        print("Table doesn't exist")


def update():
    try:
        cmd = "select * from bankinfo"
        cursor.execute(cmd)
        A = input("Enter the Account No. whose details to be changed : ")
        for i in cursor:
            i = list(i)
            if i[0] == A:
                ch = input("Change Name (Y/N) ")
                if ch == 'Y' or ch == 'y':
                    i[1] = input("Enter Name : ")
                    i[1] = i[1].upper()

                ch = input("Change Mobile (Y/N) ")
                if ch == 'Y' or ch == 'y':
                    i[2] = input("Enter Mobile No. : ")

                ch = input("Change Email (Y/N) ")
                if ch == "Y" or ch == 'y':
                    i[3] = input("Enter Email : ")
                    # i[3]=i[3].upper()

                ch = input("Change Address (Y/N) ")
                if ch == "Y" or ch == 'y':
                    i[4] = input("Enter Address : ")
                    # i[4]=i[4].upper()

                ch == input("Change City (Y/N) ")
                if ch == "Y" or ch == "y":
                    i[5] = input("Enter City : ")
                    # i[5]=i[5].upper()

                ch == input("Change Country (Y/N) ")
                if ch == "Y" or ch == "y":
                    i[6] = input("Enter Country : ")
                    # i[6]=i[6].upper()

                ch == input("Change Balance (Y/N) ")
                if ch == "Y" or ch == "y":
                    i[7] = float(input("Enter Balance : "))

                cmd = "update bankinfo set Name=%s, Mobile=%s, Email=%s, Address=%s, City=%s, Country=%s, Balance=%s where Account_No=%s"
                val = (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
                cursor.execute(cmd, val)
                conn.commit()
                print("Account Updated")
                break
        else:
            print("Record not found")
    except:
        print("No such Table")


def delete():
    try:
        cmd = "select * from bankinfo"
        cursor.execute(cmd)
        A = input("Enter the Account No whose account want to delete : ")
        for i in cursor:
            i = list(i)
            if i[0] == A:
                cmd = "delete from bankinfo where Account_No=%s"
                val = (i[0],)
                cursor.execute(cmd, val)
                conn.commit()
                print("Account Deleted")
        else:
            print("Record Not Found")
    except:
        print("No such Table")


def debit():
    cmd = "select * from bankinfo"
    cursor.execute(cmd)
    print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
    Acc = input("Enter the Account No from which the money is to be debited : ")
    for i in cursor:
        i = list(i)
        if i[0] == Acc:
            Amt = float(input("Enter the Amount to be withdrawn : "))
            if i[7] - Amt > 5000:
                i[7] -= Amt
                cmd = "update bankinfo set Balance=%s where Account_No=%s"
                val = (i[7], i[0])
                cursor.execute(cmd, val)
                conn.commit()
                print("Account Debited")
                break
            else:
                print("There must be min Balance of Rs 5000")
                break
        else:
            print("Record Not Found")


def credit():
    try:
        cmd = "select * from bankinfo"
        cursor.execute(cmd)
        acc = input("Enter the Account No in which you want to deposit : ")
        for i in cursor:
            i = list(i)
            if i[0] == acc:
                Amt = float(input("Enter the Amount to be deposit : "))
                i[7] += Amt
                cmd = "update bankinfo set Balance=%s where Account_No=%s"
                val = (i[7], i[0])
                cursor.execute(cmd, val)
                conn.commit()
                print("Amount Credited")
                break
            else:
                print("Record Not Found")
    except:
        print("Table Doesn't Exist")


while True:
    menu()
    ch = input("Enter Your Choice : ")
    if ch == "1":
        insert()
    elif ch == "2":
        DispAcc()
    elif ch == "3":
        search()
    elif ch == "4":
        update()
    elif ch == "5":
        delete()
    elif ch == "6":
        while True:
            MenuTransaction()
            ch1 = input("Enter Choice a/b/c : ")
            if ch1 == 'a':
                debit()
            elif ch1 == 'b':
                credit()
            elif ch1 == 'c':
                print("Back to Main Menu")
                break
            else:
                print("Invalid Choice")
    elif ch == "7":
        print("Exiting...")
        break
    else:
        print("Wrong Choice Entered")

master.mainloop()