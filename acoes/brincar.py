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
                    tabela.add_row(f"    [bold yellow]▶  {opcao}[/bold yellow]")
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
        CUSTO = 5
        
        if personagem.moedas < CUSTO:
            Terminal.limpar()
            
            painel_erro = Panel(
                Align.center("[bold red]❌ MOEDAS INSUFICIENTES! ❌[/]\n\n[yellow]Você precisa de R$05 para jogar[/]"),
                title="[bold red]🚫 SEM MOEDAS[/bold red]",
                border_style="red",
                width=50,
                padding=(1, 2)
            )
            
            console.print()
            console.print(Align.center(painel_erro))
            console.print()
            console.print(Align.center("[dim]Pressione qualquer tecla para continuar...[/dim]"))
            time.sleep(2.5)
            return
        
        opcoes = [
            "🖥️  Piada de Computador",
            "🐍  Piada de Programador",
            "💻  Piada de Bug",
            "🤖  Piada de Código",
            "🎭  Piada Aleatória"
        ]
        
        indice = 0
        
        while True:
            Terminal.limpar()
            
            console.print()
            console.print(Align.center("[bold gold]🎭 CONTAR PIADA 🎭[/bold gold]"))
            console.print()
            
            # Construir o texto como string simples (não usar Text())
            linhas = []
            
            # Primeira linha em branco
            linhas.append("")
            
            # Adicionar opções
            for i, opcao in enumerate(opcoes):
                cursor = "▶ " if i == indice else "  "
                
                if i == indice:
                    linhas.append(f"[bold yellow]{cursor}{opcao} (R${CUSTO})[/bold yellow]")
                else:
                    linhas.append(f"   {cursor}{opcao} (R${CUSTO})")
            
            # Última linha em branco
            linhas.append("")
            
            # Juntar como string simples
            texto_opcoes = "\n".join(linhas)
            
            painel_escolha = Panel(
                Align.center(texto_opcoes),
                title="[bold magenta]🎪 ESCOLHA O TIPO DE PIADA[/bold magenta]",
                subtitle=f"[bold yellow]Saldo: R${personagem.moedas:03d}[/bold yellow]",
                border_style="magenta",
                width=48,
                padding=0
            )
            
            console.print(Align.center(painel_escolha))
            console.print()
            console.print(Align.center("[bold cyan][dim]Use ↑ ↓ para navegar • ENTER para contar[/dim][/bold cyan]"))
            
            tecla = readchar.readkey()
            
            if tecla == readchar.key.UP:
                indice = (indice - 1) % len(opcoes)
            elif tecla == readchar.key.DOWN:
                indice = (indice + 1) % len(opcoes)
            elif tecla == readchar.key.ENTER:
                break
        
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
        
        for i in range(4):
            Terminal.limpar()
            
            texto_pensamento = Text(justify="center")
            texto_pensamento.append("🤔 O Tamagotchi está pensando", style="bold white")
            texto_pensamento.append("." * i, style="bold white")
            
            painel_pensamento = Panel(
                Align.center(texto_pensamento),
                border_style="cyan",
                width=50
            )
            
            console.print()
            console.print(Align.center(painel_pensamento))
            time.sleep(0.6)
        
        piada = random.choice(piadas)
        
        Terminal.limpar()
        
        tabela_piada = Table.grid(padding=(0, 2))
        tabela_piada.add_column(justify="center")
        
        tabela_piada.add_row("[bold yellow]🎭 PIADA DO DIA 🎭[/]")
        tabela_piada.add_row("")
        tabela_piada.add_row(f"[bold cyan]{piada['pergunta']}[/]")
        tabela_piada.add_row("")
        tabela_piada.add_row(f"[bold white]{piada['resposta']}[/]")
        
        painel_piada = Panel(
            Align.center(tabela_piada),
            title="[bold magenta]📢 TAMAGOTCHI CONTA[/bold magenta]",
            border_style="cyan",
            width=60,
            padding=(1, 2)
        )
        
        console.print()
        console.print(Align.center(painel_piada))
        time.sleep(3.5)
        
        reacoes = [
            ("😂 Adorou a piada!", 40, "green", 8, 12, 4, 8),
            ("😊 Gostou da piada!", 30, "cyan", 5, 7, 2, 4),
            ("😐 Achou mais ou menos.", 20, "yellow", 1, 3, 0, 2),
            ("😠 Detestou a piada.", 10, "red", -1, -6, 0, 0)  # Valores negativos para perda
        ]
        
        reacao_escolhida = random.choices(reacoes, weights=[r[1] for r in reacoes], k=1)[0]
        
        texto_reacao, _, cor_reacao, min_felicidade, max_felicidade, min_moedas, max_moedas = reacao_escolhida
        
        if "Detestou" in texto_reacao:
            perda_felicidade = random.randint(abs(min_felicidade), abs(max_felicidade))
            personagem._felicidade = max(personagem.felicidade - perda_felicidade, 0)
            ganho_moedas = 0
            
        else:
            ganho_felicidade = random.randint(min_felicidade, max_felicidade)
            personagem._felicidade = min(personagem.felicidade + ganho_felicidade, 100)
            ganho_moedas = random.randint(min_moedas, max_moedas)
            personagem.moedas += ganho_moedas
        
        Terminal.limpar()
        
        tabela_resultado = Table.grid(padding=(1, 2))
        tabela_resultado.add_column(justify="center")
        
        tabela_resultado.add_row(f"[bold {cor_reacao}]{texto_reacao}[/]")
        tabela_resultado.add_row("")
        
        if "Detestou" in texto_reacao:
            tabela_resultado.add_row(f"[bold red]💔 Felicidade: -{perda_felicidade}[/]")
            tabela_resultado.add_row(f"[bold red]💰 Moedas: +R$00[/]")
            
        else:
            tabela_resultado.add_row(f"[bold green]💚 Felicidade: +{ganho_felicidade}[/]")
            tabela_resultado.add_row(f"[bold cyan]💰 Ganhou: R${ganho_moedas:02d}[/]")
        
        tabela_resultado.add_row("")
        tabela_resultado.add_row(f"[dim]Saldo atual: R${personagem.moedas:03d}[/dim]")
        
        if "Adorou" in texto_reacao:
            borda_cor = "green"
            
        elif "Gostou" in texto_reacao:
            borda_cor = "cyan"
            
        elif "mais ou menos" in texto_reacao:
            borda_cor = "yellow"
            
        else:
            borda_cor = "red"
        
        painel_resultado = Panel(
            Align.center(tabela_resultado),
            title="[bold magenta]🎯 RESULTADO[/bold magenta]",
            border_style=borda_cor,
            width=50,
            padding=(0, 2)
        )
        
        console.print()
        console.print(Align.center(painel_resultado))
        console.print()
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

