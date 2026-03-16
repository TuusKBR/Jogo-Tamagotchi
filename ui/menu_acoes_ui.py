from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
from ui.status_ui import StatusUI
import readchar
from rich.layout import Layout
import time
from services.tempo import AtualizarTempo
from utils.terminal import Terminal

console = Console()

opcoes = [
    "Usar item",
    "Brincar",
    "Dormir",
    "Loja",
    "Salvar e sair"
]


class MenuAcoesUI:

    @staticmethod
    def render(personagem, selecionado):

        layout = Layout()

        layout.split_row(
            Layout(name="status", size=62),
            Layout(name="menu")
        )

        layout["status"].update(
            StatusUI.mostrar(personagem, personagem.sexo, personagem.aniversario)
        )

        menu = []

        menu.append(Align.center("[italic cyan]Use ↑ e ↓ para navegar e Enter para selecionar[/italic cyan]"))
        menu.append("")

        for i, opcao in enumerate(opcoes):

            if i == selecionado:
                painel = Panel(
                    f"[bold yellow]▶ {opcao}[/bold yellow]",
                    border_style="yellow",
                    width=30
                )
            else:
                painel = Panel(
                    f"  {opcao}",
                    width=30
                )

            menu.append(Align.center(painel))

        layout["menu"].update(Group(*menu))
        return layout


    @staticmethod
    def mostrar(personagem):

        Terminal.limpar()
        selecionado = 0
        ultimo_tick = time.time()

        with Live(
            MenuAcoesUI.render(personagem, selecionado),
            refresh_per_second=10,
            screen=True
        ) as live:

            while True:

                if not personagem.vivo:
                    return None

                if time.time() - ultimo_tick >= 5:
                    AtualizarTempo.aplicar_tempo(personagem)
                    ultimo_tick = time.time()

                    if not personagem.vivo:
                        return None

                    live.update(MenuAcoesUI.render(personagem, selecionado))

                tecla = readchar.readkey()

                if tecla == readchar.key.DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)

                elif tecla == readchar.key.UP:
                    selecionado = (selecionado - 1) % len(opcoes)

                elif tecla == readchar.key.ENTER:
                    Terminal.limpar()
                    return selecionado + 1

                live.update(MenuAcoesUI.render(personagem, selecionado))