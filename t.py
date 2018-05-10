nomes=[]
for i in range (5):
    nome = input("nome: ")
    nomes.append(nome)
nomes.sort()

for nome in nomes:
    print(nome)
