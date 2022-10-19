# https://python-bloggers.com/2020/07/generate-qr-code-using-python/
# https://pyshark.com/generate-qr-code-using-python/

import pyqrcode
#import pypng

dest = ['https://pyshark.com/generate-qr-code-using-python/',
        '1 Yonge Street, Toronto, Ontario, Canada',
        '+1 (999) 999-9999']
for i in dest:
    myQR = pyqrcode.QRCode(i)
    myQR.png('myqrcode'+str(dest.index(i))+'.png', scale=8)