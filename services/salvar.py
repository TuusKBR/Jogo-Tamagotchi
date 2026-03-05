import json
from datetime import datetime
import time
import os
import sys
from utils.terminal import Terminal


class Salvar:

    @staticmethod
    def salvar_e_sair(personagem):

        # Caminho compatível com .py e .exe
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

        for _ in range(2):
            for l in range(4):
                print(f'\n{"O jogo está sendo salvo":>38}' + '.' * l)
                time.sleep(0.8)
                Terminal.limpar()

        print(f'\n{"Jogo salvo com sucesso!":^55}')
        time.sleep(2)

        from core.jogo import Tamagotchi
        Tamagotchi.sair_jogo()
