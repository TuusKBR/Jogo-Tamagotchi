import json
from datetime import datetime
import time
import os
import sys
from utils.terminal import Terminal


def salvar_jogo(personagem, t=0):
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
    for i in range(2):
        for l in range(0, 4):
            print(f'\n{f"O jogo está sendo salvo":>38}' + '.' * l)
            time.sleep(0.8)
            Terminal.limpar()

    print(f'\n{f"Jogo salvo com sucesso!":^55}')
    time.sleep(3)
    Terminal.limpar()
    if t == 0:
        from core.tamagotchi import Tamagotchi
        Tamagotchi.exibir_personagem(personagem)


def salvar_e_sair(personagem):
    salvar_jogo(personagem, 1)
    from core.tamagotchi import Tamagotchi
    Tamagotchi.sair_jogo()
