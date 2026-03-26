import os
import time
from utils.terminal import Terminal

import readchar
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.console import Console


console = Console()

class Loja:

    itens_loja = {
        "Comidas": {
            1: {"nome": "Pão",               "preco": 5,  "saciedade": 20, "felicidade": 1,  "energia": 0},
            2: {"nome": "Maçã",              "preco": 7,  "saciedade": 15, "felicidade": 4,  "energia": 2},
            3: {"nome": "Sanduíche",         "preco": 15, "saciedade": 28, "felicidade": 6,  "energia": 5},
            4: {"nome": "Peixe Grelhado",    "preco": 30, "saciedade": 40, "felicidade": 12, "energia": 8},
            5: {"nome": "Curry Picante",     "preco": 42, "saciedade": 35, "felicidade": 18, "energia": 12},
            6: {"nome": "Banquete Deluxe",   "preco": 75, "saciedade": 70, "felicidade": 25, "energia": 20},
        },

        "Remedios": {
            1: {"nome": "Curativo",          "preco": 20, "saude": 20, "felicidade": -1, "energia": 0},
            2: {"nome": "Analgésico",        "preco": 35, "saude": 35, "felicidade": 0,  "energia": 0},
            3: {"nome": "Tônico Energético", "preco": 45, "saude": 10, "felicidade": -3, "energia": 20},
            4: {"nome": "Antibiótico",       "preco": 50, "saude": 50, "felicidade": -5, "energia": 0},
            5: {"nome": "Soro Regenerador",  "preco": 85, "saude": 80, "felicidade": 10, "energia": 0},
        }
    }
    

    @staticmethod
    def exibir_loja(categoria_tipo, personagem):
        Terminal.limpar()
        
        for categoria, itens in Loja.itens_loja.items():
            if categoria == categoria_tipo:
                print('=' * 69)
                print(f'{categoria.upper():^69}')
                print('=' * 69)

                print(
                    f'{"ID":<3} | '
                    f'{"ITEM":<20} | '
                    f'{"R$":<4} | '
                    f'{"SAC":>3} | '
                    f'{"FEL":>3} | '
                    f'{"ENE":>3} | '
                    f'{"SAU":>3}'
                )
                print('-' * 69)

                for id_item, status in itens.items():
                    print(
                        f'{id_item:<3} | '
                        f'{status["nome"]:<20} | '
                        f'{status["preco"]:<4} | '
                        f'{f"{status.get("saciedade", 0):02d}":>3} | '
                        f'{f"{status.get("felicidade", 0):02d}":>3} | '
                        f'{f"{status.get("energia", 0):02d}":>3} | '
                        f'{f"{status.get("saude", 0):02d}":>3}'
                    )

                print('-' * 69)
                print(f'{"SALDO: R$ " + str(personagem.moedas):^69}')
                print('=' * 69)
                
    @staticmethod
    def estilo_status(valor):
        if valor > 0:
            return "bold green"
        elif valor < 0:
            return "bold red"
        else:
            return "bold white"


    @staticmethod
    def verificar_venda(categoria_tipo, personagem):

        itens_dict = Loja.itens_loja[categoria_tipo]
        lista_itens = list(itens_dict.items())

        indice = 0

        while True:
            Terminal.limpar()

            id_item, dados = lista_itens[indice]

            nome = dados["nome"]
            preco = dados["preco"]
            sac = dados.get("saciedade", 0)
            fel = dados.get("felicidade", 0)
            ene = dados.get("energia", 0)
            sau = dados.get("saude", 0)

            info = Table.grid(padding=(0, 2))
            info.add_column(justify="left", width=15)
            info.add_column(justify="right", width=10)
            
            info.add_row("")
            info.add_row("🍖  Saciedade", f"[{Loja.estilo_status(sac)}]{sac:+03d}[/{Loja.estilo_status(sac)}]")
            info.add_row("😊  Felicidade", f"[{Loja.estilo_status(fel)}]{fel:+03d}[/{Loja.estilo_status(fel)}]")
            info.add_row("⚡  Energia", f"[{Loja.estilo_status(ene)}]{ene:+03d}[/{Loja.estilo_status(ene)}]")
            info.add_row("💗  Saúde", f"[{Loja.estilo_status(sau)}]{sau:+03d}[/{Loja.estilo_status(sau)}]\n")

            painel_info = Panel(
                Align.center(info),
                title="[bold cyan]INFORMAÇÕES DO ITEM[/bold cyan]",
                border_style="cyan",
                width=42
            )

            tabela = Table.grid(padding=(0, 2))
            tabela.add_column(justify="left", width=22)
            tabela.add_column(justify="right", width=7)

            tabela.add_row("", "")

            for i, (id_item, dados) in enumerate(lista_itens):

                nome_item = dados["nome"]
                preco_item = dados["preco"]

                if i == indice:
                    tabela.add_row(
                        f"[bold yellow]▶ {nome_item}[/bold yellow]",
                        f"[bold yellow]R${preco_item:02d}[/bold yellow]"
                    )
                else:
                    tabela.add_row(
                        f"  {nome_item}",
                        f"R${preco_item:02d}"
                    )

            tabela.add_row("", "")

            painel_loja = Panel(
                Align.center(tabela),
                title=f"[bold magenta]🏪 LOJA - {categoria_tipo.upper()}[/bold magenta]",
                subtitle=f"[bold yellow]Saldo: R${personagem.moedas:03d}[/bold yellow]",
                border_style="magenta",
                width=42
            )

            console.print()
            console.print(Align.center(painel_info))
            console.print()
            console.print(Align.center(painel_loja))
            console.print(
                Align.center(
                    "\n[bold cyan][dim]Use ↑ ↓ para navegar • ENTER para comprar • ESC para voltar[/dim][/bold cyan]"
                )
            )

            tecla = readchar.readkey()

            if tecla == readchar.key.UP:
                indice = (indice - 1) % len(lista_itens)

            elif tecla == readchar.key.DOWN:
                indice = (indice + 1) % len(lista_itens)

            elif tecla == readchar.key.ENTER:

                id_item, item = lista_itens[indice]

                if personagem.moedas < item["preco"]:
                    Terminal.limpar()
                    msg = Panel(
                        Align.center("\n[bold]💸 Moedas insuficientes![/bold]\n"),
                        border_style="red",
                        width=40
                    )
                    console.print()
                    console.print(Align.center(msg))
                    time.sleep(2)
                    continue

                personagem.moedas -= item["preco"]

                item_nome = item["nome"]
                atributos = {
                    k: v for k, v in item.items()
                    if k not in ("nome", "preco")
                }

                invent = personagem.inventario[categoria_tipo]

                if item_nome in invent:
                    invent[item_nome]["quantidade"] += 1
                else:
                    invent[item_nome] = {
                        "quantidade": 1,
                        "atributos": atributos
                    }

                Terminal.limpar()
                msg = Panel(
                    Align.center(f"\n🛒 Você comprou {item_nome}!\n"),
                    border_style="green",
                    width=40
                )

                console.print()
                console.print(Align.center(msg))
                time.sleep(1.8)

            elif tecla == readchar.key.ESC:
                return


    @staticmethod
    def comprar(personagem):

        opcoes_exibicao = [
            "🍔  Comidas",
            "💊  Remédios",
            "🚪  Sair"
        ]

        opcoes = [
            "Comidas",
            "Remedios",
            "Sair"
        ]

        indice = 0

        while True:
            Terminal.limpar()

            tabela = Table.grid(padding=(0, 3))
            tabela.add_column(justify="left", width=25)
            tabela.add_row("")

            for i, opcao in enumerate(opcoes_exibicao):
                if i == indice:
                    tabela.add_row(f"[bold yellow]▶  {opcao}[/bold yellow]")
                else:
                    tabela.add_row(f"    {opcao}")

            tabela.add_row("")

            painel_loja = Panel(
                Align.center(tabela),
                title="[bold magenta]🏬 LOJA[/bold magenta]",
                border_style="magenta",
                width=45
            )

            console.print()
            console.print(Align.center(painel_loja))
            console.print(
                Align.center(
                    "\n[bold cyan][dim]Use ↑ ↓ para navegar • ENTER para selecionar[/dim][/bold cyan]"
                )
            )

            tecla = readchar.readkey()

            if tecla == readchar.key.UP:
                indice = (indice - 1) % len(opcoes)

            elif tecla == readchar.key.DOWN:
                indice = (indice + 1) % len(opcoes)

            elif tecla == readchar.key.ENTER:

                escolha = opcoes[indice]

                if escolha == "Comidas":
                    Loja.verificar_venda("Comidas", personagem)

                elif escolha == "Remedios":
                    Loja.verificar_venda("Remedios", personagem)

                elif escolha == "Sair":
                    from core.jogo import Tamagotchi
                    Tamagotchi.exibir_personagem(personagem)
                    return
                
