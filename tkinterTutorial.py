# from tkinter import *

# # ***************Example 1)**********************
# #This is demonstrating how to put labels using the grid method and rows/columns
# root = Tk()

# labelWidget = Label(root, text='asdfas').grid(row=0, column=2)
# otherWidget = Label(root, text='xbcvxcvb').grid(row=1, column=1)
# anotherWidget = Label(root, text='fslfjslfjskdfj').grid(row=2, column=3)

# root.mainloop()

#************************************************************************Example 2)***************************************************************************************
# #This demonstrates stuff about buttons
# root = Tk()
# heresAButton = Button(root, text='Click me bruh', state=DISABLED).grid(row=0, column=0) #disabled state greys out the button
# anotherButton = Button(root, text='click me too', padx=50).grid(row=1, column=0) #padx changes the width of the button
# buttonyButton = Button(root, text='blahblah', pady=50).grid(row=2, column=2) #pady changes the height

# #How do you get a button to do something?
# #first create a function

# def showButtonBoi():
#     buttonLabel = Label(root, text='So sick bro').grid(row=5, column=0)
# def clearButtonBoi():
#     buttonLabel = Label(root, text='                                  ').grid(row=5,column=0)

# #use the command parameter to call the function when you click the button
# boiButton = Button(root, text="Show it", command=showButtonBoi).grid(row=3, column=4)
# clearBoiButton = Button(root, text='clear', command=clearButtonBoi).grid(row=3, column=3)
# root.mainloop()


#*************************************************************************Example 3)*******************************************************************************

# root = Tk()

# #a text entry box
# entryWidget = Entry(root, width=50)
# entryWidget.pack() #change the width with the width parameter with the Entry Method
# entryWidget.insert(0, "Nice") #have some text pre-entered into the input box

# def clicky():

#     clickyLabel = Label(root, text=entryWidget.get())
#     clickyLabel.pack()

# clickyButton = Button (root, text="clicker", command=clicky).pack()
# root.mainloop()


# # print(clickylist)

#*************************************************************************Example 4)**********************************************************************
# a simple calculator
# root = Tk()
# root.title('A simple calculator')

# entryBox = Entry(root, width=35, borderwidth=5)
# entryBox.grid(row=0, column=0, columnspan=3, padx=10, pady=10) #establish the column span (how wide stuff is)

# def clickButton(number):
#     # entryBox.delete(0, END)
#     currentNumber = entryBox.get()
#     entryBox.delete(0, END)
#     entryBox.insert(0, str(currentNumber) + str(number))

# def clickClearButton():
#     entryBox.delete(0, END)

# def clickAddButton():
#     firstNumber = entryBox.get()
#     global firNumber
#     global math
#     math = "addition"
#     firNumber = int(firstNumber)
#     entryBox.delete(0, END)

# def clickEqualsButton():
#     secondNumber = entryBox.get()
#     entryBox.delete(0, END)

#     if math == 'addition':
#         entryBox.insert(0, firNumber + int(secondNumber))

#     if math == 'subtraction':
#         entryBox.insert(0, firNumber - int(secondNumber))

#     if math == 'multiplication':
#         entryBox.insert(0, firNumber * int(secondNumber))
    
#     if math == 'division':
#         entryBox.insert(0, firNumber / int(secondNumber))


# def clickSubtractionButton():
#     firstNumber = entryBox.get()
#     global firNumber
#     global math
#     math = "subtraction"
#     firNumber = int(firstNumber)
#     entryBox.delete(0, END)

# def clickMultiplicationButton():
#     firstNumber = entryBox.get()
#     global firNumber
#     global math
#     math = "multiplication"
#     firNumber = int(firstNumber)
#     entryBox.delete(0, END)

# def clickDivisionButton():
#     firstNumber = entryBox.get()
#     global firNumber
#     global math
#     math = "division"
#     firNumber = int(firstNumber)
#     entryBox.delete(0, END)



# #define your buttons first
# button1 = Button(root, text="1", padx=40, pady=20, command=lambda: clickButton(1))
# button2 = Button(root, text="2", padx=40, pady=20, command=lambda: clickButton(2))
# button3 = Button(root, text="3", padx=40, pady=20, command=lambda: clickButton(3))
# button4 = Button(root, text="4", padx=40, pady=20, command=lambda: clickButton(4))
# button5 = Button(root, text="5", padx=40, pady=20, command=lambda: clickButton(5))
# button6 = Button(root, text="6", padx=40, pady=20, command=lambda: clickButton(6))
# button7 = Button(root, text="7", padx=40, pady=20, command=lambda: clickButton(7))
# button8 = Button(root, text="8", padx=40, pady=20, command=lambda: clickButton(8))
# button9 = Button(root, text="9", padx=40, pady=20, command=lambda: clickButton(9))
# button0 = Button(root, text="0", padx=40, pady=20, command=lambda: clickButton(0))

# additionButton = Button(root, text='+', padx=40, pady=20, command=clickAddButton)
# subtractionButton = Button(root, text='-', padx=40, pady=20, command=clickSubtractionButton)
# multiplicationButton = Button(root, text='*', padx=40, pady=20, command=clickMultiplicationButton)
# divisionButton = Button(root, text='/', padx=40, pady=20, command=clickDivisionButton)
# equalsButton = Button(root, text='=', padx=89, pady=20, command=clickEqualsButton)
# clearButton = Button(root, text='C', padx=40, pady=20, command=clickClearButton)

# #then place them into the root

# button7.grid(row=1, column=0)
# button8.grid(row=1, column=1)
# button9.grid(row=1, column=2)

# button4.grid(row=2, column=0)
# button5.grid(row=2, column=1)
# button6.grid(row=2, column=2)

# button1.grid(row=3, column=0)
# button2.grid(row=3, column=1)
# button3.grid(row=3, column=2)

# button0.grid(row=4, column=0)

# additionButton.grid(row=1, column=3)
# equalsButton.grid(row=4, column=1, columnspan=2)
# clearButton.grid(row=1, column=4)
# subtractionButton.grid(row=3, column=3)
# divisionButton.grid(row=2, column=3)
# multiplicationButton.grid(row=4, column=3)


# root.mainloop()

#****************************************************Example 5************************************************************************
# Open files

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()
root.title("Tutorial example # 5")

root.filename = filedialog.askopenfilename(initialdir="/", #initial dir lets you pick the directory the box opens to 
                                            title="Pick a file", # Upper left hand title of the dialog box
                                            filetypes=(("png files", "*png"), ("all files", "*.*"))) # what file types are allowed to be chosen (the little pulldown
                                                                                                     # menu on the bottom left of the dialog box)

testLabel = Label(root, text=root.filename).pack()
myImage = ImageTk.PhotoImage(Image.open(root.filename))
myImageLabel = Label(image=myImage).pack()

root.mainloop()
