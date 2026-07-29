# 🗡️ Dungeons Terminal

Um RPG de batalha em turno desenvolvido em Python para execução no terminal.

Este projeto foi desenvolvido durante o **2º semestre da graduação** com o objetivo de praticar lógica de programação, utilização de matrizes, funções, estruturas de dados e mecânicas básicas de jogos.

## Funcionalidades

- Movimentação do jogador em um mapa 5x5 utilizando **W, A, S e D**.
- Sistema de batalha por turnos.
- Ataque, defesa e cura.
- Sistema de rolagem de dado (D20), incluindo:
  - Erro crítico (1)
  - Acerto crítico (20)
  - Ataques normais
- Bônus de dano baseado na posição do jogador em relação ao inimigo.
- Inimigo controlado por uma IA simples com ações aleatórias.

## Tecnologias

- Python 3
- Biblioteca `random`
- Biblioteca `time`

## Como executar

O projeto foi desenvolvido para ser executado no Visual Studio Code.

Basta abrir o arquivo principal do projeto e clicar no botão **Run (▶)** para iniciar o jogo.

## Mecânicas

### Movimentação

O jogador pode se mover pelo mapa utilizando:

| Tecla | Ação |
|-------|------|
| W | Cima |
| A | Esquerda |
| S | Baixo |
| D | Direita |
| P | Permanecer parado |

Durante o turno, o jogador escolhe primeiro sua movimentação e depois sua ação.

### Combate

As ações disponíveis são:

- Atacar
- Defender
- Curar

Os ataques utilizam uma rolagem de D20 que influencia o dano causado.

Também existem bônus posicionais:

- Ataque pelas costas → dano dobrado.
- Ataque lateral → bônus de 20% de dano.

## Objetivos do projeto

Este projeto teve como foco praticar:

- Estruturas condicionais
- Laços de repetição
- Funções
- Listas e matrizes
- Dicionários
- Modularização do código
- Lógica de jogos em turno

## Melhorias futuras

Como este projeto foi desenvolvido no início da graduação, hoje identifico diversas melhorias que poderiam ser implementadas, por exemplo:

- Separação do código em múltiplos arquivos.
- Utilização de classes (Programação Orientada a Objetos).
- Melhor organização da lógica do jogo.
- IA do inimigo mais elaborada.
- Sistema de múltiplos inimigos.
- Inventário e equipamentos.
- Correção de pequenas inconsistências encontradas durante revisões posteriores do código.
- Interface de terminal mais amigável.

Apesar dessas possíveis melhorias, optei por manter o projeto praticamente em seu estado original por representar meu aprendizado naquele momento da graduação.
