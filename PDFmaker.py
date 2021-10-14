# from PIL import Image
# import docx2pdf as dtp

# HOME = 'c:\\Users\\VD102541\\Desktop\\Misc STuff\\'

# dtp.convert(HOME + 'Hello blahblah blah test.docx')




# Import Module
import tkinter as tk
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showinfo
from pathlib import Path
import img2pdf
  
# Create Object
root = tk.Tk()
root.title('Pick a file, dude')
root.resizable(True, True)
root.geometry('400x200')

def pickFile():
    fileNames = askopenfilenames(title='Open Files', initialdir = '/')
    tk.Label(root, text=f'The File you have chosen is\n{fileNames}').pack()

openButton = tk.Button(root, text = "pick a file", command = pickFile).pack(expand=True)

root.mainloop()

# image = Image.open(r'C:\Users\VD102541\Desktop\Barcodes\One.png')
# imageName = 'test'
# imagePDF = image.convert('RGB')
# imagePDF.save(f'C:\\Users\\VD102541\\Desktop\\Barcodes\\{imageName}.pdf')
print('end')
