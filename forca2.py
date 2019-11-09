from random import randrange


def jogo():
    #arquivo = open('palavras.txt')
    with open('palavras.txt') as arquivo:
    
    #palavras = arquivo.readlines()
        palavras = []
        for linha in arquivo:
            fruta = linha.strip()    
            palavras.append(fruta)
    #arquivo.close()
    #palavras = ['abacaxi', 'maca','banana', 'manga']    
    indice = randrange(0,len(palavras))
    palavra_secreta = palavras[indice]

    saida2 = ['_' for letra in palavra_secreta]

    chances = 6

    linha1 =     ' ________'
    linha2 =     '|        |'
    linhatraco = '|'
    cabeca = linhatraco
    corpo = linhatraco
    perna = linhatraco

    def mensagem_de_boas_vindas():
        print ('******************************')
        print ('Bem vindo ao jogo da forca! o/')
        print ('******************************')


    def print_forca(chances):
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

    mensagem_de_boas_vindas()
    print_forca(6)  

    while chances > 0:
        letra = input('Digite uma letra: ').lower()

        if letra in palavra_secreta:
            posicao = 0
            for letra_secreta in palavra_secreta:
                if letra_secreta == letra:                
                    saida2[posicao] = letra                
                posicao+=1        
        else:
            chances -= 1      


    
        print_forca(chances)

        if '_' not in saida2:                           
            print('Você ganhou!')      
            chances = 0
    
    if '_' in saida2:
        saida2 = list(palavra_secreta)
        print_forca(chances)
        print('Você foi enforcado   :(   !!!')

jogo()