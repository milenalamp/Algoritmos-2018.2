valor = float(input("Digite o valor do produto: "))
qt_parcelas = int(input("Digite a quantidade de parcelas: "))

if qt_parcelas == 1:
    if valor < 300:
        valor = valor
    elif valor >= 300 and valor <= 500:
        valor = valor*0.9
    elif valor > 500:
        valor = (valor*0.75)
    print("O preço final é: R$ ", valor, "parcelando em ", qt_parcelas, "X de R$", valor)
if qt_parcelas == 2:
    valor = valor
    valor_parcela = valor/2
    print("O preço final é: R$ ", valor, "parcelando em ", qt_parcelas, "X de R$", valor_parcela)

if qt_parcelas == 3:
    if valor <= 1100:
        aux = valor*0.10
        valor = aux + valor
    if valor > 1100:
        aux = valor*0.20
        valor = aux + valor
    valor_parcela = valor/3
    print("O preço final é: R$ {:.2f} parcelando em {:.2f} X de R$".format( valor , valor_parcela))

if qt_parcelas == 4:
    valor = valor
    valor_parcela = valor/4
    print("O preço final é: R$ ", valor, "parcelando em ", qt_parcelas, "X de R$", valor_parcela)

if qt_parcelas == 5:
    aux = valor*0.25
    valor = aux+valor
    valor_parcela = valor/5
    print("O preço final é: R$ ", valor, "parcelando em ", qt_parcelas, "X de R$", valor_parcela)
