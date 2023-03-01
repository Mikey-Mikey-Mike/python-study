### Simple Calculator

"""
Simple calculator built following codemy tutorial on Youtube.com
https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5334s
Michael Gannon 01-03-2023

Improvements to original code
1. included arguments + - x / in button calls so that math operation can be determined from a single 
   function. Save rpeating four very similar functions
2. chnaged data type from int --> float to prevent divide by error
3. Simple error checking to return "ERROR" on screen in equals function to prevent entering text 
   or causing and error if pressing equals when no digits are entered.
"""

#### IMPORTS

from tkinter import *
from PIL import ImageTk, Image

#### GLOBALS


#### FUNCTIONS

def makeNumber(number):
    #take existing display
    current = UserInput.get()
    # clear siplay
    UserInput.delete(0,END)
    # add new digit to end of sting and display
    UserInput.insert(0, current + str(number))

def clearInput():
    UserInput.delete(0,END)
    number1 = 0
    number2 = 0

def mathOpp(OppInput):
    global number1
    global action1
    # get current displayed number
    number1 = float(UserInput.get())
    # get selected math operation + - x /
    action1 = OppInput
    # clear display for next number
    UserInput.delete(0,END)

def equals(number1, action1):
    # first number and action provided by button click
    # get 2nd number include error checking
    try:
        number2 = float(UserInput.get())
    except:
        action1 = ""

    # clear display
    UserInput.delete(0,END)
    # perform correct mathematical operation 
    if action1 == "+":
        result = float(number1) + float(number2)
    elif action1 == "-":
        result = float(number1) - float(number2)
    elif action1 == "x":
        result = float(number1) * float(number2)
    elif action1 == "/":
        result = float(number1) / float(number2)
    else:
        result = str("ERROR")

    
    UserInput.insert(0, str(result))

#### PROGRAM BODY

root = Tk()
root.title("Simple Calculator")
# root.iconbitmap("calc.ico")

btnpadx = 30
btnpady = 10

UserInput = Entry(root, width=50, borderwidth=3)
UserInput.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

button0 = Button(root, text='0', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(0)).grid(row=4,column=2)
button1 = Button(root, text='1', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(1)).grid(row=3,column=0)
button2 = Button(root, text='2', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(2)).grid(row=3,column=1)
button3 = Button(root, text='3', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(3)).grid(row=3,column=2)
button4 = Button(root, text='4', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(4)).grid(row=2,column=0)
button5 = Button(root, text='5', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(5)).grid(row=2,column=1)
button6 = Button(root, text='6', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(6)).grid(row=2,column=2)
button7 = Button(root, text='7', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(7)).grid(row=1,column=0)
button8 = Button(root, text='8', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(8)).grid(row=1,column=1)
button9 = Button(root, text='9', padx=btnpadx, pady=btnpady, command=lambda: makeNumber(9)).grid(row=1,column=2)

buttonAdd = Button(root, text='+', padx=btnpadx, pady=btnpady, command=lambda: mathOpp("+")).grid(row=4,column=0)
buttonMinus = Button(root, text='-', padx=btnpadx, pady=btnpady, command=lambda: mathOpp("-")).grid(row=4,column=1)
buttonMultiply = Button(root, text='x', padx=btnpadx, pady=btnpady, command=lambda: mathOpp("x")).grid(row=5,column=0)
buttonDivide = Button(root, text='/', padx=btnpadx, pady=btnpady, command=lambda: mathOpp("/")).grid(row=5,column=1)


buttonClear = Button(root, text='Clear', padx=20, pady=10, command=lambda: clearInput()).grid(row=5,column=2)
buttonExit = Button(root, text='Exit', padx=20, pady=10, command=lambda: root.quit()).grid(row=6,column=2)

buttonEquals = Button(root, text='=', padx=40, pady=20, command=lambda: equals(number1, action1)).grid(row=6, column=0,columnspan=2, padx=20, pady=10, sticky= W+E)

graphic = ImageTk.PhotoImage(Image.open("C:\\users\\W130355\\OneDrive - Vodafone Group\\Documents\\Python\\tkinter\\calc.png"))
labelBottom = Label(root, image=graphic).grid(row=7,column=0, columnspan=3, padx=10, pady=10)

# labelBottom = Label(root, text="My Simple Calculator 01-03-2023").grid(row=7,column=0, columnspan=3, padx=10, pady=10)






root.mainloop()
