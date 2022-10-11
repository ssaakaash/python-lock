from tkinter import *
from tkinter import ttk
from datetime import date


# LOGO_PATH = r'C:\Users\Vipra\AppData\Local\Programs\Python\Python39\12th project\ncfe_logo.gif'
LOGO_PATH = '/Users/aakaash/PycharmProjects/project-2022/logo.gif'


class Election:
    def __init__(self, root):
        root.title('NCFE Election')

        mainframe = ttk.Frame(root, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky="N W E S")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.logo = PhotoImage(file=LOGO_PATH)
        self.logo1 = self.logo.subsample(4, 4)

        ttk.Label(mainframe, image=self.logo1).grid(row=0, column=2)

        ttk.Label(mainframe, text='ELECTIONS').grid(row=2, column=2)
        yr = date.today().year

        ttk.Label(mainframe, text=f'{yr}-{yr - 1999}').grid(row=3, column=2)

        ttk.Button(mainframe, text='Setup').grid(row=4, column=1)
        ttk.Button(mainframe, text='Start').grid(row=4, column=3)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)


if __name__ == '__main__':
    root = Tk()
    app = Election(root)
    root.mainloop()
