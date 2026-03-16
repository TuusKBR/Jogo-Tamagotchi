import time
import random
from utils.terminal import Terminal

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table

console = Console()

class Dormir:

    @staticmethod
    def tipo_de_sono():
        sorteio = random.randint(1, 100)

        if sorteio <= 60:
            tipo = 'Bom'
            saude = random.randint(8, 12)
            energia = random.randint(18, 22)
            felicidade = random.randint(8, 12)
            saciedade = random.randint(7, 12)

        elif 60 < sorteio <= 90:
            tipo = 'Normal'
            saude = random.randint(6, 9)
            energia = random.randint(16, 20)
            felicidade = random.randint(6, 9)
            saciedade = random.randint(10, 15)

        else:
            tipo = 'Com pesadelo'
            saude = random.randint(4, 7)
            energia = random.randint(11, 16)
            felicidade = random.randint(-5, 0)
            saciedade = random.randint(15, 18)

        return tipo, saude, energia, felicidade, saciedade

    @staticmethod
    def adormecer(personagem):
        from datetime import datetime, timedelta
        from services.tempo import AtualizarTempo
        from core.jogo import Tamagotchi

        tempo_sono = random.randint(3, 6)
        Terminal.limpar()
        rosto = "( -_- )"

        for _ in range(tempo_sono):
            for z in range(1, 4):

                conteudo = f"""
            {rosto}

🌕 O tomagotchi está dormindo 🌕

              {"Z" * z}
"""

                painel = Panel(
                    Align.center(conteudo),
                    title="[bold blue]\nHora de dormir[/bold blue]",
                    border_style="blue",
                    width=42
                )

                console.clear()
                console.print()
                console.print(Align.center(painel))
                time.sleep(0.8)

        if hasattr(personagem, "_ultimo_tick_idade"):
            personagem._ultimo_tick_idade -= timedelta(seconds=100)

        AtualizarTempo.atualizar_idade(personagem, datetime.now())
        tipo, saude, energia, felicidade, saciedade = Dormir.tipo_de_sono()

        personagem._saude = min(personagem.saude + saude, 100)
        personagem._energia = min(personagem.energia + energia, 100)
        personagem._felicidade = min(personagem.felicidade + felicidade, 100)
        personagem._saciedade = max(personagem.saciedade - saciedade, 0)

        quase_morreu = False

        if personagem._saude <= 0:
            personagem._saude = 1
            quase_morreu = True

        if personagem._energia <= 0:
            personagem._energia = 1
            quase_morreu = True

        if personagem._felicidade <= 0:
            personagem._felicidade = 1
            quase_morreu = True

        if personagem._saciedade <= 0:
            personagem._saciedade = 1
            quase_morreu = True

        Terminal.limpar()

        tabela = Table.grid(padding=(0, 3))
        tabela.add_column(justify="left")
        tabela.add_column(justify="right")

        def cor(valor):
            return "green" if valor >= 0 else "red"

        tabela.add_row("\n💗 Saúde", f"\n[{cor(saude)}]{saude:+03d}[/{cor(saude)}]")
        tabela.add_row("🍖 Saciedade", f"[red]{-saciedade:+03d}[/red]")
        tabela.add_row("⚡ Energia", f"[{cor(energia)}]{energia:+03d}[/{cor(energia)}]")
        tabela.add_row("😊 Felicidade", f"[{cor(felicidade)}]{felicidade:+03d}[/{cor(felicidade)}]\n")

        painel = Panel(
            Align.center(tabela),
            title=f"\n[bold cyan]{personagem.nome} acordou![/bold cyan]",
            subtitle=f"[bold yellow]Sono: {tipo}[/bold yellow]\n",
            border_style="bold white",
            width=42
        )

        console.print()
        console.print(Align.center(painel))
        console.print()

        if quase_morreu:

            aviso = Panel(
                Align.center("🛑 O Tamagotchi está em estado crítico 🛑"),
                border_style="red",
                width=42
            )

            console.print(Align.center(aviso))

        time.sleep(5)

        Tamagotchi.exibir_personagem(personagem)