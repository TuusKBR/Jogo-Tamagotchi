class ASCII_PPT:

    PEDRA = [
        "    ________       ",
        " --'   _____)      ",
        "      (______)     ",
        "      (______)     ",
        "       (____)      ",
        " ---.__(___)       ",
        "                   "
    ]

    PEDRA_INV = [
        "          ________   ",
        "         (_____   '--",
        "        (______)     ",
        "        (______)     ",
        "         (____)      ",
        "          (___)__.---",
        "                     "
    ]

    PAPEL = [
        "     _______       ",
        " ---'   ____)____  ",
        "           ______) ",
        "           _______)",
        "          _______) ",
        " ---.__________)   ",
        "                   "
    ]

    PAPEL_INV = [
        "          _______    ",
        "     ____(____   '---",
        "    (______          ",
        "   (_______          ",
        "    (_______         ",
        "      (__________.---",
        "                     "
    ]

    TESOURA = [
        "     _______       ",
        " ---'   ____)____  ",
        "           ______) ",
        "        __________)",
        "       (____)      ",
        " ---.__(___)       ",
        "                   "
    ]

    TESOURA_INV = [
        "          _______    ",
        "     ____(____   '---",
        "    (______          ",
        "   (__________       ",
        "         (____)      ",
        "          (___)__.---",
        "                     "
    ]

    @staticmethod
    def get(opcao, invertido=False):
        if opcao == "Pedra":
            return ASCII_PPT.PEDRA_INV if invertido else ASCII_PPT.PEDRA
        
        elif opcao == "Papel":
            return ASCII_PPT.PAPEL_INV if invertido else ASCII_PPT.PAPEL
        
        elif opcao == "Tesoura":
            return ASCII_PPT.TESOURA_INV if invertido else ASCII_PPT.TESOURA
        return []