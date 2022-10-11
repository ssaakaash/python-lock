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
        self.logo1 = self.logo.subsample(3, 3)

        ttk.Label(mainframe, image=self.logo1).grid(row=0, column=2)

        heading = ttk.Label(mainframe, text='ELECTIONS')
        heading['font'] = "Alta_light", 150
        heading.grid(row=2, column=2)
        yr = date.today().year

        year = ttk.Label(mainframe, text=f'{yr}-{yr - 1999}')
        year['font'] = "Alta_light", 80
        year.grid(row=3, column=2, sticky='N')

        Button(mainframe, text='Set up', font='TkHeadingFont 30', bg='#323232')\
            .grid(row=4, column=1, sticky='N S E W')
        Button(mainframe, text='Start', font='TkHeadingFont 30', bg='#323232')\
            .grid(row=4, column=3, sticky='N S E W')

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        for n in range(mainframe.grid_size()[1]):
            mainframe.rowconfigure(n, weight=1)
            mainframe.columnconfigure(n, weight=1)


if __name__ == '__main__':
    root = Tk()
    #root.attributes('-fullscreen', True)
    root.state('zoomed')
    app = Election(root)
    root.mainloop()
