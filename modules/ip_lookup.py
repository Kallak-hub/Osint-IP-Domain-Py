import requests

def ip_lookup(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        print(f"IP: {data.get('query')}")
        print(f"País: {data.get('country')}")
        print(f"Cidade: {data.get('city')}")
        print(f"ISP: {data.get('isp')}")

    except Exception as e:
        print(f"Erro: {e}")