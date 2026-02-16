# cf. requirements.txt for qrcode generation
import segno
from urllib.request import urlopen

qrcode = segno.make_qr("https://reseau-loops.github.io/2026/02/16/cafe-loops")
qrcode.to_artistic(
    background="tasse_b.png",
    target="qrcode.png",
    scale=20,
)
