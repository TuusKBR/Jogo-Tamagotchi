import random
import os
from datetime import datetime, timedelta

TICK_STATUS = timedelta(seconds=30)
TICK_IDADE = timedelta(minutes=5)

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def aplicar_tempo(personagem, ultimo_acesso):

    agora = datetime.now()

    if not hasattr(personagem, "_ultimo_tick_status"):
        personagem._ultimo_tick_status = ultimo_acesso
        personagem._ultimo_tick_idade = ultimo_acesso

    atualizar_status(personagem, agora)
    atualizar_idade(personagem, agora)



def atualizar_status(personagem, agora):
    tempo_passado = agora - personagem._ultimo_tick_status

    if tempo_passado < TICK_STATUS:
        return

    ciclos = tempo_passado // TICK_STATUS

    for _ in range(ciclos):
        personagem._saude = max(0, personagem._saude - random.randint(1, 2))
        personagem._saciedade = max(0, personagem._saciedade - random.randint(1, 4))
        personagem._energia = max(0, personagem._energia - random.randint(2, 3))
        personagem._felicidade = max(0, personagem._felicidade - random.randint(1, 3))

    personagem._ultimo_tick_status += TICK_STATUS * ciclos

    verificar_morte(personagem)



def atualizar_idade(personagem, agora):
    tempo_passado = agora - personagem._ultimo_tick_idade

    if tempo_passado < TICK_IDADE:
        return

    ciclos = tempo_passado // TICK_IDADE
    personagem._idade += ciclos

    personagem._ultimo_tick_idade += TICK_IDADE * ciclos


def verificar_morte(personagem):
    if personagem._vivo is False:
        return

    if personagem._saude <= 0:
        motivo = "Doença"
    elif personagem._saciedade <= 0:
        motivo = "Fome"
    elif personagem._energia <= 0:
        motivo = "Exaustão"
    elif personagem._felicidade <= 0:
        motivo = "Depressão"
    else:
        return

    personagem._vivo = False
    registrar_morte(personagem, motivo)



def registrar_morte(personagem, motivo):
    apagar_save()
    mostrar_relatorio_morte(personagem, motivo)
    bloquear_jogo()


def apagar_save():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho = os.path.join(base, "saves", "save.json")
    if os.path.exists(caminho):
        os.remove(caminho)


def fase_da_vida(idade):
    if idade <= 2:
        return "Bebê"
    elif idade <= 6:
        return "Criança"
    elif idade <= 12:
        return "Adolescente"
    elif idade <= 20:
        return "Adulto"
    return "Idoso"


def mostrar_relatorio_morte(personagem, motivo):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 55)
    print(" 💀 TOMOGATCHI FALECEU 💀 ".center(55))
    print("=" * 55)

    print(f"Nome: {personagem._nome}")
    print(f"Idade: {personagem._idade}")
    print(f"Aniversário: {personagem._aniversario.strftime('%d/%m/%Y')}")
    print(f"Fase da vida: {fase_da_vida(personagem._idade)}")
    print(f"Saldo final: R${personagem._moedas}")
    print(f"Motivo da morte: {motivo}")

    print("=" * 55)
    input("\nPressione ENTER para encerrar...")
    limpar()



def bloquear_jogo():
    import sys
    sys.exit()
