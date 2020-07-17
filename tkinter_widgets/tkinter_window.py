from tkinter import Tk, Label, Button, IntVar
from tkinter.ttk import Progressbar

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200')


app = App()
app.mainloop()