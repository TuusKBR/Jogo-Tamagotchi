import time
import random
import os
from utils.terminal import Terminal

class Dormir:

    @staticmethod
    def tipo_de_sono():
        sorteio = random.randint(1, 100)

        if sorteio <= 60:
            tipo = 'Bom'
            saude = random.randint(8, 12)
            energia = random.randint(18, 22)
            felicidade = random.randint(8, 12)
            saciedade = random.randint(7, 12)
        
        elif 60 < sorteio <= 90:
            tipo = 'Normal'
            saude = random.randint(6, 9)
            energia = random.randint(16, 20)
            felicidade = random.randint(6, 9)
            saciedade = random.randint(10, 15)
        
        else:
            tipo = 'Com pesadelo'
            saude = random.randint(4, 7)
            energia = random.randint(11, 16)
            felicidade = random.randint(-5, 0)
            saciedade = random.randint(15, 18)
            
        return tipo, saude, energia, felicidade, saciedade

    @staticmethod
    def adormecer(personagem):
        from core.tamagotchi import Tamagotchi
        from datetime import timedelta
        tempo_sono = random.randint(3, 8)
        Terminal.limpar()

        for i in range(tempo_sono):
            for l in range(0, 4):
                print(f'\n{f"O Tamagotchi está dormindo":>38}' + '.' * l)
                time.sleep(0.8)
                Terminal.limpar()

        if hasattr(personagem, "_ultimo_tick_idade"):
            from datetime import timedelta, datetime
            from outros.tempo import atualizar_idade
            personagem._ultimo_tick_idade -= timedelta(seconds=100)
        atualizar_idade(personagem, datetime.now())

        tipo, saude, energia, felicidade, saciedade = Dormir.tipo_de_sono()
        
        personagem._saude      = min(personagem.saude + saude, 100)
        personagem._energia    = min(personagem.energia + energia, 100)
        personagem._felicidade = min(personagem.felicidade + felicidade, 100)
        personagem._saciedade  = max(personagem.saciedade - saciedade, 0)

        quase_morreu = False

        if personagem._saude <= 0:
            personagem._saude = 1
            quase_morreu = True
        if personagem._energia <= 0:
            personagem._energia = 1
            quase_morreu = True
        if personagem._felicidade <= 0:
            personagem._felicidade = 1
            quase_morreu = True
        if personagem._saciedade <= 0:
            personagem._saciedade = 1
            quase_morreu = True

        print('=' * 55)
        print(f'{f"{personagem.nome} teve um sono *{tipo}*!":^55}')
        print('=' * 55)

        print(f'{"Saúde:":<15}{saude:+03d}'.center(56))
        print(f'{"Saciedade:":<15}{-saciedade:+03d}'.center(56))
        print(f'{"Energia:":<15}{energia:+03d}'.center(56))
        print(f'{"Felicidade:":<15}{felicidade:+03d}'.center(56))

        if quase_morreu:
            print()
            print(f'{"⚠️  O Tamagotchi está em estado crítico ⚠️":^55}')
            quase_morreu = False

        print('=' * 55)
        time.sleep(5)

        from core.tamagotchi import Tamagotchi
        Tamagotchi.exibir_personagem(personagem)
