import qrcode  
qr_img = qrcode.make('http://127.0.0.1:8000/SearchPatient')
qr_img.save("qr-img.jpg")