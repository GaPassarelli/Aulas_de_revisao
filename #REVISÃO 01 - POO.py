#REVISÃO 01 - POO
#AC 01

def eh_primo(n):
    if n < 2:
        return False

    for i in range (2, n):
        if n % i == 0:
            return False
    return True

def lista_primo (n):
    lista_primo = []
    
    for i in range (2, n):
        if eh_primo(i):
            lista_primo.append(i)
    return lista_primo

def conta_primos (s):
    dict_primo = {}
        
    for i in s:
        if eh_primo(i):
            dict_primo [i] = dict_primo.get(i, 0) + 1
    return dict_primo

def eh_armstrong (n):
    if n < 0:
        return False
    
    dig = len(str(n))
    soma = 0
    
    for carac in str(n):
        valor = int(carac)**dig
        soma = soma + valor
        
    if n == soma:
        return True
    else:
        return False
        
def eh_quase_armstrong (n):
    if eh_armstrong(n):
         return False
     
    elif eh_armstrong(n+1) or eh_armstrong(n-1):
        return True
    else:
        return False
                  
n = int(input())
x = eh_primo(n)

print (f'{n} é primo, {x}!')

n = int(input())
x = lista_primo(n)

print (f'lista primo, {x}!')

n = int(input())
x = eh_armstrong(n)

print (f'{n} é armstrong, {x}!')

n = int(input())
x = eh_quase_armstrong(n)

print (f'{n} é quase armstrong, {x}!')