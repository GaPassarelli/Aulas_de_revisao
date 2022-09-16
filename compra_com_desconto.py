quant = 0
valor = float(input("Valor: R$ "))

while(True):
    quant = int(input("Insira a quantidade: "))
    if (quant <= 40):
        break

    print("Valor Inválido. Inserir número igual ou inferior a 40")

subtotal = quant * valor

desconto = (subtotal * 0.10) + (subtotal * quant * 0.01)
valor_final = subtotal - desconto

print(f"O seu valor sem desconto é de R$ {subtotal:.2f}")
print(f"O seu valor com desconto é de R$ {valor_final:.2f}")

