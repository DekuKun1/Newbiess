from time import strftime
from tkinter import *
def time():
    Present_time = strftime('%I:%M:%S %p')
    lbl.config(text = Present_time)
    lbl.after(1000, time)


window= Tk()
window.title('CLOCK')

lbl =Label(window, font = ('calibri', 50, 'bold'),
            background = 'black',
            foreground = 'white')

lbl.pack(anchor = 'center')
time()
window.mainloop()