import requests

def get_headers(url):
    try:
        response = requests.get(url, timeout=10)

        for chave, valor in response.headers.items():
            print(f"{chave}: {valor}")

    except Exception as e:
        print(f"Erro: {e}")