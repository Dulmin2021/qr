import qrcode

img = qrcode.make("https://google.com")
img.save('my-qr.png')
img.show


