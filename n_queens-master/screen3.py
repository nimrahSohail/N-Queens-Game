from tkinter import *
import tkinter as ttk
#screen3=Tk()
#screen3.geometry('500x500')
#screen3.title('N-Queen')
#screen3.configure(bg='black')
#def get_data():
#    print(text_dis.get())

#text_inp=StringVar()
#text_dis=Entry(screen3,bg='blue',width=20,bd=30,insertwidth=4).grid(padx=10,pady=20)
#a=Button(screen3,command=get_data).grid()
#screen3.mainloop()

win = Tk()

#Set the geometry
win.geometry("700x250")

# Define a function to return the Input data
def get_data():
   label.config(text= entry.get(), font= ('Helvetica 13'))
   print(entry.get())

#Create an Entry Widget
entry = Entry(screen3, bg='white', width=40, bd=30, insertwidth=4).grid(padx=10, pady=20)
entry = Entry(win, width= 42)

entry.place(relx= .5, rely= .5, anchor= CENTER)

#Inititalize a Label widget
label= Label(win, text="", font=('Helvetica 13'))
label.pack()

#Create a Button to get the input data
ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

win.mainloop()