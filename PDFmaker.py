from PIL import Image
import docx2pdf as dtp

HOME = 'c:\\Users\\VD102541\\Desktop\\Misc STuff\\'

dtp.convert(HOME + 'Hello blahblah blah test.docx')








# image = Image.open(r'C:\Users\VD102541\Desktop\Barcodes\One.png')
# imageName = 'test'
# imagePDF = image.convert('RGB')
# imagePDF.save(f'C:\\Users\\VD102541\\Desktop\\Barcodes\\{imageName}.pdf')
print('end')
