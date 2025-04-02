import qrcode

# Step 1: QRCode object create karo
qr = qrcode.QRCode(
    version=1,  # QR code ka size (1 is smallest, larger numbers mean bigger QR codes)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Each box (square) size in pixels
    border=4  # White border thickness
)

# Step 2: QR Code me data add karo
qr.add_data("www.youtube.com/@Syntax-Coderz")
qr.make(fit=True)  # Automatically best size select karega

# Step 3: Image generate karo aur save karo
img = qr.make_image(fill_color="black", back_color="white")  # Colors customize kar sakte ho
img.save("SyntaxError.png")  # Save as image

print("QR Code Generated Successfully!")
