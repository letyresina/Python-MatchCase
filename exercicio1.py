'''
    Exercício 1:
    Leia a primeira letra do estado civil de uma pessoa e mostre uma mensagem com a sua descrição 
    (Solteiro, Casado, Viúvo, Divorciado). Mostre uma mensagem de erro, se necessário (o algoritmo
    deve funcionar para letras maiúsculas e minúsculas).
'''

print("S ou s para solteiro \n C ou c para casado \n V ou v para viúvo \n D ou d para divorciado")
estadoCivil = input("Informe a primeira letra do seu Estado Civil: ")

match estadoCivil:
    case "S" | "s":
        print("Seu estado civil é: Solteiro(a).")
    case "C" | "c":
        print("Seu estado civil é: Casado(a).")
    case "V" | "v":
        print("Seu estado civil é: Viúvo(a).")
    case "D" | "d":
        print("Seu estado civil é: Divorciado(a).")
    case _:
        print("Nenhum estado civil selecionado.")

