from utils.terminal import Terminal
import time


class CriarPersonagemUI:

    @staticmethod
    def mostrar_intro(sexo):

        Terminal.limpar()
        opc_sexo = 'e' if sexo == 'Macho' else 'a'
        
        print('=' * 55)
        print(' BEM-VINDO AO MUNDO TAMAGOTCHI '.center(55))
        print('=' * 55)
        texto = f'O seu Tamagotchi nasceu e é {sexo}!'
        sexo_colorido = f'\033[33m{sexo}\033[0m'
        print(texto.center(55).replace(sexo, sexo_colorido))
        print('Antes de começar a aventura,'.center(55))
        print(f'qual vai ser o nome del{opc_sexo}?'.center(55))
        print('=' * 55)


    @staticmethod
    def mostrar_erro_nome(sexo):

        Terminal.limpar()
        print('=' * 55)
        print(' ESCOLHA UM NOME VÁLIDO '.center(55))
        print('=' * 55)
        print(f'O seu Tamagotchi nasceu e é {sexo}!'.center(55))
        print()
        texto = 'OBS: O nome deve conter no mínimo 5 letras'
        texto = texto.replace('OBS:', '\033[31mOBS:\033[0m')

        print(texto.center(55))
        print('e não pode possuir números.'.center(55))
        print('=' * 55)

    @staticmethod
    def pedir_nome():

        return input('Digite o nome: ').strip().title()