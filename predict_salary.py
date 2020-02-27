from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
import os.path
from tkinter import messagebox as msg
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import tkinter as tk


root=tk.Tk()
#root.geometry('1200x600')
#root.configure(bg='indigo')
root.wm_title("Salary Predictor")

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Salary Predictor')
label1.config()
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter year of experience:')
label2.config()
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root,text='') 
canvas1.create_window(200, 140, window=entry1)
def predict_salary():
        try: 
                if(os.path.exists('empsal.csv')):
                    emp_expr_sal_df = pd.read_csv('empsal.csv', usecols = ['expyr', 'salary'])

                    expr = emp_expr_sal_df.iloc[:, :-1].values  
                    salary = emp_expr_sal_df.iloc[:, 1].values
                    
                    
                    X_train, X_test, y_train, y_test = train_test_split(expr, salary, test_size = 1/3,random_state = 0)
                    regressor = LinearRegression()
                    regressor.fit(X_train, y_train)

                    
                    new_expr = DoubleVar()
                    new_expr = float(entry1.get())  
                    new_expr = [[new_expr]]       
                    prediction = regressor.predict(new_expr)    
                    prediction = ("%.2f" % prediction[0])

                    
                    label3 = tk.Label(root, text= 'Expected Salary:')
                    canvas1.create_window(200, 210, window=label3)
    
                    label4 = tk.Label(root, text=str(prediction))
                    canvas1.create_window(200, 230, window=label4)   
                    
                    
        except FileNotFoundError as e:
                msg.showerror('CSV file not found', e)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()

    
button1 = tk.Button(text='Predict', command=predict_salary)
canvas1.create_window(200, 180, window=button1)

button = tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=tk.RIGHT)


root.mainloop()
             
