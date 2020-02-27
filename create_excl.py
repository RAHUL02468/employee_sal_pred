import tkinter as tk
from openpyxl.workbook import Workbook
from   tkinter import messagebox as msg
import sys
import pandas as pd
import os.path
import csv
from tkintertable import TableCanvas

root=tk.Tk()
root.wm_title('Convert csv to Excel')
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Display Excel')
label1.config()
canvas1.create_window(200, 100, window=label1)

def conv_to_exls():
     df=pd.read_csv('empsal.csv')
     df.to_excel("empsal.xlsx",index=None,header=True)
     MsgBox = tk.messagebox.askquestion ('Message','Your excel file is saved as empsal.xlsx')

def _quit():
    root.quit()     # stops mainloop
    root.destroy()
    
button1 = tk.Button(text='Display', command=conv_to_exls)
canvas1.create_window(200, 180, window=button1)

button = tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=tk.RIGHT)

root.mainloop()
