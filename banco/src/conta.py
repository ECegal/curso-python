import datetime


class Conta:
    __slots__ = ['numero', 'cliente',
                 '_saldo', 'historico',
                 'limite']

    # variavel de classe
    _quantidade_de_contas = 0

    # dunder __init__

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.cliente = cliente  # Agragação
        self._saldo = saldo
        self.historico = Historico()  # Composição
        self.limite = limite
        Conta._quantidade_de_contas += 1

    def __str__(self):
        return f'Numero:{self.numero} Cliente:{self.cliente} Saldo:{self._saldo}'

    def deposita(self, valor):
        self.historico.transacoes.append(f'Depósito no valor de {valor}')
        self._saldo += valor

    def saca(self, valor):
        if valor <= self._saldo + self.limite:
            self.historico.transacoes.append(f'Saque no valor de {valor}')
            self._saldo -= valor
            return True
        else:
            return False

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.exibe()

    def tranfere_para(self, conta_destino, valor):
        if self.saca(valor):
            self.historico.transacoes.append(f'Transferencia para a conta {conta_destino.numero}, no valor de {valor}')
            conta_destino.deposita(valor)

    def atualiza(self,taxa):
        self._saldo += self._saldo * taxa


    # para pegar um valor
    # getter
    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def get_quantidade_de_contas(cls):
        return cls._quantidade_de_contas


class ContaCorrente(Conta):

    def atualiza(self,taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10

class ContaPoupanca(Conta):
    def atualiza(self,taxa):
        self._saldo += self._saldo * taxa * 3


class Cliente:

    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco


class Historico:

    def __init__(self):
        self.data_de_abertura = datetime.datetime.now()
        self.transacoes = []

    def exibe(self):
        for movimentacao in self.transacoes:
            print(movimentacao)

class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    #propriedades
    def roda(self, conta):
        print(conta.saldo)
        conta.atualiza(self._selic)
        self._saldo_total += conta.saldo


class Banco:
    _contas = []

    def adiciona(self, conta):
        self._contas.append(conta)

    def pega_conta(self, indice):
        return self._contas[indice]

    def pega_total_contas(self):
        return len(self._contas)

if __name__ == '__main__':
    c = Conta('123-4', 'Joao',1000.0)
    cc = ContaCorrente('123-5','Jose', 1000.0)
    cp = ContaPoupanca('123-6','Maria',1000.0)

    c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(c.saldo)
    print(cc.saldo)
    print(cp.saldo)

    #print(c)
    #print(cc)
    #print(cp)

    banco = Banco()
    banco.adiciona(c)
    banco.adiciona(cc)
    banco.adiciona(cp)

    for indice in range(0, banco.pega_total_contas()):
        print(banco.pega_conta(indice))
