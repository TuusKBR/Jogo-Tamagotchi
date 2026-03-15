import json
import os
import time
import sys
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.align import Align

from core.personagem import Personagem
from utils.terminal import Terminal


console = Console()


class CarregarJogo:

    @staticmethod
    def caixa_mensagem(texto):

        painel = Panel(
            Align.center(texto),
            width=36,
            border_style="white"
        )

        console.print()
        console.print(Align.center(painel))
        console.print()


    @staticmethod
    def carregar_jogo():

        if getattr(sys, 'frozen', False):
            base_projeto = os.path.dirname(sys.executable)
        else:
            base_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        pasta_saves = os.path.join(base_projeto, "saves")
        caminho_save = os.path.join(pasta_saves, "save.json")

        if not os.path.exists(caminho_save):
            Terminal.limpar()

            CarregarJogo.caixa_mensagem(
                "\n🛑 SALVAMENTO NÂO ENCONTRADO!\n"
            )

            time.sleep(2)
            return None


        with open(caminho_save, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        from services.tempo import AtualizarTempo

        personagem = Personagem()
        personagem._nome = dados["nome"]
        personagem._sexo = dados["sexo"]
        personagem._idade = dados["idade"]
        personagem._saude = dados["saude"]
        personagem._saciedade = dados["saciedade"]
        personagem._energia = dados["energia"]
        personagem._felicidade = dados["felicidade"]
        personagem._moedas = dados["moedas"]
        personagem._inventario = dados["inventario"]
        personagem._vivo = dados["vivo"]
        personagem._aniversario = datetime.strptime(dados["aniversario"], "%d/%m/%Y")

        ultimo_acesso = datetime.fromisoformat(
            dados.get("ultimo_acesso", datetime.now().isoformat())
        )

        personagem._ultimo_tick_status = ultimo_acesso
        personagem._ultimo_tick_idade = ultimo_acesso
        AtualizarTempo.aplicar_tempo(personagem)

        Terminal.limpar()

        CarregarJogo.caixa_mensagem(
            "\n💾  JOGO SALVO ENCONTRADO!\n"
        )

        time.sleep(2)
        return personagem