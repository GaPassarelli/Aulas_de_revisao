semana = [
    "domingo", 
    "segunda", 
    "terça", 
    "quarta", 
    "quinta",
    "sexta",
    "sabado"
]

dia_da_compra = input("Insira o dia da compra: ") # sabado
prazo = 0

# O prazo não pode ser maior que 6
while True:
    prazo = int(input()) # 6
    if (prazo <= 6):
        break
    print("Erro! O prazo não pode ser superior a 6.")

index_dia_da_compra = 0

# Vamos buscar o index do dia da semana que o usuario fez a compra
for index in range(len(semana)):
    if dia_da_compra == semana[index]:
        index_dia_da_compra = index
        break

# soma o index do dia da compra com o prazo
prazo_final = index_dia_da_compra + prazo

# corrige o index de prazo final caso seja maior que o ultimo index
if prazo_final > (len(semana) - 1):
    prazo_final = prazo_final % len(semana)

# busca o dia da semana relativo ao prazo final
data_entrega = semana[prazo_final]

print("O dia da entrega será ", data_entrega)