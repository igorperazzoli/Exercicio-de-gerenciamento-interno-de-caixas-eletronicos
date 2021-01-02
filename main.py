from Caixa import Caixa

# Método main contendo um menu para o caixa
if __name__ == '__main__':
    # Instanciação do caixa
    caixa = Caixa()

    # Variável que armazena a opção escolhida no menu
    op = ""

    # Enquanto a opção 0 não for escolhida o menu seguirá executando
    while op != "0":

        # Opções do menu
        op = input("-=-=-=-=-=-=-=- MENU -=-=-=-=-=-=-=-\n\n"
                   "Escolha uma opção:\n\n"
                   "1 - Depositar notas\n"
                   "2 - Retirar notas\n"
                   "3 - Consultar saldo\n"
                   "0 - Sair\n\n")

        # Se a opção escolhida for 1, então serão solicitadas as informações necessárias para o depósito das notas
        if op == "1":
            valor_nota = input("\nDigite o valor da nota que deseja depositar (Ex: 10, 20, 50 ou 100):\n")
            if caixa.verificar_nota(valor_nota):
                quantidade_notas = int(input("\nDigite a quantidade de notas que deseja depositar:\n"))
                if quantidade_notas > 0:
                    caixa.adicionar_notas(valor_nota, quantidade_notas)
                    print(f"\n{quantidade_notas} nota(s) de R${valor_nota},00 depositadas com sucesso!\n")
                else:
                    print("\nQuantidade de notas inválida, operação cancelada!\n")
            else:
                print("\nValor inválido, operação cancelada!\n")

        # Se a opção escolhida for 2, então serão solicitadas as informações necessárias para o saque das notas
        elif op == "2":
            valor_total = int(input("\nDigite o valor que deseja retirar:\n"))
            if valor_total > 0:
                caixa.retirar_notas(valor_total)
            else:
                print("\nValor inválido, operação cancelada!\n")

        # Se a opção escolhida for 1, então serão mostradas as informações atuais do caixa
        elif op == "3":
            print(caixa.consultar_caixa())

        # Se a opção escolhida for diferente, então o usuário deverá digitar um valor válido
        elif op != "0":
            print("\nDigite uma opção válida!\n")