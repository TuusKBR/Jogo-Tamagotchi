import json
import os
import time
import sys
from datetime import datetime
from core.personagem import Personagem


def carregar_jogo():
    # Caminho compatível com .py e .exe
    if getattr(sys, 'frozen', False):
        base_projeto = os.path.dirname(sys.executable)
    else:
        base_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    pasta_saves = os.path.join(base_projeto, "saves")
    caminho_save = os.path.join(pasta_saves, "save.json")

    if not os.path.exists(caminho_save):
        print(f'\n{"⚠️  Nenhum jogo salvo encontrado!":^55}\n')
        time.sleep(2)
        try:
            while True:
                print('-' * 55)
                escolha = input("Deseja começar um novo jogo? (S/N): ").strip().upper()

                if escolha == "S":
                    from core.tomogatchi import Tomogatchi
                    return Tomogatchi.criar_personagem()

                elif escolha == 'N':
                    return 'SAIR'

                else:
                    print(f'\n{"⚠️  Opção inválida!":^55}')
                    time.sleep(2)

        except ValueError:
            print(f'\n{"⚠️  Opção inválida!":^55}')
            time.sleep(2)

    with open(caminho_save, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    from outros.tempo import aplicar_tempo

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

    aplicar_tempo(personagem, ultimo_acesso)

    print(f'\n{"💾 Jogo carregado com sucesso!":^55}')
    time.sleep(2)
    return personagem
