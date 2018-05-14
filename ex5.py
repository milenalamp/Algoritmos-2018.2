gabarito = []
print("Gabarito")

for i in range(13):
    N = int(input("Informe a aposta{}: ".format(i+1))
        gabarito.append(N)

aposta = []
print("\n aposta:")

for i in range(13):
    N = int(input("Informe a aposta{}:".format(i+1))
    aposta.append(N)

#Comparar Vetores
acertos: 0
for i in range(13):
    if gabarito[i] == aposta[i]:
        acertos +=1
print("Quantidade de acetos:",acertos)
    if acertos == 13:
        print("GANHADOR, PARABÉNS!")
