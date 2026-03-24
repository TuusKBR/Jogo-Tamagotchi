import time
import os
from core.personagem import Personagem
from acoes.brincar import Brincar
from acoes.dormir import Dormir
from services.loja import Loja
from services.salvar import Salvar
from services.carregar import CarregarJogo
from acoes.usar_item import UsarItem
from services.tempo import AtualizarTempo
from utils.terminal import Terminal
from ui.menu_inicial import MenuInicial
from ui.criar_personagem_ui import CriarPersonagemUI
from ui.status_ui import StatusUI
from ui.menu_acoes_ui import MenuAcoesUI
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import time
import sys
from services.morte import Morte

console = Console()

class Tamagotchi:

    @staticmethod
    def sair_jogo():
        Terminal.limpar()

        painel = Panel(
            Align.center(
                "\n👋 OBRIGADO POR JOGAR!\n\n"
                "Seu Tamagotchi se despede\n"
                "ele vai estar te esperando.\n"
            ),
            title="[bold cyan]TAMAGOTCHI[bold cyan]",
            width=42
        )

        console.print()
        console.print(Align.center(painel))
        console.print()
        time.sleep(3)
        Terminal.limpar()
        sys.exit()


    @staticmethod
    def menu():
        while True:
            opc = MenuInicial.mostrar()
            if opc == 0:
                Tamagotchi.criar_personagem()

            elif opc == 1:
                personagem = CarregarJogo.carregar_jogo()

                if personagem:
                    Tamagotchi.exibir_personagem(personagem)

            elif opc == 2:
                Tamagotchi.sair_jogo()


    @staticmethod
    def criar_personagem():
        personagem = Personagem()
        CriarPersonagemUI.mostrar_intro(personagem.sexo)

        while True:
            try:
                nome = CriarPersonagemUI.pedir_nome()  

                if len(nome) < 5:
                    raise ValueError
                if any(c.isdigit() for c in nome):
                    raise ValueError

                personagem.nome = nome
                break  

            except ValueError:
                CriarPersonagemUI.mostrar_erro_nome(personagem.sexo)

        Tamagotchi.exibir_personagem(personagem)


    @staticmethod
    def exibir_personagem(personagem):
        while True:
            if not personagem.vivo:
                Morte.mostrar_relatorio_morte(personagem, personagem._motivo_morte)
                Morte.bloquear_jogo()
                return

            Terminal.limpar()

            StatusUI.mostrar(
                personagem,
                personagem.sexo,
                personagem.aniversario
            )

            Tamagotchi.acoes_menu(personagem)
        
        
    @staticmethod
    def acoes_menu(personagem):
        opcoes = {
            1: UsarItem.usar_item,
            2: Brincar.escolher_jogo,
            3: Dormir.adormecer,
            4: Loja.comprar,
            5: Salvar.salvar_e_sair,
        }

        opcao = MenuAcoesUI.mostrar(personagem)

        if opcao in opcoes:
            opcoes[opcao](personagem)

        Morte.verificar_morte(personagem)
 
