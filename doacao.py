doacao_vic = 0

while True:
    doacao = float(input())
    if doacao == -1:
        break
    doacao_vic = doacao_vic + doacao

doacao_real = doacao_vic * 2.5

print(f'VC$: {doacao_vic:.2f}')
print(f'R$: {doacao_real:.2f}')