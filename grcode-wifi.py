import qrcode
from getpass import getpass
import os

try:
    type = "WPA"
    ssid = input("SSID(Nome da Rede): ")
    password = getpass("Password(Senha): ")
    hidden = False

    if not os.path.exists("QRCODE"):
        os.makedirs("QRCODE")
    img = qrcode.make(f"WIFI:T:{type};S:{ssid};P:{password};H:{hidden};;")
    img.save(f"QRCODE/{ssid.upper()}.png")
    print("QRCODE Salvo com Sucesso")

except:
    print("\nOcorreu algum erro!")