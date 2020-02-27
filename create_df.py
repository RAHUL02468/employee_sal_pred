

import tkinter as tk
from   tkinter import messagebox as msg
import pandas as pd

from pandastable import Table
from tkintertable import TableCanvas

root=tk.Tk()
root.wm_title('Build and Display DF from csv')
canvas1 = tk.Canvas(root, width = 200, height = 100,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Display DF')
label1.config()
canvas1.create_window(100, 20, window=label1)

def conv_to_df():
     empsal_df = pd.read_csv("empsal.csv",index_col='empno',parse_dates=['dob'])
     empsal_df.dropna(axis=0,how='any',inplace=True)
     empsal_df['conv']=empsal_df.salary*0.10
     empsal_df['total']=empsal_df.salary+empsal_df.hra+empsal_df.conv
     canvas2 = tk.Canvas(root, height=300, width=400,relief='raised') 
     canvas2.pack()
     table = Table(canvas2, dataframe=empsal_df,read_only=True)
     table.show()


def _quit():
    root.quit()     # stops mainloop
    root.destroy()
    
button1 = tk.Button(text='Display', command=conv_to_df)
canvas1.create_window(100, 50, window=button1)

button5 = tk.Button(text="Quit", command=_quit)
canvas1.create_window(100,80,window=button5)

root.mainloop()


