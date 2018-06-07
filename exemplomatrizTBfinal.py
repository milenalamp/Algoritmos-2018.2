ordem = int(input("Informe o tamanho da matriz"))

mat = []
for i in range (ordem):
    linha = []
    for j in range (ordem):
      n = int(input("Informe mat [{}] [{}]:".format(i,j)))
      linha.append(n)
    mat.append(linha)

print(mat)
