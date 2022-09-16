num = 0

while True:
    num = int(input("Digite um número de 0 a 10: "))
    if num >= 0 and num <= 10:
        break
    print("Erro! O número deve estar entre 0 e 10.")

for index in range(1, 11):
    resultado = index * num
    print(num, "x", index, "=", resultado)