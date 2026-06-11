import whois

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print(f"Domínio: {w.domain_name}")
        print(f"Registrador: {w.registrar}")
        print(f"Criado em: {w.creation_date}")
        print(f"Expira em: {w.expiration_date}")

    except Exception as e:
        print(f"Erro: {e}")