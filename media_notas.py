print('***************************************')
print('*************Média Notas***************')
print('***************************************')

notas = []
notasstring = []
for x in range(1,5):
    nota = input('insira a nota {}:'.format(x))
    notas.append(int(nota))
    notasstring.append(nota)
valor = ''.join(str(notas))
print('Suas notas foram: {}'.format(valor))
print('A média é: {}'.format(sum(notas)/len(nota)))