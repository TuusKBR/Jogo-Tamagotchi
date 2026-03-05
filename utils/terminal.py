import os
import time

class Terminal:
    
    @staticmethod
    def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    
    @staticmethod
    def opcao_errada(personagem):
        from core.jogo import Tamagotchi
        time.sleep(2)
        Terminal.limpar()
        Tamagotchi.exibir_personagem(personagem)