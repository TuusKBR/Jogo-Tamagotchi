import os

class Terminal:
    
    @staticmethod
    def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')