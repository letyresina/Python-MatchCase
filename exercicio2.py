'''
    Exercício 2:
    Faça um programa que receba um número, digitado pelo usuário e mostre o menu para selecionar o
    tipo de cálculo que deve ser realizado. Exiba o resultado do cálculo efetuado.
    Opção 1 - O dobro
    Opção 2 - A metade
    Opção 3 - 10% do número
'''

num = int(input("Informe um número inteiro qualquer: "))

print("Escolha uma das opções a seguir:")
print("1 - Dobro \n 2 - Metade \n 3 - 10%")

opcao = int(input("Informe a opção desejada: "))

match opcao:
    case 1:
        dobro = num * 2
        print(f"O dobro de {num} é {dobro}")
    case 2:
        metade = num / 2
        print(f"A metade de {num} é {metade}")
    case 3:
        porcentagem = num * 0.1
        print(f"A metade de {num} é {porcentagem}")
    case _:
        print("Nenhuma das opções selecionadas.")