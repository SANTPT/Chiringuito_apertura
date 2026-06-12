import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H
COLOR_ELEGANTE = (34, 34, 34)
CREMA = (247, 243, 234)
def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    url = sys.argv[1]
    qr = qrcode.QRCode(version=1, error_correction=ERROR_CORRECT_H, box_size=20, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    imagen = qr.make_image(fill_color=COLOR_ELEGANTE, back_color=CREMA)
    imagen.save('qr_final.png')
    print('QR generado con exito como qr_final.png')
if __name__ == '__main__':
    main()
