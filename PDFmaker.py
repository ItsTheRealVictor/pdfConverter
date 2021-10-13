from PIL import Image
import docx2pdf

image = Image.open(r'C:\Users\VD102541\Desktop\Barcodes\One.png')
imageName = 'test'
imagePDF = image.convert('RGB')
imagePDF.save(f'C:\\Users\\VD102541\\Desktop\\Barcodes\\{imageName}.pdf')
print('end')
