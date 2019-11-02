import datetime

class Conta:
    
    __slots__ = ['_numero','_cliente','_saldo','_limite','_historico','_data_abertura']

    _numero_conta = 0

    def __init__(self, cliente, saldo, limite):
        #self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._data_abertura = datetime.datetime.now()
        Conta._numero_conta += 1

    def deposita(self, valor,transferencia = False,conta = None):
        self._saldo += valor
        if not transferencia:
            self._historico.insere(f"Deposito de {valor}")
        else:
            self._historico.insere(f"Recebida transferencia de {conta._numero} no valor de {valor}")

    
    def saca(self, valor):
        if(self._saldo < valor):
            return False
        else:            
            self._saldo -= valor
            self._historico.insere(f"Saque: {valor}")
            return True
    
    def transfere_para(self, destino,valor):
        retirou = self.saca(valor)

        if(retirou):
            destino.deposita(valor,True,self)
            self._historico.insere(f"Transferido para {destino.numero} o valor {valor}")
        
        return retirou


    def extrato(self):
        print("numero: {} \nsaldo:{}".format(self._numero,self._saldo))
        self._historico.mostra()

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




    