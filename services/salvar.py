import json
from datetime import datetime
import time
import os
import sys
from utils.terminal import Terminal
from ui.mensagens_ui import MensagensUI

class Salvar:

    @staticmethod
    def salvar_e_sair(personagem):
        if getattr(sys, 'frozen', False):
            base_projeto = os.path.dirname(sys.executable)
        else:
            base_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        pasta_saves = os.path.join(base_projeto, "saves")
        os.makedirs(pasta_saves, exist_ok=True)
        caminho_save = os.path.join(pasta_saves, "save.json")

        dados = {
            "nome": personagem._nome,
            "sexo": personagem._sexo,
            "idade": personagem._idade,
            "saude": personagem._saude,
            "saciedade": personagem._saciedade,
            "energia": personagem._energia,
            "felicidade": personagem._felicidade,
            "moedas": personagem._moedas,
            "inventario": personagem._inventario,
            "vivo": personagem._vivo,
            "aniversario": personagem._aniversario.strftime("%d/%m/%Y"),
            "ultimo_acesso": datetime.now().isoformat()
        }

        with open(caminho_save, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        Terminal.limpar()
        MensagensUI.salvando()
        MensagensUI.sucesso("JOGO SALVO COM SUCESSO!")

        from core.jogo import Tamagotchi
        Tamagotchi.sair_jogo()
