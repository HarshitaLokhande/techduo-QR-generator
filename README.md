🎨 Advanced QR Code Generator

This project generates stylized QR codes with:

Circular modules (instead of square blocks)

Gradient colors

Custom background image

All done using Python, NumPy, Pillow (PIL), and qrcode library.

🚀 Features

✅ Generate QR codes from any text (up to 50 characters)
✅ Apply gradient colors to QR modules
✅ Use circular shapes instead of default square blocks
✅ Overlay QR code on a custom background image

🛠️ Requirements

Install dependencies before running:

pip install qrcode[pil] numpy pillow

📌 Usage

Place your background image in the project folder (example: image2.png)

Run the script:

python qr_generator.py


Enter your text when prompted (up to 50 characters).

The styled QR code will be saved as:

qr_with_gradient.png

🎨 Example Output

A QR code with circular dots, gradient coloring, and background image.

(You can add your generated QR image here in the repo!)

📂 Project Structure
📦 advanced-qr-generator
 ┣ 📜 qr_generator.py     # Main script
 ┣ 📜 README.md           # Documentation
 ┣ 🖼️ image2.png          # Background image
 ┗ 🖼️ qr_with_gradient.png # Output QR code

🔧 Customization

Change gradient colors by editing:

start_color = (255, 255, 255)      
end_color   = (230, 230, 250)


Adjust module shape (currently circles, can be squares, rounded, etc.)

Use a different background image
