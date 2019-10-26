def soma(*numeros, mensagem = 'soma = '): # o caractere * define multiplos argumentos.
    print(type(numeros))    
    
    resultado = { 'msg': mensagem,
                  'soma' : sum(numeros)}

    #print('{msg}{soma}'.format(msg=mensagem,soma = sum(numeros)))
    print('{msg}{soma}'.format(**resultado))


soma(1,2,3,4,mensagem = 'A soma é ') #Após o varargs, sempre deverá ser definido o próximo parametro
soma(1,2,3,4)

def diz_oi(**mensagem):
    print ('{saudacao}, {pronome} {nome}'.format(**mensagem))

mensagem = {'nome':'Eder','pronome':'Supremo senhor','saudacao' : 'Olá'}
diz_oi(**mensagem)
diz_oi(nome='Joao',pronome ='mestre',saudacao='Bom dia')
