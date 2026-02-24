import os
import time


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


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
        limpar()

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
    def verificar_venda(categoria_tipo, personagem):
        while True:
            try:
                limpar()
                Loja.exibir_loja(categoria_tipo, personagem)
                opc = int(input('\nDigite o ID do item que deseja comprar (0 para voltar): '))

                if opc == 0:
                    return 

                itens = Loja.itens_loja[categoria_tipo]
                if opc not in itens:
                    print(f'\n{"⚠️  ID inválido!":^55}')
                    time.sleep(2)
                    continue

                item = itens[opc]


                if personagem.moedas < item["preco"]:
                    print(f'\n{"💸 Você não tem dinheiro suficiente!":^55}')
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
                print(f'\n{f"Você comprou {item_nome}!":^55}')
                time.sleep(1.5)
                continue


            except ValueError:
                print(f'\n{"⚠️  Valor inválido!":^55}')
                time.sleep(2)
                continue

    @staticmethod
    def comprar(personagem):

        while True:
            try:
                limpar()
                print('=' * 47)
                print(f'{" BEM-VINDO À LOJA ":^47}')
                print('=' * 47)
                print(f'{"1 - COMIDAS"}')
                print(f'{"2 - REMÉDIOS"}')
                print(f'{"0 - SAIR"}')
                print('=' * 47)

                opc = int(input('Escolha sua opção: '))

                if opc == 1:
                    Loja.verificar_venda("Comidas", personagem)
                elif opc == 2:
                    Loja.verificar_venda("Remedios", personagem)
                elif opc == 0:
                    from core.tomogatchi import Tomogatchi
                    Tomogatchi.exibir_personagem(personagem)
                    return
                    
                else:
                    print(f'\n{"⚠️  Valor inválida!":^55}')
                    time.sleep(2)
                    continue

            except ValueError:
                print(f'\n{"⚠️  Valor inválida!":^55}')
                time.sleep(2)
                continue
                

