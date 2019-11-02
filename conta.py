import datetime

class Conta:
    
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        self.data_abertura = datetime.datetime.now()

    def deposita(self, valor,transferencia = False,conta = None):
        self.saldo += valor
        if not transferencia:
            self.historico.insere(f"Deposito de {valor}")
        else:
            self.historico.insere(f"Recebida transferencia de {conta.numero} no valor de {valor}")

    
    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:            
            self.saldo -= valor
            self.historico.insere(f"Saque: {valor}")
            return True
    
    def transfere_para(self, destino,valor):
        retirou = self.saca(valor)

        if(retirou):
            destino.deposita(valor,True,self)
            self.historico.insere(f"Transferido para {destino.numero} o valor {valor}")
        
        return retirou


    def extrato(self):
        print("numero: {} \nsaldo:{}".format(self.numero,self.saldo))
        self.historico.mostra()

class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Historico:

    def __init__(self):
        self.movimentacoes = []
    
    def mostra(self):
        for movimentacao in self.movimentacoes:
            print(movimentacao)

    def insere(self,mensagem):
        self.movimentacoes.append(mensagem)




    