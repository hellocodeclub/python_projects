from tkinter import Tk,Label,StringVar, OptionMenu


class DropDownApp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200')

        self.gender_selected = StringVar()
        self.gender_selected.set("Select")

        self.dropdown = OptionMenu(self, self.gender_selected, *["Male", "Female"])
        self.dropdown.grid(row=0,column=1)

        self.label = Label(self, text="No Gender Selected")
        self.label.grid(row=1,column=1)

        self.gender_selected.trace("w", callback=self.update_label)


    def update_label(self, *args):
        self.label.configure(text="Selected gender is {}".format(self.gender_selected.get()))

app = DropDownApp()
app.mainloop()