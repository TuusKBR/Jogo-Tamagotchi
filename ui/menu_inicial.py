from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
import keyboard
import time

from ui.ascii_titulo import titulo

console = Console()

opcoes = [
    "Começar jogo",
    "Carregar jogo",
    "Sair"
]


class MenuInicial:

    @staticmethod
    def render(selecionado):

        layout = []

        layout.append(Align.center(titulo))
        layout.append("")

        for i, opcao in enumerate(opcoes):

            if i == selecionado:
                painel = Panel(
                    f"[bold yellow]▶ {opcao}[/bold yellow]",
                    width=35,
                    border_style="yellow"
                )
            else:
                painel = Panel(opcao, width=35)

            layout.append(Align.center(painel))

        return Group(*layout)


    @staticmethod
    def mostrar():

        selecionado = 0

        with Live(MenuInicial.render(selecionado), refresh_per_second=20, screen=True) as live:

            while True:

                if keyboard.is_pressed("down"):
                    selecionado = (selecionado + 1) % len(opcoes)
                    live.update(MenuInicial.render(selecionado))
                    time.sleep(0.15)

                if keyboard.is_pressed("up"):
                    selecionado = (selecionado - 1) % len(opcoes)
                    live.update(MenuInicial.render(selecionado))
                    time.sleep(0.15)

                if keyboard.is_pressed("enter"):
                    return selecionado