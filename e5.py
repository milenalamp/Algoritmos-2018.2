print("Calculo do fatorial de um numero =) ")

   # leia o valor de n
n = int(input("Digite um numero inteiro não-negativo: "))

# inicializa��es
i     = 1  # contador
n_fat = 1

# calcule n!
while i <= n:
   n_fat = n_fat * i
   i = i + 1

print("%d! = %d" %(n, n_fat))
