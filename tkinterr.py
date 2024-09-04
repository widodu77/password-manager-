import tkinter as tk
from passwordm import *

m = tk.Tk()

m.title("password manager")

word = tk.Label(m,
                text = "welcome to your password manager",
                height = 1,
                relief = tk.SUNKEN,
                fg = 'white',
                font = ('calibri',18),
                bg = "#550000")

txt_entry = tk.Label(m,
                     text = "enter the master password")

entry = tk.Entry(m)  

word.grid(row = 1, columnspan= 6, padx = 15, pady = 15)

txt_entry.grid(row = 2 , column= 2 )

entry.grid(row=2, column=3)

frame = tk.Frame(m,
                 padx = 20,
                 pady = 30)

button2 = tk.Button(frame,
                text = "add a password",
                command=m.destroy,
                relief = tk.GROOVE,
                fg = 'blue',
                font = ('calibri',18),
                bg = "#CCCCCC"
                )

button3 = tk.Button(frame,
                text = "remove a password",
                command=m.destroy,
                relief = tk.GROOVE,
                fg = 'blue',
                font = ('calibri',18),
                bg = "#CCCCCC"
                )

def password_checking():  
    labeel = tk.Label(m, text = readfile())
    labeel.grid(row = 5, column = 3)


def check_master_password(): 
    s = entry.get() 
    txt = tk.Label(m,
                   text ="fuck you",
                   fg = 'red')
    
    if s != "walid":
        txt.grid(row = 3, column=3)
    else:
        for widget in m.grid_slaves():
            if widget.grid_info()['row'] == 3 and widget.grid_info()['column'] == 3:
                widget.destroy()
        
        frame.grid(row = 4, columnspan = 6, padx = 10, pady = 10)

        button1.grid(row = 1,column=1)

        button2.grid(row = 1, column = 3,  padx = 15 , pady = 15)

        button3.grid(row = 1, column = 5)
            
master_password_check_button = tk.Button(m,
                text = "check password",
                command=check_master_password,
                relief = tk.GROOVE,
                fg = 'blue',
                font = ('calibri',12),
                bg = "#CCCCCC"
                )
       
button1 = tk.Button(frame,
                text = "check all of your passwords",
                command=password_checking,
                relief = tk.GROOVE,
                fg = 'blue',
                font = ('calibri',18),
                bg = "#CCCCCC"
                )


master_password_check_button.grid(row=2, column =4 ) 

'''

frame.grid(row = 3, columnspan = 6, padx = 10, pady = 10)

button1.grid(row = 1,column=1)

button2.grid(row = 1, column = 3,  padx = 15 , pady = 15)

button3.grid(row = 1, column = 5)
'''
m.mainloop()

