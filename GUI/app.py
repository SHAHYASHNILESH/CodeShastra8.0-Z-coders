import this
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from turtle import onclick
from PIL import ImageTk, Image

app = Tk()

#	enter widgets here
# bg = PhotoImage(file = "skynight2.png")

# myLabel = Label(app,image = bg) 
# myLabel.place(x=0,y=0,relwidth=1,relheight=1) 
# Show image using label
app.title('Sleep Tracker')
app.geometry('616x411')

# dashBoard = StringVar()
# dashBoardLabel = Label(app,text='DASHBOARD',font = ('bold 14 underline'))


# def onClick():

#      messagebox.showinfo("Thank You","Our Team Will Get Back to you")

# ActivityBtn = tk.Button(app,text = "Sleeping Activity", command = onClick).grid(row=1,column=0)

# TrackingBtn = tk.Button(app,text = "Tracking", command = onClick).grid(row=3,column=0,pady = 30)



# dictionary of colors:
color = {"nero": "#FFFFFF", "purple": "purple", "darkorange": "#FE6101"}

# setting app window:
# app = tk.Tk()
# app.title("Tkinter Navbar")
# app.config(bg="gray17")
# app.geometry("400x600+850+50")

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="GUI/Menu.png")
closeIcon = PhotoImage(file="GUI/close.png")

  

        
# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navapp.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
     #    brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg=color["purple"])
        topFrame.config(bg=color["purple"])
        app.config(bg="white")

        # turning button OFF:
        btnState = False
    else:
        # make app dim:
     #    brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        app.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navapp.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(app, bg=color["purple"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="Sleep Tracker", font="Bahnschrift 15", bg=color["purple"], height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
# brandLabel = tk.Label(app,font="System 30", bg="gray17", fg="green")
# brandLabel.place(x=100, y=250)

# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["purple"], activebackground=color["purple"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navapp = tk.Frame(app, bg="white", height=1000, width=200)
navapp.place(x=-300, y=0)
tk.Label(navapp, font="Bahnschrift 15", bg=color["purple"], fg="white", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80

def db_click():
    # messagebox.showinfo("Dashboard Popup")
    switch()
    dashBoardLabel = Label(app,text='DASHBOARD',bg="white",font = ('bold 15 underline')).place(x=240,y=60)


def SA_click():
    messagebox.showinfo("Sleep Analytics Popup")
def Track_click():
    from ..Tracker import  sleep_tracker
    switch()
    trackBtn = tk.Button(app,text="Start Tracking", font="BahnschriftLight 15",fg='black',bg="purple",bd=0,activebackground="green",activeforeground="white").place(x=240, y=280)
    # dashBoardLabel.destroy()


ActivityBtn = tk.Button(navapp,text = "Dashboard", font="BahnschriftLight 15 underline", bg="white", fg=color["purple"], activeforeground="green", bd=0,command = db_click).place(x=25, y=y)
y += 60
ActivityBtn = tk.Button(navapp,text = "Sleep Analytics", font="BahnschriftLight 15 underline", bg="white", fg=color["purple"], activeforeground="green", bd=0,command = Track_click).place(x=25, y=y)
y += 60
ActivityBtn = tk.Button(navapp,text = "Tracking", font="BahnschriftLight 15 underline", bg="white", fg=color["purple"], activeforeground="green", bd=0,command = Track_click).place(x=25, y=y)
y += 60
# ActivityBtn = tk.Button(navapp,text = "Tracking", font="BahnschriftLight 15 underline", bg="white", fg=color["purple"], activeforeground="green", bd=0,command = db_click).place(x=25, y=y)
# y += 60


# Navbar Close Button:
closeBtn = tk.Button(navapp,image=closeIcon, bg=color["purple"], activebackground=color["purple"], bd=0, command=switch)
closeBtn.place(x=150, y=10)

# window in mainloop:

app.mainloop()

