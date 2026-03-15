from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import time
from utils.terminal import Terminal

console = Console()

class MensagensUI:

    @staticmethod
    def caixa(texto, largura=36, cor="white"):

        painel = Panel(
            Align.center(texto),
            width=largura,
            border_style=cor
        )

        console.print()
        console.print(Align.center(painel))
        console.print()


    @staticmethod
    def salvando():

        for _ in range(2):
            for l in range(4):

                Terminal.limpar()
                texto = f"💾 SALVANDO JOGO{'.' * l}"
                MensagensUI.caixa(texto)
                time.sleep(0.6)


    @staticmethod
    def sucesso(texto):

        Terminal.limpar()
        MensagensUI.caixa(f"✔ {texto}", cor="green")
        time.sleep(2)


    @staticmethod
    def erro(texto):

        Terminal.limpar()
        MensagensUI.caixa(f"🛑 {texto}", cor="yellow")
        time.sleep(2)