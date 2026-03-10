from utils.formatadores import Formatadores

class StatusUI:

    @staticmethod
    def barra(valor, tamanho=20):

        cheios = int((valor / 100) * tamanho)
        vazios = tamanho - cheios
        return '[' + ('#' * cheios) + ('-' * vazios) + f'] {valor:>3}%'

    @staticmethod
    def exibir(personagem):

        sexo = Formatadores.formatar_sexo(personagem.sexo)
        aniversario = Formatadores.formatar_data(personagem.aniversario)

        print('+------------------ STATUS -------------------+')
        print(f'| NOME:         {personagem.nome:<30}|')
        print(f'| SEXO:         {sexo:<30}|')
        print(f'| IDADE:        {personagem.idade:<30}|')
        print(f'| ANIVERSÁRIO:  {aniversario:<30}|')
        print('+---------------------------------------------+')
        print(f'| SAÚDE:        {StatusUI.barra(personagem.saude):<30}|')
        print(f'| SACIEDADE:    {StatusUI.barra(personagem.saciedade):<30}|')
        print(f'| ENERGIA:      {StatusUI.barra(personagem.energia):<30}|')
        print(f'| FELICIDADE:   {StatusUI.barra(personagem.felicidade):<30}|')
        print('+---------------------------------------------+')

        largura = 47
        conteudo = f"| SALDO: R${personagem.moedas:03d} |"
        preenchimento = largura - len(conteudo) - 2
        esq = preenchimento // 2
        dir = preenchimento - esq
        linha = "|" + "=" * esq + conteudo + "=" * dir + "|"
        print(linha)
        print('+---------------------------------------------+')