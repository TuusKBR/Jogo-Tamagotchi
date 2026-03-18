import time
import readchar
from utils.terminal import Terminal
import random
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.text import Text
from ui.ascii_ppt import ASCII_PPT
from rich.columns import Columns


console = Console()


class Brincar:

    @staticmethod
    def escolher_jogo(personagem):

        from core.jogo import Tamagotchi

        opcoes = [
            "📄 Pedra, papel e tesoura (Grátis)",
            "😂 Contar piada (5 moedas)",
            "🚪 Escolha a porta (15 moedas)",
            "🔙 Voltar"
        ]

        indice = 0
        while True:

            Terminal.limpar()
            tabela = Table.grid(padding=(0, 3))
            tabela.add_column(justify="left", width=40)
            tabela.add_row("")

            for i, opcao in enumerate(opcoes):

                if i == indice:
                    tabela.add_row(f"[bold yellow]▶ {opcao}[/bold yellow]")
                else:
                    tabela.add_row(f"   {opcao}")

            tabela.add_row("")

            painel = Panel(
                Align.center(tabela),
                title="[bold magenta]🎮 ESCOLHER JOGO[/bold magenta]",
                subtitle=f"[bold yellow]Saldo: R${personagem.moedas:03d}[/bold yellow]",
                border_style="magenta",
                width=45
            )

            console.print()
            console.print(Align.center(painel))
            console.print(
                Align.center("\n[bold cyan][dim]Use ↑ ↓ para navegar • ENTER para selecionar[/dim][/bold cyan]")
            )

            tecla = readchar.readkey()

            if tecla == readchar.key.UP:
                indice = (indice - 1) % len(opcoes)

            elif tecla == readchar.key.DOWN:
                indice = (indice + 1) % len(opcoes)

            elif tecla == readchar.key.ENTER:

                if indice == 0:
                    Brincar.jogo_pedra_papel(personagem)

                elif indice == 1:
                    Brincar.jogo_contar_piada(personagem)

                elif indice == 2:
                    Brincar.jogo_escolher_porta(personagem)

                elif indice == 3:
                    Tamagotchi.exibir_personagem(personagem)
                    return


    @staticmethod
    def jogo_pedra_papel(personagem):

        opcoes = ["Pedra", "Papel", "Tesoura"]
        indice = 0

        while True:
            Terminal.limpar()

            tabela = Table.grid(padding=(0, 3))
            tabela.add_column(justify="left", width=25)
            tabela.add_row("")

            for i, opcao in enumerate(opcoes):
                if i == indice:
                    tabela.add_row(f"[bold yellow]▶  {opcao}[/bold yellow]")
                else:
                    tabela.add_row(f"    {opcao}")

            tabela.add_row("")

            painel = Panel(
                Align.center(tabela),
                title="[bold magenta]✊ PEDRA, PAPEL E TESOURA[/bold magenta]",
                border_style="magenta",
                width=45
            )

            console.print()
            console.print(Align.center(painel))
            console.print(
                Align.center("\n[bold cyan][dim]Use ↑ ↓ para navegar • ENTER para escolher[/dim][/bold cyan]")
            )

            tecla = readchar.readkey()

            if tecla == readchar.key.UP:
                indice = (indice - 1) % len(opcoes)

            elif tecla == readchar.key.DOWN:
                indice = (indice + 1) % len(opcoes)

            elif tecla == readchar.key.ENTER:
                opc = opcoes[indice]
                break

        for i in range(4):
            Terminal.limpar()

            texto = Text(justify="center")
            texto.append("\n🤖 A máquina está pensando", style="bold white")
            texto.append("." * i, style="bold white")
            texto.append("\n")

            painel = Panel(
                Align.center(texto),
                border_style="cyan",
                width=45
            )

            console.print()
            console.print(Align.center(painel))

            time.sleep(0.6)

        opc_maquina = ['Tesoura', 'Pedra', 'Papel']
        opc_sorteada = random.choice(opc_maquina)

        regras = {
            "Pedra": {"Pedra": "Empate", "Papel": "Derrota", "Tesoura": "Vitória"},
            "Papel": {"Papel": "Empate", "Tesoura": "Derrota", "Pedra": "Vitória"},
            "Tesoura": {"Tesoura": "Empate", "Pedra": "Derrota", "Papel": "Vitória"}
        }

        resultado = regras[opc][opc_sorteada]

        if resultado == 'Vitória':
            resultado_moedas = random.randint(3, 6)
            cor = "green"
        elif resultado == "Empate":
            resultado_moedas = random.randint(1, 3)
            cor = "yellow"
        else:
            resultado_moedas = 0
            cor = "red"

        personagem.moedas += resultado_moedas

        def ajustar(arte, largura=22):
            return [linha.ljust(largura) for linha in arte]

        ascii_jogador = ajustar(ASCII_PPT.get(opc, invertido=False))
        ascii_maquina = ajustar(ASCII_PPT.get(opc_sorteada, invertido=True))

        Terminal.limpar()

        console.print()
        console.print(Align.center("[bold magenta]📄 PEDRA, PAPEL E TESOURA 📄[/bold magenta]"))
        console.print()

        arte_jogador = "\n".join(ascii_jogador)
        arte_maquina = "\n".join(ascii_maquina)

        painel_jogador = Panel(
            Align.center(arte_jogador),
            title=f"[bold cyan]VOCÊ: {opc}[/bold cyan]",
            border_style="italic cyan",
            width=30,
            padding=(0, 1)
        )

        painel_maquina = Panel(
            Align.center(arte_maquina),
            title=f"[bold bright_red]MÁQUINA: {opc_sorteada}[/bold bright_red]",
            border_style="italic cyan",
            width=30,
            padding=(0, 1)
        )

        console.print(Align.center(Columns([painel_jogador, painel_maquina], equal=True)))
        console.print()

        tabela_resultado = Table(show_header=False, box=None, padding=(0, 2))
        tabela_resultado.add_column(justify="center", width=30)

        tabela_resultado.add_row(f"\n[bold {cor}]{resultado}![/]")
        tabela_resultado.add_row(f"[bold white]Ganhou:[/][bold] R${resultado_moedas:02d}[/]\n")

        painel_resultado = Panel(
            Align.center(tabela_resultado),
            title="[bold bright_white]🎯 RESULTADO FINAL[/bold bright_white]",
            border_style=cor,
            width=50,
            padding=(0, 1)
        )

        console.print(Align.center(painel_resultado))
        console.print()
        time.sleep(4)
        

    @staticmethod
    def jogo_contar_piada(personagem):
        Terminal.limpar()
        CUSTO = 5

        if personagem.moedas < CUSTO:
            print(f'\n{"Você não tem moedas suficientes! (5 necessárias)":^55}')
            time.sleep(2.5)
            return

        personagem.moedas -= CUSTO

        piadas = [
            {"pergunta": "Por que o computador foi ao médico?", "resposta": "Porque ele pegou um vírus!"},
            {"pergunta": "Por que o programador confunde Halloween com Natal?", "resposta": "Porque OCT 31 é igual a DEC 25."},
            {"pergunta": "Qual é o cúmulo da informática?", "resposta": "Achar que Java é só café."},
            {"pergunta": "Por que o código foi preso?", "resposta": "Porque ele executou sem permissão."},
            {"pergunta": "Por que o programador foi ao terapeuta?", "resposta": "Porque ele tinha muitos problemas não resolvidos."},
            {"pergunta": "O que o HTML disse para o CSS?", "resposta": "Sem você eu não tenho estilo."},
            {"pergunta": "Por que o computador espirrou?", "resposta": "Porque estava cheio de vírus."},
            {"pergunta": "Qual linguagem os fantasmas usam?", "resposta": "Boo-thon."},
            {"pergunta": "Por que o bug foi promovido?", "resposta": "Porque ele aparecia em todos os sistemas."},
            {"pergunta": "Por que o programador terminou o namoro?", "resposta": "Porque a relação não tinha mais compatibilidade."}
        ]

        Terminal.limpar()
        for i in range(3):
            print(f'\n{f"O Tamagotchi está pensando em uma piada":>42}' + '.' * i)
            time.sleep(1)
            Terminal.limpar()

        piada = random.choice(piadas)
        print('=' * 55)
        print(f'{piada["pergunta"]:^55}')
        time.sleep(3.5)
        print(f'{piada["resposta"]:^55}')
        print('=' * 55)
        time.sleep(3)

        reacoes = [
            ("Adorou a piada!", 40),
            ("Gostou da piada!", 30),
            ("Achou mais ou menos.", 20),
            ("Detestou a piada.", 10)
        ]

        reacao = random.choices(
            [r[0] for r in reacoes],
            weights=[r[1] for r in reacoes],
            k=1
        )[0]

        if reacao == "Adorou a piada!":
            ganho_felicidade = random.randint(8, 12)
            ganho_moedas = random.randint(4, 8)

        elif reacao == "Gostou da piada!":
            ganho_felicidade = random.randint(5, 7)
            ganho_moedas = random.randint(2, 4)

        elif reacao == "Achou mais ou menos.":
            ganho_felicidade = random.randint(1, 3)
            ganho_moedas = random.randint(0, 2)

        else:  
            perda_felicidade = random.randint(3, 6)
            personagem._felicidade = max(personagem.felicidade - perda_felicidade, 0)
            
            print(f'{"O Tamagotchi detestou a piada...":^55}')
            print(f'{"Felicidade: -" + str(perda_felicidade):^55}')
            print(f'{"Moedas ganhas: R$00":^55}')
            print('=' * 55)
            time.sleep(4)
            return

        personagem._felicidade = min(personagem.felicidade + ganho_felicidade, 100)
        personagem.moedas += ganho_moedas

        print(f'{reacao:^55}')
        print(f'{"Felicidade: +" + str(ganho_felicidade):^55}')
        print(f'{"Ganhou: R$" + f"{ganho_moedas:02d}":^55}')
        print('=' * 55)
        time.sleep(4)



    @staticmethod
    def jogo_escolher_porta(personagem):
        Terminal.limpar()

        CUSTO = 15

        if personagem.moedas < CUSTO:
            print(f'\n{"💸 Você não tem moedas suficientes! (15 necessárias)":^55}')
            time.sleep(2.5)
            return

        portas = [1, 2, 3, 4, 5]

        resultados = [
            ("50_moedas", 1),
            ("35_moedas", 2),
            ("item", 3),
            ("perdeu", 2),
            ("perdeu", 2),
        ]

        print('=' * 55)
        print(f'{"ESCOLHA UMA PORTA":^55}')
        print('=' * 55)
        print(f'\n{"🚪  🚪  🚪  🚪  🚪":^51}\n')
        print(f'{"⏱️  Você tem 30 segundos para escolher":^55}\n')

        inicio = time.time()

        while True:
            if time.time() - inicio > 30:
                print(f'\n{"⌛ Tempo esgotado! Você perdeu a vez!":^55}')
                personagem.moedas -= CUSTO
                time.sleep(3)
                return

            try:
                escolha = int(input(f'{"Escolha uma porta (1 a 5): ":<25}'))
                if escolha not in portas:
                    print('-' * 55)
                    print(f'{"⚠️ Porta inválida! Escolha entre 1 e 5.":^55}')
                    print('-' * 55)
                    continue  
                break
            except ValueError:
                print('-' * 55)
                print(f'{"⚠️ Entrada inválida! Digite um número.":^55}')
                print('-' * 55)
                continue

        Terminal.limpar()
        for i in range(3):
            print(f'\n{f"Abrindo a porta {escolha}":>38}' + '.' * i)
            time.sleep(1)
            Terminal.limpar()

        premio = random.choices(
            [r[0] for r in resultados],
            weights=[r[1] for r in resultados],
            k=1
        )[0]

        print('=' * 55)

        if premio == "50_moedas":
            personagem.moedas += 50
            print(f'{"🎉 Você encontrou 50 moedas!":^55}')

        elif premio == "35_moedas":
            personagem.moedas += 35
            print(f'{"✨ Você ganhou 35 moedas!":^55}')

        elif premio == "perdeu":
            print(f'{"💀 Porta vazia... você perdeu a vez!":^55}')
            personagem.moedas -= CUSTO

        elif premio == "item":
            from jogo import Loja
            personagem.moedas -= 15

            categoria = random.choice(["Comidas", "Remedios"])
            itens = list(Loja.itens_loja[categoria].values())

            pesos = [1 / item["preco"] for item in itens]
            item = random.choices(itens, weights=pesos, k=1)[0]

            nome = item["nome"]

            invent = personagem.inventario[categoria]
            if nome in invent:
                invent[nome]["quantidade"] += 1
            else:
                invent[nome] = {
                    "quantidade": 1,
                    "atributos": {
                        k: v for k, v in item.items()
                        if k not in ("nome", "preco")
                    }
                }

            print(f'{"🎁 Você encontrou um item!":^55}')
            print(f'{f"→ {nome}":^55}')

        print('=' * 55)
        time.sleep(4)

