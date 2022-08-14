from tkinter import *
import base64
class MyWindow():
    def __init__(self,win):
        labl1=Label(window, text='Give Message :')
        labl1.place(x=100, y=50)
        self.lbl3=Label(win, text='Result : ')
        self.lbl3.place(x=100, y=150)
        self.t1=Entry()
        self.t1.place(x=200, y=50)
        self.btn1 = Button(window, text='Encoding')
        self.b1=Button(window, text='Encoding', command=self.encoding)
        self.b1.place(x=100,y=100)
        self.btn2=Button(window, text='Decoding')
        self.b2=Button(window, text='Decoding', command=self.decoding)
        self.b2.place(x=200, y=100)
        self.t2 = Entry()
        self.t2.place(x=200, y=150)
        self.btn3=Button(window, text='EXIT')
        self.b3=Button(window, text='EXIT', command=self.qExit)
        self.b3.place(x=200, y=200)

    def encoding(self):
        message =self.t1.get()
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        self.t2.insert(END, str(base64_message))

    def decoding(self):
        base64_message = self.t1.get()
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        self.t2.insert(END,str(message))

    def qExit(self):
        window.destroy()

window=Tk()
mywin=MyWindow(window)
window.title('Encoding and Decoding')
window.geometry("400x250+10+10")
window.mainloop()