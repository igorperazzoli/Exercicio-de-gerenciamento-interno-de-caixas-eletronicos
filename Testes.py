from Caixa import Caixa
import unittest


# Testes unitários em função da classe Caixa
class Testes(unittest.TestCase):

    # Teste de depósito simples, em que uma nota de cada tipo é inserida
    def teste_deposito_simples(self):
        caixa = Caixa()
        self.assertEqual(caixa.adicionar_notas("10", 1), True)
        self.assertEqual(caixa.dic_de_notas["10"], 1)
        self.assertEqual(caixa.adicionar_notas("20", 1), True)
        self.assertEqual(caixa.dic_de_notas["20"], 1)
        self.assertEqual(caixa.adicionar_notas("50", 1), True)
        self.assertEqual(caixa.dic_de_notas["50"], 1)
        self.assertEqual(caixa.adicionar_notas("100", 1), True)
        self.assertEqual(caixa.dic_de_notas["100"], 1)

    # Teste de depósito sortido, em que as notas são inseridas em quantidades diferentes e de forma não ordenada
    def teste_deposito_sortido(self):
        caixa = Caixa()
        self.assertEqual(caixa.adicionar_notas("10", 3), True)
        self.assertEqual(caixa.adicionar_notas("50", 20), True)
        self.assertEqual(caixa.adicionar_notas("100", 6), True)
        self.assertEqual(caixa.adicionar_notas("10", 7), True)
        self.assertEqual(caixa.adicionar_notas("20", 30), True)
        self.assertEqual(caixa.adicionar_notas("20", 1), True)
        self.assertEqual(caixa.adicionar_notas("100", 4), True)

        self.assertEqual(caixa.dic_de_notas["10"], 10)
        self.assertEqual(caixa.dic_de_notas["20"], 31)
        self.assertEqual(caixa.dic_de_notas["50"], 20)
        self.assertEqual(caixa.dic_de_notas["100"], 10)

    # Teste de depósito inválido, em que as tentativas de depósito incluem valores de notas e quantidades incorretas
    def teste_deposito_incorreto(self):
        caixa = Caixa()
        self.assertEqual(caixa.adicionar_notas("5", 3), False)
        self.assertEqual(caixa.adicionar_notas("-2", 20), False)
        self.assertEqual(caixa.adicionar_notas("100", 0), False)
        self.assertEqual(caixa.adicionar_notas("20", -1), False)

    # Teste de saque simples, em que um saque simples de R$70,00 é realizado
    def teste_retirar_simples(self):
        caixa = Caixa()
        self.assertEqual(caixa.adicionar_notas("10", 1), True)
        self.assertEqual(caixa.adicionar_notas("20", 1), True)
        self.assertEqual(caixa.adicionar_notas("50", 1), True)
        self.assertEqual(caixa.adicionar_notas("100", 1), True)

        self.assertEqual(caixa.retirar_notas(70), True)

        self.assertEqual(caixa.dic_de_notas["10"], 1)
        self.assertEqual(caixa.dic_de_notas["20"], 0)
        self.assertEqual(caixa.dic_de_notas["50"], 0)
        self.assertEqual(caixa.dic_de_notas["100"], 1)

    # Teste de saque sortido, onde o saque pode ser feito com diferentes notas e em ordem diversa
    def teste_retirar_sortido(self):
        caixa = Caixa()
        self.assertEqual(caixa.adicionar_notas("10", 2), True)
        self.assertEqual(caixa.adicionar_notas("50", 1), True)

        self.assertEqual(caixa.retirar_notas(70), True)

        self.assertEqual(caixa.dic_de_notas["10"], 0)
        self.assertEqual(caixa.dic_de_notas["50"], 0)

        self.assertEqual(caixa.adicionar_notas("10", 1), True)
        self.assertEqual(caixa.adicionar_notas("20", 2), True)
        self.assertEqual(caixa.adicionar_notas("100", 2), True)

        self.assertEqual(caixa.retirar_notas(250), True)

        self.assertEqual(caixa.dic_de_notas["10"], 0)
        self.assertEqual(caixa.dic_de_notas["20"], 0)
        self.assertEqual(caixa.dic_de_notas["100"], 0)

    # Teste de saque inválido, em que os valores solicitados para o saque são incorretos
    def teste_retirar_incorreto(self):
        caixa = Caixa()
        self.assertEqual(caixa.retirar_notas(1), False)

        self.assertEqual(caixa.adicionar_notas("10", 1), True)
        self.assertEqual(caixa.adicionar_notas("50", 1), True)

        self.assertEqual(caixa.retirar_notas(70), False)
        self.assertEqual(caixa.retirar_notas(40), False)
        self.assertEqual(caixa.retirar_notas(-1), False)

    # Teste para verificar se a nota está presente no dicionário principal
    def teste_verificar_nota(self):
        caixa = Caixa()
        self.assertEqual(caixa.verificar_nota(10), True)
        self.assertEqual(caixa.verificar_nota(20), True)
        self.assertEqual(caixa.verificar_nota(50), True)
        self.assertEqual(caixa.verificar_nota(100), True)

        self.assertEqual(caixa.verificar_nota(-10), False)
        self.assertEqual(caixa.verificar_nota(5), False)


# Execução dos testes
if __name__ == '__main__':
    unittest.main()
