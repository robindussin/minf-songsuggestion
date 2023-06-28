from tkinter import *

class NewWindow(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title('NewWindow')
        self.master = master

        self.lb = Label(self, text='Hello')
        self.lb.grid(column=0, row=0, columnspan=1)

        self.bt1 = Button(self, text="apply Hello", command=self.bt_press)
        self.bt1.grid(column=0, row=1)
    def bt_press(self):
        self.master.basic_lb.config(text="Hello")
        self.destroy()

