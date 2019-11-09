
class Funcionario:

    def __init__(self, nome, codigo, salario):
        self.nome = nome
        self.codigo = codigo
        self.salario = salario

    def calcula_bonificacao(self):
        return self.salario * 0.10


class Gerente(Funcionario):

    def __init__(self, nome, codigo, salario, senha):
        super().__init__(nome, codigo, salario)
        self.senha = senha

    # sobrescrita
    def calcula_bonificacao(self):
        return self.salario * 0.20

    def autentica(self, senha):
        if senha == self.senha:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.nome}, Salario R$ {self.salario}'

class Caixa(Funcionario):

    def __init__(self, nome, codigo, salario):
        super().__init__(nome, codigo, salario)

    def calcula_bonificacao(self):
        return self.salario * 0.15




class Bonificacao:

    def __init__(self):
        self.valor = 0.0

    def insere_bonificacao(self, funcionario):

        # Polimorfismo
        if isinstance(funcionario, Funcionario):
            self.valor += funcionario.calcula_bonificacao()

class Cliente:

    def calcula_bonificacao(self):
        return 100000.0





gerente = Gerente('Fernando', '1234', 100.0, '123456')
print(gerente)
caixa = Caixa('Thiago', '1234', 100.0)
print(caixa.nome)


controle_de_bonificacoes = Bonificacao()

controle_de_bonificacoes.insere_bonificacao(gerente)
controle_de_bonificacoes.insere_bonificacao(caixa)
cliente = Cliente()


controle_de_bonificacoes.insere_bonificacao(cliente)
print(controle_de_bonificacoes.valor)


gerente = Gerente('Fernando', '1234', 100.0, '123456')
print(gerente)
caixa = Caixa('Thiago', '1234', 100.0)
print(caixa.nome)


controle_de_bonificacoes = Bonificacao()

controle_de_bonificacoes.insere_bonificacao(gerente)
controle_de_bonificacoes.insere_bonificacao(caixa)
cliente = Cliente()


controle_de_bonificacoes.insere_bonificacao(cliente)
print(controle_de_bonificacoes.valor)



# gerente = Gerente('Fernando', '1234', 100.0, '123456')
# print(gerente.nome)
# print(gerente.calcula_bonificacao())
# print(gerente.autentica('123456'))
#
#
# funcionario = Funcionario('Joao', '123', 100.0)
# print(funcionario.nome)
# print(funcionario.calcula_bonificacao())
