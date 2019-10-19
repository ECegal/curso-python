print('*****************************************************')
print('************Trabalhando com estruturas***************')
print('*****************************************************')

lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

print (max(lista))
print (min(lista))

pares = []
for n in lista:
    if(n%2 == 0):
        pares.append(n)
print(pares)

qtdadefirst = 0
for n in lista:
    if n == lista[0]:
        qtdadefirst += 1
print('Método 1: ',qtdadefirst)
print('Método 2: ',lista.count(lista[0]))

print(sum(lista)/len(lista))

somanegativos = 0
for n in lista:
    if n < 0:
        somanegativos += n

print(somanegativos)