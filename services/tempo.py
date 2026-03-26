import random
from datetime import datetime, timedelta
from utils.terminal import Terminal
from services.morte import Morte

class AtualizarTempo:
    
    TICK_STATUS = timedelta(seconds=40)
    TICK_IDADE = timedelta(minutes=5)
    MAX_TICKS = 10
    
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
        
        if ciclos > AtualizarTempo.MAX_TICKS:
            ciclos = AtualizarTempo.MAX_TICKS
            personagem._ultimo_tick_status = agora - (AtualizarTempo.TICK_STATUS * AtualizarTempo.MAX_TICKS)

        for _ in range(ciclos):
            personagem._saude = max(0, personagem._saude - random.randint(1, 2))
            personagem._saciedade = max(0, personagem._saciedade - random.randint(1, 4))
            personagem._energia = max(0, personagem._energia - random.randint(2, 3))
            personagem._felicidade = max(0, personagem._felicidade - random.randint(1, 3))

        personagem._ultimo_tick_status += AtualizarTempo.TICK_STATUS * ciclos
        Morte.verificar_morte(personagem)


    @staticmethod
    def atualizar_idade(personagem, agora):
        tempo_passado = agora - personagem._ultimo_tick_idade

        if tempo_passado < AtualizarTempo.TICK_IDADE:
            return

        ciclos = tempo_passado // AtualizarTempo.TICK_IDADE
        if ciclos > AtualizarTempo.MAX_TICKS:
            ciclos = AtualizarTempo.MAX_TICKS
            personagem._ultimo_tick_idade = agora - (AtualizarTempo.TICK_IDADE * AtualizarTempo.MAX_TICKS)
        
        personagem._idade += ciclos
        personagem._ultimo_tick_idade += AtualizarTempo.TICK_IDADE * ciclos


    
