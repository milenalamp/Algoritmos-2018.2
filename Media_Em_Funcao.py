def media(n1,n2):
    med = (n1+n2)/2
    return med

for i in range(5):
    nomes = str(input("Digite o nome: "))
    nota1 = int(input("Digite a nota1: "))
    nota2 = int(input("Digite a nota2: "))
    med = media(nota1,nota2)

    print("A média do aluno {} é {}".format(nomes, med))
