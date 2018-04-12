soma = 0
valor = int(input("digite um valor: "))
maior = valor
menor = valor

for i in range(4):
	valor = int(input("digite um valor: "))

	if valor > maior:
		maior = valor
	if valor < menor:
		menor = valor
	soma = menor + maior

print("Maior{}, Menor {} Soma= {}".format(maior,menor,soma))
