'''
    Exercício 5:
    Faça um algoritmo que exiba um Menu com as opções de um cardápio de restaurante. O cliente deve 
    escolher o código do prato desejado e na sequência, informar se aceita pagar a gorjeta do garçom. 
    Se o usuário aceitar, mostrar o valor final (valor do prato + 10%), caso contrário, mostrar 
    somente o valor do prato.
'''

print("Bem vindo ao Restaurante Dona Dô. Selecione um dos pratos abaixo:")
print("1 para Picanha \n 2 para Lasanha \n 3 para Strogonoff \n 4 para Bife Acebolado \n 5 para Pão com Ovo")

prato = int(input("Informe a opção: "))

# Preços, guardando na variável para simplificar
picanha = 25.00
lasanha = 20.00
strogonoff = 20.00
bifeAcebolado = 15.00
paoComOvo = 5.00

match prato:
    case 1:
        opcionalGorjeta = int(input("Deseja pagar a gorjeta do garçom? \n 1 para Sim \n 2 para Não: "))
        if (opcionalGorjeta == 1):
            gorjeta = picanha * 0.1
            valorTotal = picanha + gorjeta
            print(f"O valor total é de {valorTotal}")
        else: 
            print(f"O valor total é de R$ {picanha}")
    case 2:
        opcionalGorjeta = int(input("Deseja pagar a gorjeta do garçom? \n 1 para Sim \n 2 para Não: "))
        if (opcionalGorjeta == 1):
            gorjeta = lasanha * 0.1
            valorTotal = lasanha + gorjeta
            print(f"O valor total é de {valorTotal}")
        else: 
            print(f"O valor total é de R$ {lasanha}")
    case 3:
        opcionalGorjeta = int(input("Deseja pagar a gorjeta do garçom? \n 1 para Sim \n 2 para Não: "))
        if (opcionalGorjeta == 1):
            gorjeta = strogonoff * 0.1
            valorTotal = strogonoff + gorjeta
            print(f"O valor total é de {valorTotal}")
        else: 
            print(f"O valor total é de R$ {strogonoff}")
    case 4:
        opcionalGorjeta = int(input("Deseja pagar a gorjeta do garçom? \n 1 para Sim \n 2 para Não: "))
        if (opcionalGorjeta == 1):
            gorjeta = bifeAcebolado * 0.1
            valorTotal = bifeAcebolado + gorjeta
            print(f"O valor total é de {valorTotal}")
        else: 
            print(f"O valor total é de R$ {bifeAcebolado}")
    case 5:
        opcionalGorjeta = int(input("Deseja pagar a gorjeta do garçom? \n 1 para Sim \n 2 para Não: "))
        if (opcionalGorjeta == 1):
            gorjeta = paoComOvo * 0.1
            valorTotal = paoComOvo + gorjeta
            print(f"O valor total é de {valorTotal}")
        else: 
            print(f"O valor total é de R$ {paoComOvo}")
