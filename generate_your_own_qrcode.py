#Generate your own QR Code
#VRIMCAS
#Packages required pyqrcode,pypng

import pyqrcode 
import png 
from pyqrcode import QRCode 
  

data = "https://vrimcas.com"
qr = pyqrcode.create(data) 
qr.png("myqrcode.png", scale = 6) 