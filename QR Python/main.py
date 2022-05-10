import pyqrcode
from pyqrcode import QRCode

url = pyqrcode.create("https://first-light-switch.web.app/")
url.svg("Linterna.svg",scale=8)