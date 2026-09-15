import qrcode

# Public GitHub Pages URL of the birthday webpage
URL = "https://negirahul1729.github.io/birthday/birthday.html"

# Create a phone-friendly QR code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("birthday-qr.png")

print("QR code generated successfully: birthday-qr.png")
print("URL:", URL)