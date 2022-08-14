from tkinter import *


def RESET():
    Name.set('')
    Number.set('')


def select():
    return int(select.curselection()[0])

def AddContact():
    contactlist.append([Name.get(),Number.get()])
    Select_set()

def EDIT():
    contactlist[select()]=[Name.get(),Number.get()]
    Select_set()

def DELET():
    del contactlist[select()]
    Select_set()

def VIEW():
    NAME,PHONE = contactlist[select()]
    Name.set(NAME)
    Number.set(PHONE)
def EXIT():
    window.destroy()

def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)


window=Tk()
window.title('Address book')
window.geometry('400x400')
contactlist=[
    
]
Name = StringVar()
Number = StringVar()

frame = Frame(window)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


Select_set()
Label(window,text='Name').place(x=30,y=20)
Entry(window, textvariable = Name).place(x= 100, y=20)
Label(window,text='Phone No.').place(x=30,y=70)
Entry(window, textvariable = 'Number').place(x= 130, y=70)
Button(window,text='ADD',command=AddContact).place(x=50,y=110)
Button(window,text='EDIT',command=EDIT).place(x=50,y=150)
Button(window,text='DELET',command=DELET).place(x=50,y=190)
Button(window,text='VIEW',command=VIEW).place(x=50,y=230)
Button(window,text='EXIT',command=EXIT).place(x=50,y=270)
Button(window,text="RESET",  command = RESET).place(x= 50, y=310)


window.mainloop()