from tkinter import Tk,Button,Label,IntVar
from tkinter.ttk import Progressbar


class ProgressApp(Tk):

    def __init__(self):
        super().__init__()
        self.value = IntVar()
        self.value.set(5)
        self.progress_bar = Progressbar(self, orient="horizontal", mode="determinate", maximum=100,variable=self.value)
        stop_button = Button(self, text='Stop', command=self.stop_progress_bar)
        start_button = Button(self, text='Start', command=self.start_progress_bar)
        increment_button = Button(self, text='Increment', command=self.increment)

        label = Label(self, text="Progess Bar")

        label.grid(row=0, column=0)
        self.progress_bar.grid(row=0, column=1)
        start_button.grid(row=1,column=0)
        stop_button.grid(row=1,column=1)
        increment_button.grid(row=2,column=0)

    def stop_progress_bar(self):
        self.progress_bar.stop()

    def start_progress_bar(self):
        self.progress_bar.start()
        self.progress_bar.step(10)

    def increment(self):
        self.value.set(self.value.get()+5)



progressApp = ProgressApp()
progressApp.mainloop()