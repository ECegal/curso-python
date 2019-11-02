class Conta:

    def __init__(self,numero: str, titular, saldo):
        self.saldo = saldo
        self.titular = titular
        self.numero = numero

if __name__ == '__main__':
    conta = Conta('123-4','Chewie',10000)
    print(conta.titular)