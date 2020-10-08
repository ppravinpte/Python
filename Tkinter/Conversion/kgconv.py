from tkinter import *

window = Tk()  # start

def unit_conversion():
    print(e1_value.get()) # get method of StringVar object.
    kg = float(e1_value.get())*1000  #  calculate kg
    t1.insert(END, kg) # put at the end everytime. Value of kg.

    pound = float(e1_value.get())*2.20462  #  calculate pound
    t2.insert(END, pound) # put at the end everytime. Value of pound.

    ounce = float(e1_value.get())*35.247  #  calculate ounce
    t3.insert(END, ounce) # put at the end everytime. Value of ounce.

b1 = Label(window, text = "Kg")
b1.grid(row=0, column=0)

e1_value = StringVar() # it's function.
e1 = Entry(window, textvariable = e1_value)  # it's an area where you can enter a value. 
#Parameter textvariable = Stringvar object which needs to be declared.
#e1_value get value whatever user enters on Entry wizard.
e1.grid(row=0, column=1)


# Button is a function and need parameters. First window as this is present in window. text is displayed with label 'Execute'.
# to display button. Need position as below.
b2 = Button(window, text = "Convert", command= unit_conversion) # command take value as function without (). 
#When press 'Button' then this function will be executed and o/p printed on command line.. 
b2.grid(row=0, column=2) # grid is method allows columns and rows to enter so you've control over positions.


##t1 = Text(window)  # to display output in Text wizard.  Default width*height is very big so need values as per below..

t1 = Text(window, height=1, width=20) 
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20) 
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20) 
t3.grid(row=1, column=2)

window.mainloop() # end