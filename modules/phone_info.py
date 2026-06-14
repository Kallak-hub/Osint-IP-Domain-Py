import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def info_lookup(phone_number):
    print("Carregando informações do número de telefone...")
    numero_usuario = phone_number
    regiao_padrao = "ID"

    numero_processado = phonenumbers.parse(numero_usuario, regiao_padrao)  # VARIABLE PHONENUMBERS
    codigo_regiao = phonenumbers.region_code_for_number(numero_processado)
    operadora = carrier.name_for_number(numero_processado, "en")
    localizacao = geocoder.description_for_number(numero_processado, "id")
    numero_valido = phonenumbers.is_valid_number(numero_processado)
    numero_possivel = phonenumbers.is_possible_number(numero_processado)
    formato_internacional = phonenumbers.format_number(
        numero_processado,
        phonenumbers.PhoneNumberFormat.INTERNATIONAL
    )
    formato_mobile = phonenumbers.format_number_for_mobile_dialing(
        numero_processado,
        regiao_padrao,
        with_formatting=True
    )
    tipo_numero = phonenumbers.number_type(numero_processado)
    fusos_horarios = timezone.time_zones_for_number(numero_processado)
    fuso_formatado = ', '.join(fusos_horarios)

    print(f"\n Informações do número de telefone: {numero_usuario}")
    print(f"\n Localização          : {localizacao}")
    print(f" Código da Região     : {codigo_regiao}")
    print(f" Fuso Horário         : {fuso_formatado}")
    print(f" Operadora            : {operadora}")
    print(f" Número Válido        : {numero_valido}")
    print(f" Número Possível      : {numero_possivel}")
    print(f" Formato Internacional: {formato_internacional}")
    print(f" Formato Mobile       : {formato_mobile}")
    print(f" Número Original      : {numero_processado.national_number}")
    print(f" Código do País       : {numero_processado.country_code}")
    print(f" Número Local         : {numero_processado.national_number}")

    if tipo_numero == phonenumbers.PhoneNumberType.MOBILE:
        print(f" Tipo                 : Número de celular")
    elif tipo_numero == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" Tipo                 : Número de linha fixa")
    else:
        print(f" Tipo                 : Outro tipo de número")