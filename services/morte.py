import os
from utils.terminal import Terminal
class Morte:
    
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
        personagem._motivo_morte = motivo
        Morte.apagar_save()


    @staticmethod
    def registrar_morte(personagem, motivo):
        Morte.apagar_save()
        Morte.mostrar_relatorio_morte(personagem, motivo)
        Morte.bloquear_jogo()


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
        
        Terminal.limpar()
        print("=" * 55)
        print(" 💀 TOMOGATCHI FALECEU 💀 ".center(55))
        print("=" * 55)
        print(f"Nome: {personagem._nome}")
        print(f"Idade: {personagem._idade}")
        print(f"Aniversário: {personagem._aniversario.strftime('%d/%m/%Y')}")
        print(f"Fase da vida: {Morte.fase_da_vida(personagem._idade)}")
        print(f"Saldo final: R${personagem._moedas}")
        print(f"Motivo da morte: {motivo}")
        print("=" * 55)
        input("\nPressione ENTER para encerrar...")
        Terminal.limpar()


    @staticmethod
    def bloquear_jogo():
        import sys
        sys.exit()
    