from tkinter import *
import parser
from math import factorial


#making a gui for our calculator

win = Tk()
win.title('Calculator')
win.geometry('437x220+800+50')
#win.configure(bg='lightskyblue')
#win.mainloop()
win.resizable(0, 0)


display = Entry(win, font = "calibri 15 bold")
display.grid(row = 1, columnspan = 6, ipady = 10, sticky = NSEW)


Button(win, text = "1", width = 7, font = "bold", command = lambda : get_variables(1), activeforeground = "blue").grid(row = 2, column = 0, sticky = N+S+E+W)
Button(win, text = "2", width = 7, font = "bold", command = lambda : get_variables(2), activeforeground = "blue").grid(row = 2, column = 1, sticky = N+S+E+W)
Button(win, text = "3", width = 7, font = "bold", command = lambda : get_variables(3), activeforeground = "blue").grid(row = 2, column = 2, sticky = N+S+E+W)
Button(win, text = "4", width = 7, font = "bold", command = lambda : get_variables(4), activeforeground = "blue" ).grid(row = 3, column = 0, sticky = N+S+E+W)
Button(win, text = "5", width = 7, font = "bold", command = lambda : get_variables(5), activeforeground = "blue" ).grid(row = 3, column = 1, sticky = N+S+E+W)
Button(win, text = "6", width = 7, font = "bold", command = lambda : get_variables(6), activeforeground = "blue" ).grid(row = 3, column = 2, sticky = N+S+E+W)
Button(win, text = "7", width = 7, font = "bold", command = lambda : get_variables(7), activeforeground = "blue" ).grid(row = 4, column = 0, sticky = N+S+E+W)
Button(win, text = "8", width = 7, font = "bold", command = lambda : get_variables(8), activeforeground = "blue" ).grid(row = 4, column = 1, sticky = N+S+E+W)
Button(win, text = "9", width = 7, font = "bold", command = lambda : get_variables(9), activeforeground = "blue" ).grid(row = 4, column = 2, sticky = N+S+E+W)

Button(win, text = "AC", width = 7, font = "bold", command = lambda : clear_all(), activebackground = "red" ).grid(row = 5, column = 0, sticky = N+S+E+W)
Button(win, text = "0", width = 7, font = "bold", command = lambda : get_variables(0), activeforeground = "blue" ).grid(row = 5, column = 1, sticky = N+S+E+W)
Button(win, text = ".", width = 7, font = "bold", command = lambda : get_variables("."), activeforeground = "blue" ).grid(row = 5, column = 2, sticky = N+S+E+W)

Button(win, text = "+", width = 7, font = "bold", command = lambda : get_operation("+"), activeforeground = "green" ).grid(row = 2, column = 3, sticky = N+S+E+W)
Button(win, text = "-", width = 7, font = "bold", command = lambda : get_operation("-"), activeforeground = "green" ).grid(row = 3, column = 3, sticky = N+S+E+W)
Button(win, text = "*", width = 7, font = "bold", command = lambda : get_operation("*"), activeforeground = "green" ).grid(row = 4, column = 3, sticky = N+S+E+W)
Button(win, text = "/", width = 7, font = "bold", command= lambda : get_operation("/"), activeforeground = "green" ).grid(row = 5, column = 3, sticky = N+S+E+W)

Button(win, text = "pi", width = 7, font = "bold", command = lambda : get_operation("*3.14"), activeforeground = "green" ).grid(row = 2, column = 4, sticky = N+S+E+W)
Button(win, text = "%", width = 7, font = "bold", command = lambda : get_operation("%"), activeforeground = "green" ).grid(row = 3, column = 4, sticky = N+S+E+W)
Button(win, text = "(", width = 7, font = "bold", command = lambda : get_operation("("), activeforeground = "green" ).grid(row = 4, column = 4, sticky = N+S+E+W)
Button(win, text = "exp", width = 7, font = "bold", command = lambda : get_operation("**"), activeforeground = "green" ).grid(row = 5, column = 4, sticky = N+S+E+W)

Button(win, text = "<-", width = 7, font = "bold", command = lambda : undo(), activebackground = "red" ).grid(row = 2, column = 5, sticky = N+S+E+W)
Button(win, text = "x!", width = 7, font = "bold", command = lambda : fact(), activeforeground = "green" ).grid(row = 3, column = 5, sticky = N+S+E+W)
Button(win, text = ")", width = 7, font = "bold", command = lambda : get_operation(")"), activeforeground = "green" ).grid(row = 4, column = 5, sticky = N+S+E+W)
Button(win, text = "^2", width = 7, font = "bold", command = lambda : get_operation("**2"), activeforeground = "green" ).grid(row = 5, column = 5, sticky = N+S+E+W)
Button(win, text = "Ans", width = 7, font = "bold", command = lambda :calculate(), activeforeground = "blue", bg = "green" ).grid(columnspan = 6, ipady = 7, sticky = N+S+E+W)

i = 0
# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Syntax Error")

def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "x!")

win.mainloop()
