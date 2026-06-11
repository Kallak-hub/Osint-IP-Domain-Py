import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import pycountry

def phone_info(numero_input):
    regiao = ""
    pais = None

    try:
        numero = phonenumbers.parse(numero_input)

        if phonenumbers.is_valid_number(numero):

            regiao = geocoder.description_for_number(numero, "pt")
            operadora = carrier.name_for_number(numero, "pt")
            fuso = timezone.time_zones_for_number(numero)
            formatado = phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

            codigo_pais = phonenumbers.region_code_for_number(numero)
            pais = pycountry.countries.get(alpha_2=codigo_pais)

            print("\nINFORMAÇÕES DO NÚMERO:")
            print("Número:", formatado)
            print("País:", pais.name if pais else "Desconhecido")
            print("ISO:", pais.alpha_3 if pais else "N/A")
            print("Região:", regiao)
            print("Operadora:", operadora)
            print("Fuso horário:", fuso)

        else:
            print("Número inválido")

    except phonenumbers.NumberParseException:
        print("Formato inválido")