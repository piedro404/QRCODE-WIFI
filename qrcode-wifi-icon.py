import qrcode
from getpass import getpass
import os
from qrcode.image.styledpil import StyledPilImage

try:
    type = "WPA"
    ssid = input("SSID(Nome da Rede): ")
    password = getpass("Password(Senha): ")
    hidden = False
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_H)

    if not os.path.exists("QRCODE"):
        os.makedirs("QRCODE")
    qr.add_data(f"WIFI:T:{type};S:{ssid};P:{password};H:{hidden};;")
    try:
        img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="imagem/signal.png")
    except:
        img = qr.make_image()
        
    img.save(f"QRCODE/{ssid.upper()}.png")
    print("QRCODE Salvo com Sucesso")

except:
    print("\nOcorreu algum erro!")
