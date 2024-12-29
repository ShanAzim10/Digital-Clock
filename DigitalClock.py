#Digital Clock
from tkinter import *
import time

win=Tk()
win.title('Digital Clock')
win.resizable(0,0)

def present_time():
    display_time=time.strftime('%I:%M:%S %p')
    lbl.config(text=display_time)
    lbl.after(200,present_time)

lbl=Label(win,font=('Arial',150),bg='black',fg='red')
lbl.pack()
present_time()



win.mainloop()