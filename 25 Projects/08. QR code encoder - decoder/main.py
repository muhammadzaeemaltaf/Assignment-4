#### Create QR code 


# import qrcode

# data = 'This is python project'

# # Simple QR
# # img = qrcode.make(data)
# # img.save('D:/Governer IT/Python Assignments/Assignment 4/25 Projects/08. QR code encoder - decoder/qrcode.png')


# # Advanced QR
# qr = qrcode.QRCode(
#     version=1,
#     box_size=10,
#     border=5,
# )

# qr.add_data(data)
# qr.make(fit=True)
# img = qr.make_image(fill_color='red', back_color='blue')

# img.save('D:/Governer IT/Python Assignments/Assignment 4/25 Projects/08. QR code encoder - decoder/qrcode1.png')



#### decode qr code

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('D:/Governer IT/Python Assignments/Assignment 4/25 Projects/08. QR code encoder - decoder/qrcode.png')
result = decode(img)
print(result[0].data.decode('utf-8'))