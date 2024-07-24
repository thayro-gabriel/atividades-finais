import os

def limpar_terminal():
    sistema = os.name
    if sistema == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

unidades_comprimentos = ["m", "mm", "km", "cm"]
unidades_volume = ["l", "ml"]
unidades_peso = ["g", "kg", "t", "mg"]
unidades_temperatura = ["c", "k", "f"]

def converter_comprimento(valor, unidade_base, unidade_conversao):
    conversao_para_metros = {
        "m": 1,
        "mm": 0.001,
        "km": 1000,
        "cm": 0.01
    }
    valor_em_metros = valor * conversao_para_metros[unidade_base]

    conversao_de_metros = {
        "m": 1,
        "mm": 1000,
        "km": 0.001,
        "cm": 100
    }
    return valor_em_metros * conversao_de_metros[unidade_conversao]

def converter_volume(valor, unidade_base, unidade_conversao):
    
    conversao_para_litros = {
        "l": 1,
        "ml": 0.001
    }
    valor_em_litros = valor * conversao_para_litros[unidade_base]
    
    conversao_de_litros = {
        "l": 1,
        "ml": 1000
    }
    return valor_em_litros * conversao_de_litros[unidade_conversao]

def converter_peso(valor, unidade_base, unidade_conversao):
    
    conversao_para_gramas = {
        "g": 1,
        "kg": 1000,
        "t": 1000000,
        "mg": 0.001
    }
    valor_em_gramas = valor * conversao_para_gramas[unidade_base]
    
    conversao_de_gramas = {
        "g": 1,
        "kg": 0.001,
        "t": 1e-6,
        "mg": 1000
    }
    return valor_em_gramas * conversao_de_gramas[unidade_conversao]

def converter_temperatura(valor, unidade_base, unidade_conversao):
    
    if unidade_base == "c":
        valor_em_celsius = valor
    elif unidade_base == "k":
        valor_em_celsius = valor - 273.15
    elif unidade_base == "f":
        valor_em_celsius = (valor - 32) * 5/9

    
    if unidade_conversao == "c":
        return valor_em_celsius
    elif unidade_conversao == "k":
        return valor_em_celsius + 273.15
    elif unidade_conversao == "f":
        return valor_em_celsius * 9/5 + 32

# Menu e seleção
print("""
      1 - Converter comprimento
      2 - Converter volume
      3 - Converter peso
      4 - Converter temperatura
      """)
escolher_unidade = int(input("---- Qual opção você escolhe? ~"))

match escolher_unidade:
    case 1:
        limpar_terminal()
        for i, unidade in enumerate(unidades_comprimentos):
            print(f'{i} - {unidade}')
        unidade_base = int(input("Escolha o número da medida base: "))
        numero_base = float(input(f"Digite a medida em {unidades_comprimentos[unidade_base]} a ser convertido: "))
        unidade_conversao = int(input("Agora escolha o número da unidade para qual o número vai ser convertido: "))
        resultado = converter_comprimento(numero_base, unidades_comprimentos[unidade_base], unidades_comprimentos[unidade_conversao])
        print(f'Resultado: {resultado} {unidades_comprimentos[unidade_conversao]}')

    case 2:
        limpar_terminal()
        for i, unidade in enumerate(unidades_volume):
            print(f'{i} - {unidade}')
        unidade_base = int(input("Escolha o número da medida base: "))
        numero_base = float(input(f"Digite a medida em {unidades_volume[unidade_base]} a ser convertido: "))
        unidade_conversao = int(input("Agora escolha o número da unidade para qual o número vai ser convertido: "))
        resultado = converter_volume(numero_base, unidades_volume[unidade_base], unidades_volume[unidade_conversao])
        print(f'Resultado: {resultado} {unidades_volume[unidade_conversao]}')

    case 3:
        limpar_terminal()
        for i, unidade in enumerate(unidades_peso):
            print(f'{i} - {unidade}')
        unidade_base = int(input("Escolha o número da medida base: "))
        numero_base = float(input(f"Digite a medida em {unidades_peso[unidade_base]} a ser convertido: "))
        unidade_conversao = int(input("Agora escolha o número da unidade para qual o número vai ser convertido: "))
        resultado = converter_peso(numero_base, unidades_peso[unidade_base], unidades_peso[unidade_conversao])
        print(f'Resultado: {resultado} {unidades_peso[unidade_conversao]}')

    case 4:
        limpar_terminal()
        for i, unidade in enumerate(unidades_temperatura):
            print(f'{i} - {unidade}')
        unidade_base = int(input("Escolha o número da medida base: "))
        numero_base = float(input(f"Digite a medida em {unidades_temperatura[unidade_base]} a ser convertido: "))
        unidade_conversao = int(input("Agora escolha o número da unidade para qual o número vai ser convertido: "))
        resultado = converter_temperatura(numero_base, unidades_temperatura[unidade_base], unidades_temperatura[unidade_conversao])
        print(f'Resultado: {resultado} {unidades_temperatura[unidade_conversao]}')

        

        