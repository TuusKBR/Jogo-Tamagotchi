from datetime import datetime
import random

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

