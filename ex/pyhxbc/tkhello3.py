import Tkinter

top = Tkinter.Tk()

hello = Tkinter.Label(top,text='Hello World!')
hello.pack()

quit = Tkinter.Button(top,text='Hello World!',command=top.quit,bg='red',fg='white')
quit.pack()

Tkinter.mainloop()