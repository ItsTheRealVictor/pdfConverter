from tkinter import *
from tkinter.filedialog import askopenfilenames

from PIL import Image

root = Tk()

def pickFile():
    global fileName
    fileName = askopenfilenames()

def convertFile():
    try:
        path = fileName[0]
        pdf = Image.open(path)
        pdf.save(path + '.pdf')
    except ValueError:
        pass


chooseButton = Button(root, text='pick a file', command=pickFile).pack()
convertButton = Button(root, text='convert', command=convertFile).pack()

root.mainloop()
