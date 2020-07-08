import pyqrcode
from time import sleep, ctime
from os import startfile

fileName = ctime().replace(':', '-', 2) + '.png'

qr = pyqrcode.create(input())
qr.png(fileName, scale=6)

sleep(1)
startfile(fileName)