# Example taken from https://github.com/heuer/segno/issues/88
# 2023/11 Vincent Rouvreau - Modified for personnal use

import io
import segno
from PIL import Image, ImageOps

qr = segno.make_qr('https://reseau-loops.github.io/2023/11/23/cafe-loops', error='H')
out = io.BytesIO()
qr.save(out, kind='png', scale=100)
out.seek(0)
img = Image.open(out)

width, height = img.size

# How big the logo we want to put in the qr code png
logo_size = 1100

# Open the logo image
logo = Image.open('tasse_b.png').convert("RGBA")

# Calculate xmin, ymin, xmax, ymax to put the logo
xmin = ymin = int((width / 2) - (logo_size / 2))
xmax = ymax = int((width / 2) + (logo_size / 2))

# resize the logo as calculated
logo = logo.resize((xmax - xmin, ymax - ymin))

# put the logo in the qr code
img.paste(logo, (xmin, ymin, xmax, ymax))

img.save('qrcode.png')

img = Image.open("qrcode.png").convert("L")
img = ImageOps.colorize(img, black="red", white="white")
img.save('qrcode.png')

