# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:39:29 2019

@author: Fazle Rasul
"""

from tkinter import *
from tkinter import filedialog
import os


root = Tk()
root.minsize(width=500,height=400)
filename="F:/Data/Images/ISIC_0000000.jpeg"

def fileBrowsing():
    filename = filedialog.askopenfilename(initialdir="/",title="select a file",filetype=(("jpeg","*.jpg"),("All Files","*.*")))
    print (filename)
def encrypt():
    print (filename)
    com = "encrypt "+filename
    os.system(com)
    
def decrypt():
    print (filename)
    com = "decrypt "+filename
    os.system(com)
    
def key_gen():
    os.system("key_generate")


menubar = Menu(root)
root.config(menu=menubar)
menu_s = Menu(menubar)
menubar.add_cascade(label="start", menu=menu_s)
menu_s.add_command(label="Register")
menu_s.add_separator()
menu_s.add_command(label="Log in")
menu_s.add_separator()
menu_s.add_command(label="Log out")

menubar.add_cascade(label="exit",command = root.destroy)

browse = PhotoImage(file="browse.png")
lock = PhotoImage(file="lock.png")
unlock = PhotoImage(file="unlock.png")

toolbar = Frame(root)
br_btn = Button(toolbar,image=browse,text="Browse File",compound=TOP,command=fileBrowsing)
lock_btn = Button(toolbar,image=lock,text="Lock",compound=TOP,command=encrypt)
unlock_btn = Button(toolbar,image=unlock,text="Unlock",compound=TOP,command=decrypt)
br_btn.pack(side=LEFT,padx=10)
lock_btn.pack(side=LEFT,padx=10)
unlock_btn.pack(side=LEFT,padx=10)
toolbar.pack(side=TOP,fill=X)

bottomFrame = Frame(root)
label = Label(bottomFrame,text="List of the files you have encrypted ......")
label.pack(pady=50)

bottomFrame.pack()


root.mainloop()

















