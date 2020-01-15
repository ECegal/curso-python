lista = [12,-2 ,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
soma = 0

print(max(lista))
print(min(lista))

for n in lista:
    if n%2 == 0:
        print('{},'.format(n))

print(lista.count(lista[0]))

for n in lista:
    soma+= n
    
print(soma / len(lista))

soma = 0

for n in lista:
    if(n < 0):
        soma+= n

print(soma)