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


    @staticmethod
    def registrar_morte(personagem, motivo):
        from core.jogo import Tamagotchi
        Morte.apagar_save()
        Tamagotchi.menu()


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
        from ui.ascii_fim_de_jogo import fim_de_jogo
        Terminal.limpar()
        tabela = Table.grid(padding=(0, 1))
        tabela.add_column(justify="right", width=16)
        tabela.add_column(justify="left", width=20)

        tabela.add_row("")
        tabela.add_row("[bold]Nome:[/]", f"  [yellow]{personagem._nome}[/]")
        tabela.add_row("[bold]Idade:[/]", f"  [yellow]{personagem._idade}[/]")
        tabela.add_row(
            "[bold]Fase:[/]",
            f"  [yellow]{Morte.fase_da_vida(personagem._idade)}[/]"
        )
        tabela.add_row("[bold]Causa:[/]", f"  [yellow]{motivo}[/]")
        tabela.add_row("")

        painel = Panel(
            Align.center(tabela),
            title="[bold white]💀 Relatório de morte 💀[/bold white]",
            border_style="red",
            width=50
        )
        console.print(Align.center(fim_de_jogo))
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
    