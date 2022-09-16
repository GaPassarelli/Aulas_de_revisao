import math
valor_total = int(input())
valor_parcela = int(input())

quant_parcelas = math.ceil(valor_total / valor_parcela)

index = 0

while index < quant_parcelas:
    antes = valor_total - index * valor_parcela
    depois = valor_total - (index+1) * valor_parcela
    if depois < 0:
           depois = 0
    print("pagamento:", index+1)
    print("antes =", antes)
    print("depois =", depois)
    print("-----")
    if depois == 0:
        break
    index = index + 1
