from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.console import Console

console = Console()

class StatusUI:

    @staticmethod
    def barra(valor, tamanho=20):
        cheios = int((valor / 100) * tamanho)
        vazios = tamanho - cheios
        return "⟦" + "█" * cheios + "-" * vazios + "⟧"


    @staticmethod
    def mostrar(personagem, sexo, aniversario):

        aniversario = aniversario.strftime("%d/%m/%y")

        largura_painel = 60
        largura_interna = largura_painel - 4

        texto = Text()

        texto.append(f"\nNome: {personagem.nome}\n", style="bold white")
        texto.append(f"Sexo: {sexo}\n")
        texto.append(f"Idade: {personagem.idade}\n")
        texto.append(f"Nasc: {aniversario}\n")

        texto.append("\n" + "─" * (largura_painel - 4) + "\n\n", style="cyan")

        largura_label = 15

        texto.append(f"{'💗  Saúde':<{largura_label}}")
        texto.append(f"  {StatusUI.barra(personagem.saude)} {personagem.saude}%\n", style="bright_white")

        texto.append(f"{'🍖  Saciedade':<{largura_label}}")
        texto.append(f"  {StatusUI.barra(personagem.saciedade)} {personagem.saciedade}%\n",style="bright_white")

        texto.append(f"{'⚡  Energia':<{largura_label}}")
        texto.append(f"  {StatusUI.barra(personagem.energia)} {personagem.energia}%\n", style="bright_white")

        texto.append(f"{'😊  Felicidade':<{largura_label}}")
        texto.append(f"  {StatusUI.barra(personagem.felicidade)} {personagem.felicidade}%\n", style="bright_white")

        painel = Panel(
            texto,
            title="[bold cyan]STATUS DO TAMAGOTCHI[/bold cyan]",
            border_style="cyan",
            width=largura_painel
        )

        console.print(Align.center(painel))