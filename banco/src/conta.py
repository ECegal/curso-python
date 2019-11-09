import datetime
import abc


class Conta (abc.ABC):
    __slots__ = ['numero', 'cliente',
                 '_saldo', 'historico',
                 'limite']

    # variavel de classe
    _quantidade_de_contas = 0

    # dunder __init__

    @abc.abstractmethod
    def tipo(self):
        pass

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

        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo')
        if(self._saldo < valor):
            raise excecoes.SaldoInsuficienteError('Saldo insuficiente')

        if valor <= self._saldo + self.limite:
            self.historico.transacoes.append(f'Saque no valor de {valor}')
            self._saldo -= valor

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.exibe()

    def tranfere_para(self, conta_destino, valor):
        if self.saca(valor):
            self.historico.transacoes.append(f'Transferencia para a conta {conta_destino.numero}, no valor de {valor}')
            conta_destino.deposita(valor)

    @abc.abstractmethod
    def atualiza(self,taxa):
        pass



    # para pegar um valor
    # getter
    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def get_quantidade_de_contas(cls):
        return cls._quantidade_de_contas


class TributavelMixIn:

    def get_valor_imposto(self):
        pass

import excecoes

class ContaCorrente(Conta, TributavelMixIn):

    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo')
        if(self._saldo < valor):
            raise excecoes.SaldoInsuficienteError('Saldo insuficiente')

        super.saca(valor)

    def atualiza(self,taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        if valor < 0:
            raise ValueError
        else:
            self._saldo += valor - 0.10

    def tipo(self):
        return 'Conta Corrente'

    def get_valor_imposto(self):
        return self._saldo * 0.01


class ContaPoupanca(Conta):

    def atualiza(self,taxa):
        self._saldo += self._saldo * taxa * 3

    def tipo(self):
        return 'Conta Poupanca'

class ContaInvestimento(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

    def tipo(self):
        return 'Conta Investimento'


class SeguroDeVida(TributavelMixIn):

    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 42 + self._valor * 0.05





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
    cc = ContaCorrente('123-4','João',1000.0)

    valor = 5000.0

    try:
        cc.saca(valor)
        print('Saque de  {} realizado com sucesso'.format(valor))
        #print(f'Saque de  {valor} realizado com sucesso')
    except ValueError:
        print('O valor a ser sacado deve ser um número positivo.')

    #c = Conta('123-4', 'Joao',1000.0)
    # cc = ContaCorrente('123-5','Jose', 1000.0)
    # cp = ContaPoupanca('123-6','Maria',1000.0)
    #
    # #c.atualiza(0.01)
    # cc.atualiza(0.01)
    # cp.atualiza(0.01)
    #
    # #print(c.saldo)
    # print(cc.saldo)
    # print(cp.saldo)
    #
    # #print(c)
    # #print(cc)
    # #print(cp)
    #
    # banco = Banco()
    # #banco.adiciona(c)
    # banco.adiciona(cc)
    # banco.adiciona(cp)
    #
    # for indice in range(0, banco.pega_total_contas()):
    #     print(banco.pega_conta(indice))
