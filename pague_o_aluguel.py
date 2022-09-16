import math
valor_total = int(input())
valor_parcela = int(input())

quant_parcelas = math.ceil(valor_total / valor_parcela)

for index in range (0, quant_parcelas):
    print("pagamento:", index+1)
    antes = valor_total - index * valor_parcela
    depois = valor_total - (index+1) * valor_parcela
    if depois < 0:
        depois = 0
    print("antes =", antes)
    print("depois =", depois)
    print("-----") 
