from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from utils.terminal import Terminal
from shutil import get_terminal_size

console = Console()


class CriarPersonagemUI:

    @staticmethod
    def mostrar_intro(sexo):
        Terminal.limpar()

        artigo = "Ele" if sexo == "Macho" else "Ela"
        indefinido = "um" if sexo == "Macho" else "uma"

        texto = Text()
        texto.append("\nUma pequena cápsula caiu do céu...\n\n")
        texto.append("Quando ela se abriu, algo incrível aconteceu.\n")
        texto.append("Um pequeno ser acabou de nascer.\n\n")
        texto.append("Seu Tamagotchi nasceu!\n")
        texto.append(f"{artigo} é {indefinido} ")
        texto.append(sexo, style="bold yellow")
        texto.append(".\n\n")
        texto.append(f"Agora {artigo.lower()} precisa de um nome para começar sua jornada.\n\n", style="italic")
        texto.append("Regras para o nome:\n", style="bold red")
        texto.append("• Mínimo de 5 letras\n", style="bold")
        texto.append("• Não pode conter números\n", style="bold")

        painel = Panel(
            texto,
            title="[bold cyan]Novo Tamagotchi[/bold cyan]",
            border_style="bold white",
            width=70
        )

        console.print()
        console.print(Align.center(painel))
        console.print()


    @staticmethod
    def mostrar_erro_nome(sexo):
        if sexo == "Macho":
            atg = "o"
        else:
            atg = "a"
            
        Terminal.limpar()
        
        texto = Text()
        texto.append("\n⚠  ", style="bold red")
        texto.append(f"Nome inválido para {atg} ", style="white")
        texto.append(sexo, style="bold yellow")
        texto.append("!\n\n", style="white")

        texto.append("O nome do seu Tamagotchi precisa seguir as regras:\n\n")
        texto.append("• Mínimo de 5 letras\n", style="bold red")
        texto.append("• Não pode conter números\n", style="bold red")

        painel = Panel(
            texto,
            title="[bold red]Erro[/bold red]",
            border_style="bold white", 
            width=60
        )

        console.print()
        console.print(Align.center(painel))
        console.print()


    @staticmethod
    def pedir_nome():
        
        prompt = "▶ Digite o nome do seu Tamagotchi: "
        largura_terminal = get_terminal_size().columns
        espacos = max((largura_terminal - len(prompt)) // 2 - 5, 0)
        nome = console.input(" " * espacos + f"[bold green]{prompt}[/]")

        return nome.strip().title()