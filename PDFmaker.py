from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()

def chooseFile():
    global choice
    choice = filedialog.askopenfilenames(title='Choose a file')
    pickLabel = Label(root, text=choice).pack()

pickButton = Button(root, text='Choose File', command=chooseFile).pack()

def convertFile():
    path = choice
    pdf = Image.open(path)
    pdf.save(path)


convertButton = Button(root, text='Convert', command=lambda:convertFile()).pack()

# pdf = Image.open(path)
# pdf.save(r'C:\Users\VD102541\Desktop\Barcodes\20210601_155926.pdf')



root.mainloop()
