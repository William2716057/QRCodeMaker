import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image

#qr code to enter
string = "example.com"

#generate QR code
QRcode = pyqrcode.create(string)

#save the QR code as a png image into current directory
QRcode.png('qr_image.png', scale=6)

#access saved image then display
QRImage = Image.open('qr_image.png')
QRImage.show()


