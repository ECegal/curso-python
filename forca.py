palavra_secreta = 'banana'
saida2 = ['_','_','_','_','_','_']
chances = 6

linha1 =     ' ________'
linha2 =     '|        |'
linhatraco = '|'
cabeca = linhatraco
corpo = linhatraco
perna = linhatraco

while chances > 0:
    letra = input('Digite uma letra: ').lower()

    if letra in palavra_secreta:
        posicao = 0
        for letra_secreta in palavra_secreta:
            if letra_secreta == letra:                
                saida2[posicao] = letra
                if '_' not in saida2:                   
                   print(saida2)
                   print('Você ganhou!')      
                   chances = 0
            posicao+=1        
    else:
        chances -= 1      


        print(linhatraco)

    print(linha1)
    print(linha2)
    if chances < 6:                
        print('{}{}'.format(linhatraco,'       ()')) #cabeca
    else:
         print(linhatraco)
    if chances <= 4 and chances > 1:
        print('{}{}'.format(linhatraco,'        |')) #corpo
    elif chances == 1:
        print('{}{}'.format(linhatraco,'       /|')) #corpo
    elif chances == 0:
        print('{}{}'.format(linhatraco,'       /|\\')) #corpo
    if chances==3:
        print('{}{}'.format(linhatraco,'        /')) #pernas
    elif chances<=2:
        print('{}{}'.format(linhatraco,'        /\\')) #pernas
    print(linhatraco)
    print(linhatraco)
    print(linhatraco)
    saida = '|' + '  '.join(saida2) 
    print(saida)
if '_' in saida2:
    print('Você foi enforcado   :(   !!!')
