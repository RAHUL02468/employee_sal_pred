
import tkinter as tk
from   tkinter import messagebox as msg
import pandas as pd
import matplotlib.pyplot as plt
from pandastable import Table
from tkintertable import TableCanvas

root=tk.Tk()
root.wm_title('Display and Plot State wise Sum of data')
canvas1 = tk.Canvas(root, width = 400, height = 100,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Display and Plot State wise Sum of datas')
label1.config()
canvas1.create_window(200, 20, window=label1)

def bar_graph():
     pd.set_option('display.max_rows', 500)
     pd.set_option('display.max_columns', 500)
     pd.set_option('display.width', 1000)
     empsal_df = pd.read_csv("empsal.csv",index_col='empno',parse_dates=['dob'])
     empsal_df.dropna(axis=0,how='any',inplace=True)
     empsal_df['conv']=empsal_df.salary*0.10
     empsal_df['total']=empsal_df.salary+empsal_df.hra+empsal_df.conv
     mean_list = empsal_df.groupby(['state'])['salary','hra','conv','total'].sum()
     mean_list.plot(kind='bar')
     canvas2 = tk.Canvas(root, height=300, width=400,relief='raised') 
     canvas2.pack()
     table = Table(canvas2, dataframe=mean_list,read_only=True)
     table.show()
     plt.title('State Wise Sum Figures Of\n salary, hra, conv & total')
     plt.xlabel('States-->')
     plt.ylabel('Sum Figures')
     plt.tight_layout()
     plt.legend(loc='best')
     plt.show()


def _quit():
    root.quit()     # stops mainloop
    root.destroy()
    
button1 = tk.Button(text='Display', command=bar_graph)
canvas1.create_window(200, 50, window=button1)

button5 = tk.Button(text="Quit", command=_quit)
canvas1.create_window(200,80,window=button5)

root.mainloop()
