from tkinter import *
from tkinter.filedialog import askopenfilenames

from PIL import Image

root = Tk()


def singleFile():
    try:
        path = fileName[0]
        pdf = Image.open(path)
        pdf.save(path + '.pdf')
    except ValueError:
        pass


def multipleFiles():
    try:
        path = fileName
        for file in fileName:
            print(str(file))
            # pdf = Image.open(file)
            # pdf.save(file + '.pdf')
    except ValueError:
        pass


def pickFile():
    global fileName
    fileName = askopenfilenames()

def convertFile():
    if len(fileName) > 1:
        singleFile()
    else:
        multipleFiles()


chooseButton = Button(root, text='pick a file', command=pickFile).pack()
convertButton = Button(root, text='convert', command=convertFile).pack()

root.mainloop()
