import tkinter as tk
from   tkinter import messagebox as msg
import pandas as pd

from pandastable import Table
from tkintertable import TableCanvas

root=tk.Tk()
root.wm_title('Display data Gender Wise')
canvas1 = tk.Canvas(root, width = 400, height = 120,  relief = 'raised')
canvas1.pack()
empsal_df = pd.read_csv("empsal.csv",index_col='empno',parse_dates=['dob'])
empsal_df.dropna(axis=0,how='any',inplace=True)
empsal_df['conv']=empsal_df.salary*0.10
empsal_df['total']=empsal_df.salary+empsal_df.hra+empsal_df.conv

def sum_disp():
     df=empsal_df
     df=df.groupby(['sex'])['salary','hra','conv','total'].sum()
     canvas3 = tk.Frame(root, height=200, width=400,relief='raised') 
     canvas3.pack(fill='both',expand=True)
     table = Table(canvas3, dataframe=df,read_only=True)
     table.show()

def mean_disp():
     df=empsal_df
     df=df.groupby(['sex'])['salary','hra','conv','total'].mean()
     canvas4 = tk.Frame(root, height=200, width=400,relief='raised') 
     canvas4.pack(fill='both',expand=True)
     table = Table(canvas4, dataframe=df,read_only=True)
     table.show()

def std_disp():
     df=empsal_df
     df=df.groupby(['sex'])['salary','hra','conv','total'].std()
     canvas5 = tk.Frame(root, height=200, width=400,relief='raised') 
     canvas5.pack(fill='both',expand=True)
     table = Table(canvas5, dataframe=df,read_only=True)
     table.show()

def _quit():
    root.quit()     # stops mainloop
    root.destroy()
    
button2 = tk.Button(text='Display the sum', command=sum_disp)
canvas1.create_window(200, 20, window=button2)

button3 = tk.Button(text='Display the mean', command=mean_disp)
canvas1.create_window(200, 50, window=button3)

button4 = tk.Button(text='Display the standard deviation', command=std_disp)
canvas1.create_window(200, 80, window=button4)

button5 = tk.Button(text="Quit", command=_quit)
canvas1.create_window(200,110,window=button5)

root.mainloop()
