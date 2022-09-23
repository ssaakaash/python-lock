# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import ttk
from datetime import date

class Election:
    def __init__(self,root):
        self.frame=ttk.Frame(root,height=800,width=1000)
        root.title('NCFE Election')
        self.frame.grid(column=0,row=0, sticky=(N,S,E,W))
        root.columnconfigure(0,weight=1)
        root.rowconfigure(0,weight=1)

        ttk.Label(self.frame,text=f'ELECTIONS').grid(row=2,column=2)
        yr=date.today().year
        ttk.Label(self.frame,text=f'{yr}-{yr-1999}').grid(row=3,column=2)
        ttk.Button(self.frame,text='Setup').grid(row=4, column=1)
        ttk.Button(self.frame,text='Start').grid(row=4, column=3)

        logo=PhotoImage(file=r'C:\Users\Vipra\AppData\Local\Programs\Python\Python39\12th project\ncfe_logo.gif')
        print(logo)
        img_label = ttk.Label(self.frame, image=logo).grid(row=1,column=2)

root=Tk()
Election(root)
root.mainloop()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("Hello")
    print("Hi")
    print('Hey')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
