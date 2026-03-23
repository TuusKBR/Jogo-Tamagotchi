from rich.align import Align
from rich.console import Console

console = Console()

PORTA = [
    "┌─────────┐",
    "│░░░░░░░░░│",
    "│░░░░░░░░░│",
    "│░░░░░░░░░│",
    "│░░░   ░░░│",
    "│░░░ ░ ░░░│",
    "│░░░   ░░░│",
    "│░░░░░░░░░│",
    "└─────────┘"
]


def mostrar_portas(indice):
    portas = []

    for i in range(5):
        if i == indice:
            portas.append([f"[bold yellow]{linha}[/bold yellow]" for linha in PORTA])
        else:
            portas.append(PORTA)

    for linhas in zip(*portas):
        console.print(Align.center("   ".join(linhas)))

    console.print()
    console.print(
        Align.center("[bold cyan][dim]Use ← → para escolher • ENTER para abrir[/dim][/bold cyan]")
    )