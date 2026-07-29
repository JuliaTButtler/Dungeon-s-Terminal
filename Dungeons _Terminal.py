import random
import time

# Posições iniciais
pos_jogador = [4, 2]
pos_inimigo = [2, 2]

# Matriz inicial
tab = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', 'I', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', 'J', '.', '.']
]

def tabuleiro(tab):
    for linha in tab:
        print(' '.join(linha))

def mover_jogador(pos_jogador, pos_inimigo, comando, tab):
    nova_linha, nova_coluna = pos_jogador

    if comando == "a" and nova_coluna > 0:
        nova_coluna -= 1
    elif comando == "w" and nova_linha > 0:
        nova_linha -= 1
    elif comando == "s" and nova_linha < len(tab) - 1:
        nova_linha += 1
    elif comando == "d" and nova_coluna < len(tab[0]) - 1:
        nova_coluna += 1

    if [nova_linha, nova_coluna] != pos_inimigo:
        tab[pos_jogador[0]][pos_jogador[1]] = '.'
        pos_jogador[0], pos_jogador[1] = nova_linha, nova_coluna
        tab[pos_jogador[0]][pos_jogador[1]] = 'J'
    else:
        print("\nVocê não pode ocupar a posição de I! Perdeu o movimento.")    

jogador = {"nome": "Robertão", "vida": 100, "vida_max": 100, "ataque": 20, "armadura": 10, "cura": 15}
inimigo = {"nome": "Claudio", "vida": 100, "vida_max": 100, "ataque": 20, "armadura": 10}

def status_jogador(jogador):
    print("===== STATUS DO JOGADOR =====")
    print(f"Nome: {jogador['nome']}")
    print(f"Vida (HP): {jogador['vida']} / {jogador['vida_max']}")
    print(f"Ataque: {jogador['ataque']}")
    print(f"Armadura: {jogador['armadura']}")
    print("=============================")

def status_inimigo(inimigo):
    print("===== STATUS DO INIMIGO =====")
    print(f"Nome: {inimigo['nome']}")
    print(f"Vida (HP): {inimigo['vida']} / {inimigo['vida_max']}")
    print(f"Ataque: {inimigo['ataque']}")
    print(f"Armadura: {inimigo['armadura']}")
    print("=============================")

def rolar_dado():
    dado = random.randint(1, 20)
    if dado == 1:
        print(f"\nDado rolado: {dado}")
        print("ERRO CRÍTICO!")
        return 0, dado
    elif dado == 20:
        print(f"\nDado rolado: {dado}")
        print("ACERTO CRÍTICO!")
        return 1.5, dado
    else:
        print(f"\nDado rolado: {dado}")
        return 1.2, dado

def calcular_ataque_jogador(jogador, inimigo):
    multiplicador, _ = rolar_dado()
    dano = int((jogador["ataque"] - inimigo["armadura"]) * multiplicador)
    if dano < 0:
        dano = 0
    print(f"{jogador['nome']} atacou causando {dano} de dano bruto!")
    return dano

def calcular_defesa_jogador(jogador, dano_recebido):
    multiplicador, dado = rolar_dado()
    if dado == 1:
        bloqueio = 0
    elif dado == 20:
        bloqueio = 1
    else:
        bloqueio = 0.5

    dano_final = int(dano_recebido * (1 - bloqueio))
    jogador["vida"] -= dano_final
    if jogador["vida"] < 0:
        jogador["vida"] = 0

    print(f"{jogador['nome']} defendeu! Bloqueou {int(dano_recebido * bloqueio)} e recebeu {dano_final} de dano.")
    return jogador

def calcular_cura_jogador(jogador):
    multiplicador, _ = rolar_dado()
    cura = int(jogador["cura"] * multiplicador)
    jogador["vida"] += cura
    if jogador["vida"] > jogador["vida_max"]:
        jogador["vida"] = jogador["vida_max"]
    print(f"{jogador['nome']} recuperou {cura} de vida!")
    return jogador

def bonus_posicao(pos_jogador, pos_inimigo, dano):
    linha_j, col_j = pos_jogador
    linha_i, col_i = pos_inimigo
    if col_j == col_i and 0 <= linha_i - linha_j <= 2:
        dano *= 2
        print("Ataque pelas costas! Dano dobrado!")
    elif linha_j == linha_i and abs(col_j - col_i) == 1:
        dano = int(dano * 1.2)
        print("Ataque lateral! Dano aumentado em 20%!")
    return dano

