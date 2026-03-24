import os
from utils.terminal import Terminal
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
import readchar

console = Console()
class Morte:
    
    @staticmethod
    def verificar_morte(personagem):
        if not personagem._vivo:
            return

        if personagem._saude <= 0:
            motivo = "Doença"
            
        elif personagem._saciedade <= 0:
            motivo = "Fome"
            
        elif personagem._energia <= 0:
            motivo = "Exaustão"
            
        elif personagem._felicidade <= 0:
            motivo = "Depressão"
            
        else:
            return

        personagem._vivo = False
        personagem._motivo_morte = motivo
        Morte.apagar_save()


    @staticmethod
    def registrar_morte(personagem, motivo):
        Morte.apagar_save()
        Morte.mostrar_relatorio_morte(personagem, motivo)
        Morte.bloquear_jogo()


    @staticmethod
    def apagar_save():
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho = os.path.join(base, "saves", "save.json")
        if os.path.exists(caminho):
            os.remove(caminho)


    @staticmethod
    def fase_da_vida(idade):
        if idade <= 2:
            return "Bebê"
        elif idade <= 6:
            return "Criança"
        elif idade <= 12:
            return "Adolescente"
        elif idade <= 20:
            return "Adulto"
        return "Idoso"


    @staticmethod
    def mostrar_relatorio_morte(personagem, motivo):
        Terminal.limpar()
        tabela = Table.grid(padding=(0,2))
        tabela.add_column(justify="left")
        tabela.add_column(justify="left")

        tabela.add_row("")
        tabela.add_row("Nome:", personagem._nome)
        tabela.add_row("Idade:", str(personagem._idade))
        tabela.add_row(
            "Aniversário:",
            personagem._aniversario.strftime("%d/%m/%Y")
        )
        tabela.add_row(
            "Fase da vida:",
            Morte.fase_da_vida(personagem._idade)
        )
        tabela.add_row("Saldo final:", f"R${personagem._moedas}")
        tabela.add_row("Motivo da morte:", motivo,)
        tabela.add_row("")

        painel = Panel(
            Align.center(tabela),
            title="[bold red]💀 TAMAGOTCHI FALECEU 💀[/bold red]",
            border_style="red",
            width=50
        )

        console.print()
        console.print(Align.center(painel))
        console.print()

        console.print(
            Align.center("[dim]Pressione ENTER para encerrar...[/dim]")
        )

        while True:
            tecla = readchar.readkey()
            if tecla == readchar.key.ENTER:
                break

        Terminal.limpar()


    @staticmethod
    def bloquear_jogo():
        import sys
        sys.exit()
    