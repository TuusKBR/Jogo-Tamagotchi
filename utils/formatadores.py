class Formatadores:

    @staticmethod
    def formatar_sexo(sexo):
        return 'M' if sexo == 'Menino' else 'F'

    @staticmethod
    def formatar_data(data):
        return data.strftime("%d/%m")