class Funcionario:


    def __init__(self, nome, codigo, cargo,salario):
        self._nome = nome
        self._codigo = codigo
        self._cargo = cargo
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def calcula_bonificacao(self):
        return self._salario * 0.1

if __name__ == '__main__':
    pass
