import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image


string = "This is a string"

#generate QR code
QRcode = pyqrcode.create(string)

QRcode.png('qr_image.png', scale=6)

QRImage = Image.open('qr_image.png')
QRImage.show()
#print(QRcode)


