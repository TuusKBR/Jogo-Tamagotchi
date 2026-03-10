from utils.terminal import Terminal

class MenuAcoesUI:

    @staticmethod
    def mostrar():

        print('\n+------------------- OPÇÃO -------------------+')
        print('1- Usar item')
        print('2- Brincar')
        print('3- Dormir')
        print('4- Loja')
        print('5- Salvar e sair')
        try:
            opcao = int(input('Escolha sua opção: '))
            Terminal.limpar()
            return opcao

        except ValueError:
            print("\n⚠️ Valor inválido!")
            return None