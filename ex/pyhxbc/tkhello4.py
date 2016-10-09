from Tkinter import *

def resize(ev=None):
    label.config(font='Hevetica -%d bold' % scale.get())

top = Tk()
top.geometry('250x150')

label = Label(top,text='Hello World!')
label.pack(fill=Y,expand=1)

scale = Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)

quit = Button(top,text='Hello World!',command=top.quit,activeforeground='white',activebackground='red')
quit.pack()

mainloop()