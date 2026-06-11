import pyfiglet
import os

from modules.dns_lookup import dns_lookup
from modules.whois_lookup import whois_lookup
from modules.ip_lookup import ip_lookup
from modules.headers import get_headers
from modules.port_scan import port_scan


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(pyfiglet.figlet_format("Kallak-Hub", font="slant"))


def funcionar():
    while True:
        limpar()
        banner()

        print("[1] DNS Lookup")
        print("[2] Whois")
        print("[3] Geolocalizar IP")
        print("[4] HTTP Headers")
        print("[5] Port Scan")
        print("[0] Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            dominio = input("Domínio: ")
            dns_lookup(dominio)

        elif opcao == "2":
            dominio = input("Domínio: ")
            whois_lookup(dominio)


        elif opcao == "3":
            ip = input("IP: ")
            ip_lookup(ip)

        elif opcao == "4":
            url = input("URL: ")
            get_headers(url)

        elif opcao == "5":
            host = input("IP ou domínio: ")
            port_scan(host)

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")
            input()
            continue

        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    funcionar()