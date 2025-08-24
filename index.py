import qrcode
import numpy as np
from PIL import Image, ImageDraw

# ----------------------
# Step 1: Get text input and make QR matrix
# ----------------------
text = input("Enter text (up to 50 characters): ")  # ask user for text

# create QR code object
qr = qrcode.QRCode(
    version=1,                       # QR size (1 = 21x21)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # low error correction
    box_size=1,                       # size of one module (we will scale later)
    border=0                          # no extra border
)
qr.add_data(text)  # add input text to QR
qr.make(fit=True)  # generate the QR matrix

# convert QR to a numpy array (0 = white, 1 = black)
matrix = np.array(qr.get_matrix(), dtype=int)
print("\nGenerated QR Matrix:")
print(matrix)

# ----------------------
# Step 3: Draw circular QR modules with gradient on background image
# ----------------------
module_size = 10      # size of each QR module in pixels
quiet_zone = 4        # extra space around QR
rows, cols = matrix.shape
img_size = (cols + 2*quiet_zone) * module_size  # final image size

# open background image and resize it to match QR size
bg_image = Image.open("image.png")  
bg_image = bg_image.resize((img_size, img_size))

# create a drawing object to draw on the image
draw = ImageDraw.Draw(bg_image)

# define gradient colors (top to bottom)
start_color = (255, 255, 255)  # start = white
end_color   = (230, 230, 250)  # end = light lavender

# loop through QR matrix to draw modules
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 1:  # only draw black modules
            # compute gradient color based on row
            ratio = r / (rows - 1)  # 0 at top, 1 at bottom
            r_val = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
            g_val = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
            b_val = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
            module_color = (r_val, g_val, b_val)  # final module color

            # calculate module position on image
            x0 = (c + quiet_zone) * module_size
            y0 = (r + quiet_zone) * module_size
            x1 = x0 + module_size
            y1 = y0 + module_size

            # draw a circle (ellipse) for this module
            draw.ellipse([x0, y0, x1, y1], fill=module_color)

# save the final QR image
bg_image.save("qr_with_gradient.png")
print("QR image with circular modules and gradient saved as qr_with_gradient.png")