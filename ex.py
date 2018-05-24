mat = []

for y in range(4):
    lista = []

    for k in range(4):
        n = int(input("Digite um número: [{}], [{}]".format(y,k)))
        lista.append(n)
    mat.append(lista)

soma = 0
for i in range (4):
    for j in range(4):
        soma += mat[i][i]

print("Média = ", soma /16)
