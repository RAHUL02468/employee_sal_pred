from   tkinter import messagebox as msg
import sys
import pandas as pd
import os.path
import csv
from tkintertable import TableCanvas
import tkinter as tk
root=tk.Tk()
root.wm_title('Displaying the CSV file in Tkintertable')
#root.geometry('1000x600')
#root.configure(bg='orange')

canvas1 = tk.Canvas(root, width = 200, height = 100,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Display CSV')
label1.config()
canvas1.create_window(100, 10, window=label1)

def create_csv():
     try:
          # Now display the CSV in 'tkintertable' widget
          canvas2= tk.Canvas(root, height=200, width=400,relief='raised') 
          canvas2.pack()
          #button = tk.Button(master=root, text="Quit", command=_quit)
          #button.pack(side=tk.RIGHT)
          table = TableCanvas(canvas2, read_only=True)
          table.importCSV('empsal.csv')
          table.show()
        
     except FileNotFoundError as e:
          msg.showerror('Error in opening file', e.msg)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()
    
button1 = tk.Button(text='Display', command=create_csv)
canvas1.create_window(100, 50, window=button1)

button2 = tk.Button(text="Quit", command=_quit)
canvas1.create_window(100,80,window=button2)

root.mainloop()
