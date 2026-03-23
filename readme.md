# 🐣 Tamagotchi - Jogo no Terminal

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)
![Rich](https://img.shields.io/badge/Rich-Interface-orange)

> Um Tamagotchi interativo no terminal com sistema de sobrevivência, loja e minigames!

---

## 📖 Sobre o Projeto

Tamagotchi é um jogo de simulação onde você cuida de uma criatura virtual, gerenciando seus atributos, comprando itens e jogando minigames para mantê-lo feliz e saudável. Desenvolvido em Python com interface visual rica no terminal.

---

## 🎮 Funcionalidades

### 👤 Sistema de Personagem
| Funcionalidade | Descrição |
|----------------|-----------|
| **Criação** | Personalize seu Tamagotchi com nome e cor |
| **Atributos** | Saúde, Energia, Saciedade e Felicidade |
| **Morte** | Se os atributos zerarem, o personagem morre |
| **Tempo** | Avanço de tempo que afeta os atributos |

### 💾 Sistema de Salvamento
- ✅ Salvar progresso a qualquer momento
- ✅ Carregar saves anteriores
- ✅ Continuidade entre sessões

### 🛌 Sistema de Descanso
- 💤 Dormir para recuperar energia
- 📈 Recuperação de atributos baseada no tempo de sono
- 🌙 Diferentes tipos de sono (curto, longo)

### 🎒 Inventário
- 📦 Sistema completo de itens
- 📂 Organização por categorias (Comidas, Remédios)
- 🎯 Uso estratégico de itens no momento certo

### 🏪 Loja
- 💰 Sistema de moedas
- 🛒 Compra de itens que afetam atributos
- 🔄 Itens com diferentes preços e efeitos

---

## 🎲 Minigames

### ✊ Pedra, Papel e Tesoura
Jogue contra o computador no clássico jogo de estratégia.

**Recompensas:** Moedas

### 😂 Contar Piada
Interaja socialmente e veja a reação do seu Tamagotchi.

**Recompensas:** Felicidade, Moedas (ou efeitos negativos)

### 🚪 Escolher a Porta
Teste sua sorte escolhendo uma das 5 portas.

**Recompensas:** Moedas, Itens raros, ou nada

---

## 🖥 Interface

O jogo utiliza recursos visuais avançados no terminal:

| Recurso | Detalhe |
|---------|---------|
| **Rich** | Painéis coloridos e tabelas estilizadas |
| **ASCII Art** | Desenhos nas mãos (pedra/papel/tesoura) e portas |
| **Teclado** | Navegação com setas ↑ ↓ ← → |
| **Animações** | Efeitos de pensamento, abertura de portas |

---

## 📂 Estrutura do Projeto

tamagotchi/
│
├── core/ # Lógica principal do jogo
│ ├── jogo.py # Classe principal Tamagotchi
│ └── personagem.py # Gerenciamento de atributos
│
├── ui/ # Interface visual
│ ├── ascii_ppt.py # Desenhos dos minigames
│ ├── ascii_doors.py # Desenhos das portas
│ └── components/ # Componentes reutilizáveis
│
├── services/ # Sistemas do jogo
│ ├── loja.py # Loja e itens
│ ├── inventario.py # Gerenciamento de inventário
│ └── save.py # Sistema de save/load
│
├── utils/ # Funções auxiliares
│ ├── terminal.py # Limpeza e controle do terminal
│ └── helpers.py # Funções utilitárias
│
└── main.py # Ponto de entrada do jogo

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes)

### Opção 1: Com ambiente virtual (recomendado)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/tamagotchi.git
cd tamagotchi

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o jogo
python main.py