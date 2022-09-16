numero = 2
while(True):
    numero = int(input("Insira um número maior ou igual a 2: "))
    if numero >= 2:
        break

impar = numero - 1
if impar % 2 == 0:
    impar = numero - 2

par = numero + 1
if par % 2 != 0:
    par = numero + 2

print(impar, par)
