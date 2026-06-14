import requests
import time

def ip_lookup(ip):

    print("Carregando informações do endereço IP...")

    req_api = requests.get(f"http://ipwho.is/{ip}")
    ip_data = req_api.json()

    time.sleep(2)

    print("\nIP alvo        :", ip)
    print("Tipo de IP     :", ip_data["type"])
    print("País           :", ip_data["country"])
    print("Código País    :", ip_data["country_code"])
    print("Cidade         :", ip_data["city"])
    print("Continente     :", ip_data["continent"])
    print("Código Cont.   :", ip_data["continent_code"])
    print("Região         :", ip_data["region"])
    print("Código Região  :", ip_data["region_code"])
    print("Latitude       :", ip_data["latitude"])
    print("Longitude      :", ip_data["longitude"])

    lat = int(ip_data["latitude"])
    lon = int(ip_data["longitude"])

    print("Maps           :", f"https://www.google.com/maps?={lat},{lon}")
    print("CEP            :", ip_data["postal"])
    print("Código DDI     :", ip_data["calling_code"])
    print("Capital        :", ip_data["capital"])
    print("Fronteiras     :", ip_data["borders"])
    print("Bandeira       :", ip_data["flag"]["emoji"])
    print("Domínio        :", ip_data["connection"]["domain"])
    print("ID Fuso        :", ip_data["timezone"]["id"])