import qrcode

image = qrcode.make("hello world,this is Rohan")
image.save('qr_code.png')