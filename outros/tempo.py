import random
import os
from datetime import datetime, timedelta
from utils.terminal import Terminal

class AtualizarTempo:
    
    TICK_STATUS = timedelta(seconds=30)
    TICK_IDADE = timedelta(minutes=5)
    
    @staticmethod
    def aplicar_tempo(personagem):
        agora = datetime.now()
        AtualizarTempo.atualizar_status(personagem, agora)
        AtualizarTempo.atualizar_idade(personagem, agora)


    @staticmethod
    def atualizar_status(personagem, agora):
        tempo_passado = agora - personagem._ultimo_tick_status

        if tempo_passado < AtualizarTempo.TICK_STATUS:
            return

        ciclos = tempo_passado // AtualizarTempo.TICK_STATUS

        for _ in range(ciclos):
            personagem._saude = max(0, personagem._saude - random.randint(1, 2))
            personagem._saciedade = max(0, personagem._saciedade - random.randint(1, 4))
            personagem._energia = max(0, personagem._energia - random.randint(2, 3))
            personagem._felicidade = max(0, personagem._felicidade - random.randint(1, 3))

        personagem._ultimo_tick_status += AtualizarTempo.TICK_STATUS * ciclos
        AtualizarTempo.verificar_morte(personagem)


    @staticmethod
    def atualizar_idade(personagem, agora):
        tempo_passado = agora - personagem._ultimo_tick_idade

        if tempo_passado < AtualizarTempo.TICK_IDADE:
            return

        ciclos = tempo_passado // AtualizarTempo.TICK_IDADE
        personagem._idade += ciclos
        personagem._ultimo_tick_idade += AtualizarTempo.TICK_IDADE * ciclos


    @staticmethod
    def verificar_morte(personagem):
        if not personagem._vivo:
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
        AtualizarTempo.registrar_morte(personagem, motivo)


    @staticmethod
    def registrar_morte(personagem, motivo):
        AtualizarTempo.apagar_save()
        AtualizarTempo.mostrar_relatorio_morte(personagem, motivo)
        AtualizarTempo.bloquear_jogo()


    @staticmethod
    def apagar_save():
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho = os.path.join(base, "saves", "save.json")
        if os.path.exists(caminho):
            os.remove(caminho)

    @staticmethod
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


    @staticmethod
    def mostrar_relatorio_morte(personagem, motivo):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=" * 55)
        print(" 💀 TOMOGATCHI FALECEU 💀 ".center(55))
        print("=" * 55)
        print(f"Nome: {personagem._nome}")
        print(f"Idade: {personagem._idade}")
        print(f"Aniversário: {personagem._aniversario.strftime('%d/%m/%Y')}")
        print(f"Fase da vida: {AtualizarTempo.fase_da_vida(personagem._idade)}")
        print(f"Saldo final: R${personagem._moedas}")
        print(f"Motivo da morte: {motivo}")
        print("=" * 55)
        input("\nPressione ENTER para encerrar...")
        Terminal.limpar()

    @staticmethod
    def bloquear_jogo():
        import sys
        sys.exit()
