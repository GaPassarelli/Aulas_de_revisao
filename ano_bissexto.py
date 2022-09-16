inicio = int(input())
fim = int(input())

quantidade = 0

for ano in range (inicio, fim+1):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
        quantidade = quantidade + 1
        print(ano)

print("bissextos:", quantidade)
