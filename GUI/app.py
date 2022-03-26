import this
import tkinter as tk
from tkinter import *
from tkinter import messagebox
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
# dashBoardLabel = Label(app,text='DASHBOARD',font = ('bold 14 underline'),bg="yellow")
# dashBoardLabel.grid(row=0,column=0,pady="30")
# # dashBoard.config(bg="yellow")

# def onClick():

#      messagebox.showinfo("Thank You","Our Team Will Get Back to you")

# ActivityBtn = tk.Button(app,text = "Sleeping Activity", command = onClick).grid(row=1,column=0)

# TrackingBtn = tk.Button(app,text = "Tracking", command = onClick).grid(row=3,column=0,pady = 30)



# dictionary of colors:
color = {"nero": "#FFFFFF", "orange": "purple", "darkorange": "#FE6101"}

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
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
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
topFrame = tk.Frame(app, bg=color["orange"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="Sleep Tracker", font="Bahnschrift 15", bg=color["orange"], height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
# brandLabel = tk.Label(app,font="System 30", bg="gray17", fg="green")
# brandLabel.place(x=100, y=250)

# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navapp = tk.Frame(app, bg="white", height=1000, width=200)
navapp.place(x=-300, y=0)
tk.Label(navapp, font="Bahnschrift 15", bg=color["orange"], fg="white", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Dashboard", "Settings", "Help", "About", "Feedback"]

# Navbar Option Buttons:
for i in range(5):
    tk.Button(navapp, text=options[i], font="BahnschriftLight 15", bg="white", fg=color["orange"], activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navapp,image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=150, y=10)

# window in mainloop:

app.mainloop()