def turno_jogador(pos_jogador, pos_inimigo, tab):
    jogador_defendendo = False
    while True:
        tabuleiro(tab)
        comando = input("Mover (w/a/s/d) ou ficar parado (p)? ").lower()
        if comando in ["w","a","s","d"]:
            mover_jogador(pos_jogador, pos_inimigo, comando, tab)
        elif comando == "p":
            print("Você ficou parado.")
        else:
            print("Comando inválido!")
            continue
        break
    while True:
        acao_jogador = input("Escolha sua ação (atacar/defender/curar): ").lower()
        if acao_jogador in ["atacar","curar","defender"]:
            if acao_jogador == "defender":
                jogador_defendendo = True
            break
        else:
            print("Ação inválida!")
    return acao_jogador, jogador_defendendo

def calcular_ataque_inimigo(inimigo, jogador):
    multiplicador, _ = rolar_dado()
    dano = int((inimigo["ataque"] - jogador["armadura"]) * multiplicador)
    if dano < 0:
        dano = 0
    print(f"{inimigo['nome']} atacou causando {dano} de dano bruto!")
    return dano

def calcular_defesa_inimigo(inimigo, dano_recebido):
    multiplicador, dado = rolar_dado()
    if dado == 1:
        bloqueio = 0
    elif dado == 20:
        bloqueio = 1
    else:
        bloqueio = 0.5
    dano_final = int(dano_recebido * (1 - bloqueio))
    print(f"{inimigo['nome']} defendeu! Bloqueou {int(dano_recebido * bloqueio)} e recebeu {dano_final} de dano.")
    return dano_final

def turno_inimigo(inimigo, jogador, dano_recebido=None):
    acao = random.choice(["atacar","defender"])
    if acao == "atacar":
        dano = calcular_ataque_inimigo(inimigo,jogador)
        jogador["vida"] -= dano
        if jogador["vida"] < 0:
            jogador["vida"] = 0
        print(f"O inimigo ataca e causa {dano} de dano!")
    elif acao == "defender":
        if dano_recebido is not None:
            calcular_defesa_inimigo(inimigo,dano_recebido)
        else:
            print(f"{inimigo['nome']} se prepara para defender seu próximo ataque!")

def main():
    print("=== BATALHA INICIADA ===")
    inimigo_defendendo = False

    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        print("\n--- Seu turno ---")
        status_jogador(jogador)
        status_inimigo(inimigo)

        acao_jogador, jogador_defendendo = turno_jogador(pos_jogador, pos_inimigo, tab)
        acao_inimigo = random.choice(["atacar","defender"])
        if acao_inimigo == "defender":
            inimigo_defendendo = True
            print(f"{inimigo['nome']} está se defendendo do próximo ataque!")

        if acao_jogador == "atacar":
            dano = calcular_ataque_jogador(jogador, inimigo)
            dano = bonus_posicao(pos_jogador,pos_inimigo,dano)
            if inimigo_defendendo:
                dano = calcular_defesa_inimigo(inimigo,dano)
                inimigo_defendendo = False
            inimigo["vida"] -= dano
            if inimigo["vida"] < 0:
                inimigo["vida"] = 0
            print(f"{inimigo['nome']} agora tem {inimigo['vida']} de vida.")
        elif acao_jogador == "curar":
            calcular_cura_jogador(jogador)
        elif acao_jogador == "defender":
            print(f"{jogador['nome']} está se defendendo do próximo ataque!")

        if acao_inimigo == "atacar":
            dano = calcular_ataque_inimigo(inimigo,jogador)
            if jogador_defendendo:
                calcular_defesa_jogador(jogador,dano)
            else:
                jogador["vida"] -= dano
                if jogador["vida"] < 0:
                    jogador["vida"] = 0
                print(f"{inimigo['nome']} causou {dano} de dano ao jogador!")

        if inimigo["vida"] <= 0:
            print(f"\n{inimigo['nome']} foi derrotado! Você venceu!")
            break
        if jogador["vida"] <= 0:
            print(f"\n{jogador['nome']} foi derrotado! Fim de jogo.")
            break

        time.sleep(1)
        
        # Rodar o jogo
if __name__ == "__main__":
    main()
