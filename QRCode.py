import qrcode

def generate_qr_code(data, filename):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in pixels
        border=2,  # thickness of the border (default is 4)
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)

# Example usage
data = "https://github.com/bhaveshDotcom"
filename = "qrcode.png"
generate_qr_code(data, filename)
print(f"QR code generated and saved as {filename}") 