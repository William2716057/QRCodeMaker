import pyqrcode
import png
from pyqrcode import QRCode


string = "This is a string"

#generate QR code
QRcode = pyqrcode.create(string)

QRcode.png('qr_image', scale=6)



#print(QRcode)


