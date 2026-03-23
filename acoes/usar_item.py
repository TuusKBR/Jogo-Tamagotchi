import time
import readchar
from utils.terminal import Terminal

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table

console = Console()

class UsarItem:

    @staticmethod
    def usar_item(personagem):
        from core.jogo import Tamagotchi
        from services.tempo import AtualizarTempo

        def atualizar_lista():
            lista = []
            for categoria, itens in personagem.inventario.items():
                for nome, dados in itens.items():
                    lista.append((categoria, nome, dados))
            return lista

        lista_itens = atualizar_lista()
        indice = 0

        while True:

            AtualizarTempo.aplicar_tempo(personagem)

            if not lista_itens:

                Terminal.limpar()

                painel = Panel(
                    Align.center(
                        "\n🎒 Seu inventário está vazio!\n\n"
                        "[dim]Visite a loja para comprar itens.[/dim]\n"
                    ),
                    title="[bold yellow]Inventário[/bold yellow]",
                    border_style="yellow",
                    width=45
                )

                console.print()
                console.print(Align.center(painel))
                console.print()

                time.sleep(2)

                Tamagotchi.exibir_personagem(personagem)
                return

            Terminal.limpar()

            status = Table.grid(padding=(0, 2))

            status.add_column(justify="left", width=13)
            status.add_column(justify="center", width=5)

            status.add_row("\n💗 Saúde", f"\n{personagem.saude:02d}%")
            status.add_row("🍖 Saciedade", f"{personagem.saciedade:02d}%")
            status.add_row("⚡ Energia", f"{personagem.energia:02d}%")
            status.add_row("😊 Felicidade", f"{personagem.felicidade:02d}%\n")

            status_painel = Panel(
                Align.center(status),
                title="[bold cyan]STATUS ATUAL[/bold cyan]",
                border_style="cyan",
                width=35
            )

            tabela = Table.grid(padding=(0, 2))

            tabela.add_column(justify="left", width=22)
            tabela.add_column(justify="right", width=5)
            
            tabela.add_row("", "")

            for i, (_, nome, dados) in enumerate(lista_itens):

                quantidade = dados.get("quantidade", 0)

                if i == indice:
                    tabela.add_row(
                        f"[bold yellow]▶ {nome}[/bold yellow]",
                        f"[bold yellow]x{quantidade}[/bold yellow]"
                    )
                else:
                    tabela.add_row(
                        f"  {nome}",
                        f"x{quantidade}",
                    )
                    
            tabela.add_row("", "")

            inventario = Panel(
                Align.center(tabela),
                title="[bold yellow]🎒 Inventário[/bold yellow]",
                border_style="bold white",
                width=42
            )

            console.print()
            console.print(Align.center(status_painel))
            console.print()
            console.print(Align.center(inventario))
            console.print(
                Align.center(
                    "\n[bold cyan][dim]Use ↑ ↓ para navegar • ENTER para usar • ESC para sair[/dim][/bold cyan]"
                )
            )

            tecla = readchar.readkey()

            if tecla == readchar.key.UP:
                indice = (indice - 1) % len(lista_itens)

            elif tecla == readchar.key.DOWN:
                indice = (indice + 1) % len(lista_itens)

            elif tecla == readchar.key.ENTER:

                categoria, nome_item, dados_item = lista_itens[indice]
                atributos = dados_item.get("atributos", {})

                if categoria.lower() == "comidas" and personagem.saciedade >= 100:

                    console.print(
                        Align.center(
                            "\n[red]🚨 Saciedade já está máxima![/red]"
                        )
                    )
                    time.sleep(2)
                    continue

                if categoria.lower() == "remedios" and personagem.saude >= 100:

                    console.print(
                        Align.center(
                            "\n[red]🚨 Saúde já está máxima![/red]"
                        )
                    )
                    time.sleep(2)
                    continue

                personagem._saude = min(
                    100, personagem.saude + atributos.get("saude", 0)
                )

                personagem._saciedade = min(
                    100, personagem.saciedade + atributos.get("saciedade", 0)
                )

                personagem._energia = min(
                    100, personagem.energia + atributos.get("energia", 0)
                )

                personagem._felicidade = min(
                    100, personagem.felicidade + atributos.get("felicidade", 0)
                )

                dados_item["quantidade"] = dados_item.get("quantidade", 1) - 1

                if dados_item["quantidade"] <= 0:

                    del personagem.inventario[categoria][nome_item]

                    if not personagem.inventario[categoria]:
                        del personagem.inventario[categoria]

                Terminal.limpar()

                msg = Panel(
                    Align.center(f"\n🎁 Você usou {nome_item}!\n"),
                    border_style="green",
                    width=40
                )

                console.print()
                console.print(Align.center(msg))

                time.sleep(2)

                lista_itens = atualizar_lista()

                if indice >= len(lista_itens):
                    indice = 0

            elif tecla == readchar.key.ESC:
                Tamagotchi.exibir_personagem(personagem)
                return