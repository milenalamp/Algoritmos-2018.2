#leia numero e saldo atual
#operações: D= depósito R=retirada != Operação inválida

n = int(input("Digite seu número"))
saldoA = float(input("Digite seu saldo atual"))
opc = input("Digite D para depósito ou R para retirada")
D = 07

while opc != 0:
    if opc == D:
        deposito = float(input("Valor a ser depositado: "))
        saldoA = saldoA + deposito
        print("Saldo Atual", saldoA)
