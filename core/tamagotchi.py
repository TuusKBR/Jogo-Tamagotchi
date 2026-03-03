import time
import os
from core.personagem import Personagem
from acoes.brincar import Brincar
from acoes.dormir import Dormir
from outros.loja import Loja
from outros.salvar import Salvar
from outros.carregar import CarregarJogo
from acoes.usar_item import UsarItem
from outros.tempo import AtualizarTempo
from utils.terminal import Terminal

class Tamagotchi:

    @staticmethod
    def sair_jogo():
        import sys
        Terminal.limpar()
        print(f'\n{"Saindo do jogo!":^55}')
        time.sleep(2)
        Terminal.limpar()
        sys.exit()
        
        
    @staticmethod
    def menu():
        while True:
            Terminal.limpar()
            print('='*55)
            print(f'{"JOGO TAMAGOTCHI":^55}')
            print('='*55)
            try:
                opc = int(input('1- Começar jogo\n2- Carregar jogo\n0- Sair\nEscolha sua opção: '))
                if not (0 <= opc <= 2):
                    print(f'\n{"⚠️  Opção inválida!":^55}')
                    time.sleep(2)
                else:
                    if opc == 1:
                        Tamagotchi.criar_personagem()

                    elif opc == 2:
                        personagem = CarregarJogo.carregar_jogo()
                            
                        if personagem:
                            Tamagotchi.exibir_personagem(personagem)
                        else:
                            continue

                    else:
                        return Tamagotchi.sair_jogo()
                        
            except ValueError:
                print(f'\n{"⚠️  Valor inválida!":^55}')
                time.sleep(2)


    @staticmethod
    def criar_personagem():
        personagem = Personagem()
        Terminal.limpar()

        def escrever_lento(texto, atraso=0.04):
            for letra in texto:
                print(letra, end='', flush=True)
                time.sleep(atraso)
            print()

        cont = 0

        while True:
            cont += 1
            Terminal.limpar()

            if personagem.sexo == 'Macho':
                opc_sexo = 'e'
            else:
                opc_sexo = 'a'

            print('=' * 55)

            if cont == 1:
                escrever_lento(' BEM-VINDO AO MUNDO TAMAGOTCHI '.center(55))
                print('=' * 55)
                time.sleep(0.5)

                texto = f'O seu Tamagotchi nasceu e é {personagem.sexo}!'
                texto_centralizado = texto.center(55)
                sexo_colorido = f'\033[33m{personagem.sexo}\033[0m'
                escrever_lento(
                    texto_centralizado.replace(personagem.sexo, sexo_colorido)
                )
                escrever_lento(
                    'Antes de começar a aventura,'.center(55)
                )
                escrever_lento(
                    f'qual vai ser o nome del{opc_sexo}?'.center(55)
                )
            else:
                print(' ESCOLHA UM NOME VÁLIDO '.center(55))
                print('=' * 55)
                print(
                    f'O seu Tamagotchi nasceu e é {personagem.sexo}!\n'.center(55)
                )
                texto = 'OBS: O nome deve conter no mínimo 5 letras'
                texto_centralizado = texto.center(55)

                print(
                    texto_centralizado.replace(
                        'OBS:',
                        '\033[31mOBS:\033[0m'
                    )
                )
                print(
                    'e não pode possuir números.'.center(55)
                )



            print('=' * 55)

            try:
                nome = str(input('Digite o nome: ')).strip().title()
                personagem.nome = nome
                break

            except ValueError as erro:
                print(f'{str(erro):^55}')
                time.sleep(3)

        Tamagotchi.exibir_personagem(personagem)


    @staticmethod
    def formatar_valores(sexo, aniversario):
        sexo = 'M' if sexo == 'Menino' else 'F'
        aniversario = aniversario.strftime("%d/%m")
        return sexo, aniversario
    
    
    @staticmethod
    def barra_de_status(valor, tamanho = 20):
        cheios = int((valor / 100 * tamanho))
        vazios = tamanho - cheios
        return '[' + ('#' * cheios) + ('-' * vazios) + f'] {valor:>3}%'
    
    
    @staticmethod
    def opcao_errada(personagem):
        time.sleep(2)
        Terminal.limpar()
        Tamagotchi.exibir_personagem(personagem)


    @staticmethod
    def exibir_personagem(personagem):

        from outros.tempo import AtualizarTempo
        AtualizarTempo.aplicar_tempo(personagem)

        if not personagem.vivo:
            Terminal.limpar()
            print(f'\n{"💀 SEU TAMAGOTCHI MORREU 💀":^55}')
            time.sleep(3)
            Tamagotchi.sair_jogo()

        sexo, aniversario = Tamagotchi.formatar_valores(personagem.sexo, personagem.aniversario)
        Terminal.limpar()

        def p(texto):
            print(texto)
            time.sleep(0.13)
            

        p('+------------------ STATUS -------------------+')
        p(f'| NOME:         {personagem.nome:<30}|')
        p(f'| SEXO:         {sexo:<30}|')
        p(f'| IDADE:        {personagem.idade:<30}|')
        p(f'| ANIVERSÁRIO:  {aniversario:<30}|')
        p('+---------------------------------------------+')
        p(f'| SAÚDE:        {Tamagotchi.barra_de_status(personagem.saude):<30}|')
        p(f'| SACIEDADE:    {Tamagotchi.barra_de_status(personagem.saciedade):<30}|')
        p(f'| ENERGIA:      {Tamagotchi.barra_de_status(personagem.energia):<30}|')
        p(f'| FELICIDADE:   {Tamagotchi.barra_de_status(personagem.felicidade):<30}|')
        p('+---------------------------------------------+')
        largura = 47

        conteudo = f"| SALDO: R${personagem.moedas:03d} |"
        preenchimento = largura - len(conteudo) - 2
        esq = preenchimento // 2
        dir = preenchimento - esq
        linha = "|" + "=" * esq + conteudo + "=" * dir + "|"
        print(linha)
        p('+---------------------------------------------+')
        Tamagotchi.acoes_menu(personagem)
        
    @staticmethod
    def acoes_menu(personagem):
        opcoes = {
            1: UsarItem.usar_item,
            2: Brincar.escolher_jogo,
            3: Dormir.adormecer,
            4: Loja.comprar, 
            5: Salvar.salvar_jogo,
            6: Salvar.salvar_e_sair
        }

        while True:
            try:
                print('\n+------------------- OPÇÃO -------------------+')
                opcao = int(input('1- Usar item\n2- Brincar\n3- Dormir\n4- Loja\n5- Salvar o jogo\n6- Salvar e sair\nEscolha sua opção: '))
                if 1 <= opcao <= 6:
                    acao = opcoes[opcao]
                    acao(personagem)   
                    return

                else:
                    print(f'\n{"⚠️  Opção inválida!":^55}')
                    Tamagotchi.opcao_errada(personagem)
                    return

            except ValueError:
                print(f'\n{"⚠️  Valor inválida!":^55}')
                Tamagotchi.opcao_errada(personagem)
                return
 
