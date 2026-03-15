import json
import os
import sys
from datetime import datetime
from core.personagem import Personagem
from services.tempo import AtualizarTempo
from ui.mensagens_ui import MensagensUI


class CarregarJogo:

    @staticmethod
    def carregar_jogo():

        if getattr(sys, 'frozen', False):
            base_projeto = os.path.dirname(sys.executable)
        else:
            base_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        pasta_saves = os.path.join(base_projeto, "saves")
        caminho_save = os.path.join(pasta_saves, "save.json")

        if not os.path.exists(caminho_save):

            MensagensUI.erro("🛑 SALVAMENTO NÃO ENCONTRADO!")
            return None

        with open(caminho_save, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)


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
        MensagensUI.sucesso(" JOGO SALVO ENCONTRADO!")

        return personagem