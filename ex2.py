i = 0
antecessor = 0
sucessor = 0

while i < 10:
    n = int(input("Digite 10 números para saber seu sucessor e antecessor: "))
    sucessor = n + 1
    antecessor = n - 1
    i = i + 1
    print("Número sucessor: ",sucessor,"Número antecessor: ",antecessor)
