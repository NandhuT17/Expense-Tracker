from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import os
import csv



file_path = os.path.isfile("data.csv")



def save_details() :
    date_field = date_input.get()
    time_field = time_input.get()
    type_field = type_box.get()
    category_field = category_box.get()
    amount_field = amount_input.get()
    note_field = note_input.get()

    with open("data.csv","a",newline="") as file :
        writer = csv.writer(file)

        if not file_path :
            writer.writerow(["Date","Time","Type","Category","Amount","Note"])

        writer.writerow([date_field,time_field,type_field,category_field,amount_field,note_field])
    
    date_input.delete(0,END)
    time_input.delete(0,END)
    amount_input.delete(0,END)
    note_input.delete(0,END)

    messagebox.showinfo(title="Added",message="Your Income/Expense has been successfully added")



def clear() :
    date_input.delete(0,END)
    time_input.delete(0,END)
    amount_input.delete(0,END)
    note_input.delete(0,END)

def show_transactions() :
    win = tk.Toplevel(window)
    win.title("Transactions")
    win.geometry("800x400")

    tree = ttk.Treeview(win)
    tree.pack(fill="both",expand=True)

    try :
        with open("data.csv","r") as file :
            csv_reader = csv.reader(file)
            headers = next(csv_reader)

            tree['columns'] = headers

            for h in headers :
                tree.heading(h,text=h)
                tree.column(h,width=100)

            for row in csv_reader :
                tree.insert("","end",values=row)
    except FileNotFoundError :
        messagebox.showwarning("No data")

def download_report():
    pass








window = tk.Tk()
window.title("Expense Tracker")

#Labels
date_label = tk.Label(window,text="Date (DD-MM-YY): ")
time_label = tk.Label(window,text="Time: ")
type_label = tk.Label(window,text="Type: ")
category_label = tk.Label(window,text="Category: ")
amount_label = tk.Label(window,text="Amount: ")
note_label = tk.Label(window,text="Note: ")



#Buttons
save_button = tk.Button(window,text="Save",command=save_details)
clear_button = tk.Button(window,text="Clear",command=clear)
show_transactions_button = tk.Button(window,text="Show Transactions",command=show_transactions)
download_button = tk.Button(window,text="Download Report")



#Inputs
date_input = tk.Entry(width=50)
time_input = tk.Entry(width=50)
date_input.insert(0,datetime.now().strftime("%d/%m/%y"))
time_input.insert(0,datetime.now().strftime("%H:%M"))
amount_input = tk.Entry(width=50)
note_input = tk.Entry(width=50)

#Dropdown box for Type
type_value = tk.StringVar()
type_box = Combobox(window,textvariable=type_value,state="readonly",width=48)
type_box["values"] = ["Income","Expense"]
type_box.current(0)

#Dropdown Box for Category
category_value = tk.StringVar()
category_box = Combobox(window,textvariable=category_value,state="readonly",width=48)
expense_list = ["Food","Travel","Bills","Grocery","Education","Others"]
income_list = ["Salary","Savings","Business","Others"]

def update(event=None) :
    if type_box.get() == "Expense" :
        category_box["values"] = expense_list
        category_box.current(0)
    else :
        category_box["values"] = income_list
        category_box.current(0)

type_box.bind("<<ComboboxSelected>>",update)
type_box.current(0)
update()



#Grid
date_label.grid(row=0,column=0)
date_input.grid(row=0,column=1)
time_label.grid(row=1,column=0)
time_input.grid(row=1,column=1)
type_label.grid(row=2,column=0)
type_box.grid(row=2,column=1)
category_label.grid(row=3,column=0)
category_box.grid(row=3,column=1)
amount_label.grid(row=4,column=0)
amount_input.grid(row=4,column=1)
note_label.grid(row=5,column=0)
note_input.grid(row=5,column=1)
save_button.grid(row=6,column=0)
clear_button.grid(row=6,column=1)
show_transactions_button.grid(row=0,column=2)
download_button.grid(row=1,column=2)



window.mainloop()