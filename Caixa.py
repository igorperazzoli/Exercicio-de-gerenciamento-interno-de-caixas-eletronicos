# Classe que representa um caixa eletrônico
class Caixa:

    # Método construtor do caixa
    def __init__(self):
        # Dicionário responsável por guardar a quantidade de notas disponível no caixa
        # A escolha de utilizar um dicionário foi para facilitar uma possível expansão dos tipos de notas
        # Ex: Caso o caixa também receba notas de R$5,00 fica fácil adaptar para essa condição
        self.dic_de_notas = {"100": 0, "50": 0, "20": 0, "10": 0}

    # Método para adicionar notas ao caixa
    def adicionar_notas(self, valor_nota, quantidade_notas):

        # Verifica se o valor da nota e a quantidade são válidos
        if valor_nota not in self.dic_de_notas or quantidade_notas <= 0:
            return False

        # Adiciona a quantidade de notas para a respectiva chave dentro do dicionário
        self.dic_de_notas[valor_nota] += quantidade_notas
        return True

    # Método para sacar as notas do caixa
    def retirar_notas(self, valor_total):

        # Verifica se o valor solicitado é válido
        if valor_total <= 0:
            return False

        # Instancia e organiza as variáveis necessárias
        dic_temporario = {}
        valor_atual = valor_total
        chaves = list(self.dic_de_notas.keys())

        # Executa uma simulação de saque até que o valor seja igual a 0 ou até que o saque apresente falha
        while valor_atual > 0:
            # Atribuição do valor atual para uma variável auxiliar afim de verificar se houve mudança no valor
            aux_valor_atual = valor_atual

            # Percorre pelas notas
            for chave in chaves:
                valor_nota = int(chave)
                # Caso o valor atual seja maior ou igual que o da nota, então essa nota pode ser retirada
                if valor_atual >= valor_nota:
                    # Se a nota ainda não foi inserida no dicionário temporário então é a primeira aparição dela
                    # e será iniciada pela quantidade um
                    if chave not in dic_temporario:
                        if self.dic_de_notas[chave] > 0:
                            dic_temporario[chave] = 1
                            # Decrementa o valor da nota no valor atual
                            valor_atual -= valor_nota
                            break
                    else:
                        # Se a nota inserida já está no dicionário temporário então basta incrementar em um
                        if self.dic_de_notas[chave] - dic_temporario[chave] > 0:
                            dic_temporario[chave] += 1
                            # Decrementa o valor da nota no valor atual
                            valor_atual -= valor_nota
                            break

            # Caso o valor antes do laço seja igual ao valor depois do laço então não houve alteração e portanto
            # não é possível realizar esse saque
            if aux_valor_atual == valor_atual:
                print(f"\nNão é possível retirar o valor {valor_total}!\n")
                return False

        # Se a execução chega aqui então o saque pode ser efetuado e resta preparar a mensagem que será exibida
        # Além de retirar as notas do dicionário principal através do dicionário temporário criado na simulação
        msg = "\nResultado do saque:\n\n"
        for chave in chaves:
            if chave in dic_temporario:
                self.dic_de_notas[chave] -= dic_temporario[chave]
                msg += f"{dic_temporario[chave]} nota(s) de R${chave},00\n"
        msg += f"\nO valor R${valor_total},00 foi retirado com sucesso!\n\n"
        print(msg)
        return True

    # Método que verifica se a nota está realmente presente no dicionário
    def verificar_nota(self, valor_nota):
        if str(valor_nota) in self.dic_de_notas:
            return True
        else:
            return False

    # Método para criar uma mensagem com o status atual do caixa
    def consultar_caixa(self):

        msg = "-=-=-=-=-=-=-=- SALDO -=-=-=-=-=-=-=-\n\n"
        chaves = list(self.dic_de_notas.keys())
        total = 0

        for chave in chaves:
            quantidade = self.dic_de_notas[chave]
            msg += f"{quantidade} nota(s) de R${chave},00\n"
            total += quantidade * int(chave)

        msg += f"\nTotal: R${total},00\n"
        return msg
