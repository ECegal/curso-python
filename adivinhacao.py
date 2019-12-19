print('')
print('****************************************')
print('***********jogo da adivinhação**********')
print('****************************************')

#teste

import random
numero_secreto = random.randint(1,100)

total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
#for rodada in range(1,total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    #input sempre lê string, necessário converter
    
    chute = input('Digite o seu número: ')

    #aguarda uma entrada no formato correto (numero)
    while not chute.isdigit():
        chute = input('Digite o seu número: ')
    
    chute = int(chute)
    print('Você digitou: ',chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou!')
        break
    elif maior:
        print('Você errou :(! O seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou :(! O seu chute foi menor que o número secreto')
    
    rodada += 1

print('Fim do jogo')