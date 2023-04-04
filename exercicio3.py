'''
    Exercício 3:
    Faça um algoritmo que verifica se um número inteiro informado pelo usuário é múltiplo de 3.
'''

num = int(input("Informe um número inteiro qualquer: "))
conta = num % 3

match conta:
    case 0:
        print(f"O número {num} é múltiplo de 3.")
    case 1 | 2:
        print(f"O número {num} não é múltiplo de 3.")
    case _:
        print(f"Nenhum número informado.")
