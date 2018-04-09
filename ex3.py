
N1 = int(input("Digite um numero "))
N2 = int(input("Digite um numero "))

cont = 0

while N1 >= N2:
    N1 = N1 - N2
    cont +=1

print("Quociente: {} | Resto {}".format(cont,N1))
