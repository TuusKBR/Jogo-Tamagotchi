from datetime import datetime
import random
from utils.terminal import Terminal
import time

class Personagem:
    
    def __init__(self):
        agora = datetime.now()

        self._nome = None
        self._sexo = random.choice(['Macho', 'Fêmea'])
        self._idade = 0
        self._saude = 100
        self._saciedade = 100
        self._energia = 100
        self._felicidade = 100
        self._moedas = 25
        self._inventario = {
            "Comidas": {},
            "Remedios": {}
        }
        self._vivo = True
        self._aniversario = agora

        # 🔥 ADICIONE ISSO
        self._ultimo_tick_status = agora
        self._ultimo_tick_idade = agora

    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str):
            raise ValueError('\n' + f'{"⚠️  Valor inválido!":^55}')

        valor = valor.strip()

        letras = valor.replace(' ', '')

        if len(letras) < 5 or not letras.isalpha():
            raise ValueError('\n' + f'{"⚠️  Nome inválido!":^55}')

        self._nome = valor


    @property
    def sexo(self):
        return self._sexo
    

    @property
    def idade(self):
        return self._idade
    

    @property
    def saude(self):
        return self._saude
    

    @saude.setter
    def saude(self, valor):
        self._saude = valor
    

    @property
    def saciedade(self):
        return self._saciedade
    

    @saciedade.setter
    def saciedade(self, valor):
        self._saciedade = valor
    

    @property
    def energia(self):
        return self._energia
    

    @energia.setter
    def energia(self, valor):
        self.energia = valor
    

    @property
    def felicidade(self):
        return self._felicidade
    
    
    @property
    def moedas(self):
        return self._moedas
    

    @moedas.setter
    def moedas(self, valor):
        self._moedas = valor
    

    @property
    def vivo(self):
        return self._vivo
    

    @property
    def aniversario(self):
        return self._aniversario
    

    @property
    def inventario(self):
        return self._inventario
    
    
    @staticmethod
    def criar_personagem():
        personagem = Personagem()
        Terminal.limpar()

        def escrever_lento(texto, atraso=0.04):
            for letra in texto:
                print(letra, end='', flush=True)
                time.sleep(atraso)
            print()

        cont = 0

        while True:
            cont += 1
            Terminal.limpar()

            if personagem.sexo == 'Macho':
                opc_sexo = 'e'
            else:
                opc_sexo = 'a'

            print('=' * 55)

            if cont == 1:
                escrever_lento(' BEM-VINDO AO MUNDO TAMAGOTCHI '.center(55))
                print('=' * 55)
                time.sleep(0.5)

                texto = f'O seu Tamagotchi nasceu e é {personagem.sexo}!'
                texto_centralizado = texto.center(55)
                sexo_colorido = f'\033[33m{personagem.sexo}\033[0m'
                escrever_lento(
                    texto_centralizado.replace(personagem.sexo, sexo_colorido)
                )
                escrever_lento(
                    'Antes de começar a aventura,'.center(55)
                )
                escrever_lento(
                    f'qual vai ser o nome del{opc_sexo}?'.center(55)
                )
            else:
                print(' ESCOLHA UM NOME VÁLIDO '.center(55))
                print('=' * 55)
                print(
                    f'O seu Tamagotchi nasceu e é {personagem.sexo}!\n'.center(55)
                )
                texto = 'OBS: O nome deve conter no mínimo 5 letras'
                texto_centralizado = texto.center(55)

                print(
                    texto_centralizado.replace(
                        'OBS:',
                        '\033[31mOBS:\033[0m'
                    )
                )
                print(
                    'e não pode possuir números.'.center(55)
                )

            print('=' * 55)

            try:
                nome = str(input('Digite o nome: ')).strip().title()
                personagem.nome = nome
                break

            except ValueError as erro:
                print(f'{str(erro):^55}')
                time.sleep(3)

        Tamagotchi.exibir_personagem(personagem)

