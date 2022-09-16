num = 0

while True:
    num = int(input("Digite um número de 1 a 26: "))
    if num >= 1 and num <= 26:
        break
    print("Erro! O número deve estar entre 1 e 26.")

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "W", "Y", "Z"]

for x in range(1, num+1):
    linha = ""
    for y in range(1, x+1):
        linha += alfabeto[x-1]
    print(linha)