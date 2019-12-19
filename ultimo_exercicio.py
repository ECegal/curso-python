import csv
import collections

class Funcionario:
    
    def __init__(self,nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario


class ListaFuncionarios(collections.UserList):

    _dados = []

    def __len__(self):
        




with open('funcionarios.csv', mode = 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
    
