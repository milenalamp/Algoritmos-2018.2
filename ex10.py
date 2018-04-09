
cont = 1

while cont <= 4:
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: \t"))
    cont = cont + 1

    maiorP = peso
    menorP = peso

    if maiorP > peso:
        maiorP = peso
    else:
        menorP = peso
        cont = cont + 1
    print (" Nome: ", maiorP)
