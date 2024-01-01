import qrcode
lnk=input("Enter the link to create the QR Code : ")
name=input("Enter the name to save the QR by it : ")
img = qrcode.make(lnk)
img.save(name)
img.show()