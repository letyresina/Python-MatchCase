'''
    Exercício 4:
    Faça um algoritmo que leia o código da palestra de um evento e exiba o local em que ela será 
    realizada, conforme a tabela (presente em documentação).
'''

codigoPalestra = int(input("Informe o código da palestra a seguir: "))

match codigoPalestra:
    case 1:
        print(f"A palestra de código {codigoPalestra} é sobre Linux e será transmitida no Auditório 1.")
    case 2:
        print(f"A palestra de código {codigoPalestra} é sobre Banco de Dados e será transmitida no Auditório 2.")
    case 3:
        print(f"A palestra de código {codigoPalestra} é sobre Windows Server e será transmitida no Auditório 3.")
    case 4:
        print(f"A palestra de código {codigoPalestra} é sobre Lógica de programação e será transmitida no Auditório Principal.")
    case _:
        print("Nenhum código válido selecionado.")