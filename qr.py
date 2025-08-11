import qrcode

def generate_qr(data, filename, fill_color="black", back_color="white"):
    # Create QR Code object
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Generate image with selected colors
    img = qr.make_image(fill=fill_color, back_color=back_color)
    
    # Save image
    img.save(filename)
    print(f"QR code saved as {filename}")

def main():
    print("QR Code Generator")
    choice = input("Do you want to generate multiple QR codes? (yes/no): ").strip().lower()

    # Optional: User can set color
    fill_color = input("Enter fill color (default is black): ").strip() or "black"
    back_color = input("Enter background color (default is white): ").strip() or "white"

    if choice == "yes":
        count = int(input("How many QR codes do you want to generate? "))
        for i in range(count):
            print(f"\n--- QR Code #{i + 1} ---")
            data = input("Enter the text or URL for the QR code: ")
            filename = input("Enter the filename (with .png extension): ")
            generate_qr(data, filename, fill_color, back_color)
    else:
        data = input("Enter the text or URL for the QR code: ")
        filename = input("Enter the filename (with .png extension): ")
        generate_qr(data, filename, fill_color, back_color)

if __name__ == "__main__":
    main()