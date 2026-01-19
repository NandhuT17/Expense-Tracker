from tkinter import *
import tkinter as tk
import csv
import os

window = tk.Tk()
window.title("Expense Tracker")



def add_details() :
    date = date_input.get()
    type_ = type_input.get()
    category = category_input.get()
    amount = amount_input.get()
    note = note_input.get()


    file_path = os.path.isfile("data.csv")

    with open("data.csv","a",newline='') as file:
        writer = csv.writer(file)
        
        if not file_path :
            writer.writerow(["Date","Type","Category","Amount","Note"])

        writer.writerow([date,type_,category,amount,note])

    date_input.delete(0,tk.END)
    type_input.delete(0,tk.END)
    category_input.delete(0,tk.END)
    amount_input.delete(0,tk.END)
    note_input.delete(0,tk.END)


def clear_details() :
    date_input.delete(0,tk.END)
    type_input.delete(0,tk.END)
    category_input.delete(0,tk.END)
    amount_input.delete(0,tk.END)
    note_input.delete(0,tk.END)


#labels
date_label = tk.Label(window, text = "Date (YYYY-MM-DD): ")
type_label = tk.Label(window,text="Type: ")
category_label = tk.Label(window,text="Category: ")
amount_label = tk.Label(window,text="Amount: ")
note_label = tk.Label(window,text="Note: ")


#input fields
date_input = tk.Entry(window)
type_input = tk.Entry(window)
category_input = tk.Entry(window)
amount_input = tk.Entry(window)
note_input = tk.Entry(window)



#butons
add_button = tk.Button(window,text="Add",command=add_details)
clear_button = tk.Button(window,text="Clear",command=clear_details)



#grid
date_label.grid(row=0,column=0)
type_label.grid(row=1,column=0)
category_label.grid(row=2,column=0)
amount_label.grid(row=3,column=0)
note_label.grid(row=4,column=0)
date_input.grid(row=0,column=1)
type_input.grid(row=1,column=1)
category_input.grid(row=2,column=1)
amount_input.grid(row=3,column=1)
note_input.grid(row=4,column=1) 
add_button.grid(row=5,column=0)
clear_button.grid(row=5,column=1)





window.mainloop()