import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)

        print(f"Domínio: {domain}")
        print(f"IP: {ip}")

    except Exception as e:
        print(f"Erro: {e}")

