from tkinter import Tk, messagebox as mb, filedialog as fd
from tkinter.constants import DISABLED, NORMAL
from tkinter.ttk import Button, Label
from PIL import Image
import os

root = Tk()
root.title("Image to PDF converter")
root.geometry("500x500")

imglist = []    # For creating a list of images
fimgl = []  # List for storing multiple image names
png = True  # If the image chosen is a .png file

def askfile():
    global files, fimg, order, imglist, tm, png
    files = fd.askopenfilenames(title="Choose images", filetypes=(("PNGs", "*.png"), ("JPGs", "*.jpg"), ("All Files", "*.*")))
    for i in files:
        fimgl.append(i)
    if files:
        for j in fimgl:
            if j.endswith(".png"):  # If the image is a PNG:
                png = True
            fnl = Label(root, text=j)
            fnl.pack()
            img = Image.open(j)
            fimg = img.convert('RGB')
            imglist.append(fimg)
            p.config(state=NORMAL)

def convert_pdf():
    global png
    try:
        if png:
            imglist.pop()
        saveloc = fd.asksaveasfilename(title="Save the PDF file")
        if saveloc:
            if saveloc.endswith(".pdf"):
                pass
            else:
                saveloc = saveloc + ".pdf"
            if os.path.exists(saveloc):
                yn = mb.askyesno("Confirm Save As", f"{os.path.basename(saveloc)} already exists.\nDo you want to replace it?")
                if yn:
                    os.remove(saveloc)
                else:
                    convert_pdf()
            fimg.save(saveloc, save_all=True, append_images=imglist)
            mb.showinfo("Done!", "PDF file saved! Click 'OK' to open it")
            os.startfile(saveloc)
            root.quit()
    except Exception as err:
        mb.showerror("Error", err)
        root.quit()

cb = Button(root, text="Add Files", command=askfile)
cb.pack(pady=20)

p = Button(root, text="Convert", command=convert_pdf, state=DISABLED)
p.pack(pady=20)


root.mainloop()
