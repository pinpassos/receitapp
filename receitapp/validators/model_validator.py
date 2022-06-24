import re


def RegexValidatorTempoPreparo(value):
    regex_validator = "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
    if not bool(re.match(regex_validator, value)):
        raise Exception('Formato de tempo inválido')


def verifica_se_imagem_valida(file):
    if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise Exception('Formato de imagem inválido')
