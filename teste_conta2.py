"""
    Módulo de banco
"""
import datetime

class Conta:

    #dunder __init__
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(conta, valor):
    """
        Função para depositar um valor em uma conta
    """
    conta['saldo'] += valor

    def saca(conta, valor):
    """
        Função para sacar um valor em uma conta
    """
    conta['saldo'] -= valor
    
    def extrato(conta):
    """
        Função para exibir o extrato de uma conta
    """
    print('numero: {}\nsaldo: {}\n'.format(conta['numero'], conta['saldo']))
