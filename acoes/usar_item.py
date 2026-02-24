import time
import os
from datetime import datetime

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def usar_item(personagem):
    from core.tomogatchi import Tomogatchi
    from outros.tempo import aplicar_tempo

    def atualizar_lista():
        lista = []
        for categoria, itens in personagem.inventario.items():
            for nome, dados in itens.items():
                lista.append((categoria, nome, dados))
        return lista

    lista_itens = atualizar_lista()

    while True:
        aplicar_tempo(personagem, datetime.now())

        if not lista_itens:
            print(f'\n{"🎒  Seu inventário está vazio!":^55}')
            time.sleep(2)
            Tomogatchi.exibir_personagem(personagem)
            return

        limpar()

        print('=' * 55)
        print(f'{"STATUS ATUAL":^55}')
        print('=' * 55)
        print(f'{"Saúde:":<15}{personagem.saude:>3}%'.center(55))
        print(f'{"Saciedade:":<15}{personagem.saciedade:>3}%'.center(55))
        print(f'{"Energia:":<15}{personagem.energia:>3}%'.center(55))
        print(f'{"Felicidade:":<15}{personagem.felicidade:>3}%'.center(55))
        print('=' * 55)

        print('\nItens disponíveis:')
        for i, (_, nome, dados) in enumerate(lista_itens, start=1):
            print(f'{i:02d} - {nome} (x{dados.get("quantidade", 0)})')

        escolha = input('\nEscolha um item para usar (0 para sair): ')

        if escolha == "0":
            Tomogatchi.exibir_personagem(personagem)
            return

        if not escolha.isdigit():
            print(f'\n{"⚠️  Opção inválida!":^55}')
            time.sleep(2)
            continue

        escolha = int(escolha)

        if not (1 <= escolha <= len(lista_itens)):
            print(f'\n{"⚠️  Opção inválida!":^55}')
            time.sleep(2)
            continue

        categoria, nome_item, dados_item = lista_itens[escolha - 1]
        atributos = dados_item.get("atributos", {})

        if categoria.lower() == "comidas" and personagem.saciedade >= 100:
            print(f'\n{"⚠️  Você já está com a saciedade máxima!":^55}')
            time.sleep(2)
            continue

        if categoria.lower() == "remedios" and personagem.saude >= 100:
            print(f'\n{"⚠️  Sua saúde já está máxima!":^55}')
            time.sleep(2)
            continue

        personagem._saude      = min(100, personagem.saude      + atributos.get("saude", 0))
        personagem._saciedade  = min(100, personagem.saciedade  + atributos.get("saciedade", 0))
        personagem._energia    = min(100, personagem.energia    + atributos.get("energia", 0))
        personagem._felicidade = min(100, personagem.felicidade + atributos.get("felicidade", 0))

        dados_item["quantidade"] = dados_item.get("quantidade", 1) - 1
        if dados_item["quantidade"] <= 0:
            del personagem.inventario[categoria][nome_item]
            if not personagem.inventario[categoria]:
                del personagem.inventario[categoria]

        print('=' * 55)
        print(f'{f"Você usou {nome_item}!":^55}')
        print('=' * 55)
        time.sleep(2)

        lista_itens = atualizar_lista()

        if not lista_itens:
            limpar()
            print(f'\n{"🎒  Seu inventário agora está vazio!":^55}')
            time.sleep(2)
            limpar()
            Tomogatchi.exibir_personagem(personagem)
