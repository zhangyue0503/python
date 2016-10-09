import os
from time import sleep
from Tkinter import *

class DirList(object):
    def __init__(self):
        self.top = Tk()
        self.label = Label(self.top,text='Directory Lister v1.1')
        self.label.pack()

        self.cwd = StringVar(self.top)

        self.dir1 = Label(self.top,fa='blue',font=('Helvetica',12,'bold'))
        self.dir1.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT,fill=Y)
        self.dirs = Listbox(self.dirfm,height=16,width=50,yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>',self.setDirAndGo)
        self.dirs.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT,fill=BOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top,width=50,textvariable=self.cwd)
        self.dirn.bind('<return>',self.doLS)
        self.dirn.pack()

        self.bfm = Frame(self.top)



