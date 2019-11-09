class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total

import abc


class Tributavel(abc.ABC):

    @abc.abstractmethod
    def get_valor_imposto(self):
        pass

if __name__ == '__main__':
    from conta import ContaCorrente, SeguroDeVida, TributavelMixIn

    cc1 = ContaCorrente('123-4','João',1000.0)
    cc2 = ContaCorrente('123-4','Jose',1000.0)
    seguro1 = SeguroDeVida(100.0,'Jose','345-77')
    seguro2 = SeguroDeVida(200.0,'Maria','237-98')

    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)

    maanipulador = ManipuladorDeTributaveis()
    total = maanipulador.calcula_impostos(lista_tributaveis)
    print (total)


