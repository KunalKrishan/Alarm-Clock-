from email import message
import tkinter as tk 
from tkinter import *
from tkinter import messagebox
import os, time, sys



def createWidgets():
    #(root is the root window into which all other widgets go)(One window which has all these coming widgets)
    label1= Label(root, text="Enter the time in hh:mm - ") 
    #grid is the geomtery manager which organises widegts in a table_like structure in the parent widget (length and width manage)
    label1.grid(row=0, column=0, padx=5, pady=5)

    #global allows you to modify the variable inside and outside the current space (edit anywhere)
    global entry1
    #Entry is a widget used to accept single-line text strings from a user
    entry1= Entry(root, width=15)
    entry1.grid(row=0, column=1)

    #label is a widget that is used to implement display boxes where you can place text or images (box)

    label2 = Label(root, text="Enter the message of alarm: ")
    label2.grid(row=1, column=0, padx=5, pady=5)

    global entry2
    entry2 = Entry(root, width=15)
    entry2.grid(row=1, column=1)

    but = Button(root, text="Submit", width=10, command=submit)
    but.grid(row=2, column=1)

    global label3
    label3= Label(root, text="")
    label3.grid(row=3, column=0)

def message1():
    global entry1, label3
    Alarmtimelabel = entry1.get() #.get returns the value of the item specified here entry1
    label3.configure(text="The Alarm is counting....") #configure is used to change the text on label 
    messagebox.showinfo("Alarm Clock", f"The Alarm time is: {Alarmtimelabel}")
    


    

def submit():

    global entry1, entry2, label3
    Alarmtime= entry1.get()
    message1()
    currenttime = time.strftime("%H:%M")#strftime is used to convert date and time objects to their string representation. 
    alarmmessage= entry2.get()
    print(f"The Alarm time is: {Alarmtime}")
    while Alarmtime != currenttime:
        currenttime = time.strftime("%H:%M")
        time.sleep(1)
    if Alarmtime == currenttime:
        sys.stdout.write('Playing Alarm Sound....')
        sys.stdout.flush()
        label3.config(text="Alarm Sound Playing...")
        messagebox.showinfo("Alarm Message", f"The Message is {alarmmessage}")


root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x150")




createWidgets()

root.mainloop()