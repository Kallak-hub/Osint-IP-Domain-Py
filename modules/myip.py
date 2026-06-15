import requests

def mostrar_ip():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"\n Seu IP: {Show_IP}")