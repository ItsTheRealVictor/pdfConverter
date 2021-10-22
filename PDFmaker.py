from tkinter import *
from tkinter.filedialog import askopenfilenames

from PIL import Image

root = Tk()


def pickFile():
    global fileName
    fileName = askopenfilenames()

def convertFile():
    try:
        path = fileName
        with open(f'file.pdf', 'wb') as f:
            for file in fileName:
                pdf = Image.open(file)
                pdf.save(file + '.pdf')
            
    except ValueError:
        pass
    


chooseButton = Button(root, text='pick a file', command=pickFile).pack()
convertButton = Button(root, text='convert', command=convertFile).pack()

root.mainloop()
