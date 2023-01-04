import os
import random

print("============================================")
print("Bem vindo ao jogo de Pedra, Papel ou Tesoura")
print("============================================")

computer = 0
player = 0

# exibe o placar
def placar():
    print("PLACAR:")
    print("Você: {}".format(player))
    print("Computador: {}".format(computer))

# input do usuário sobre qual escolha do jogo
def escolher_um_lance():
    ls = (0, 1, 2)
    
    print("Escolha um lance:")
    print("0 - Pedra | 1 - Papel | 2 - Tesoura")
    lance = int(input())  
    try:
        if lance not in ls:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida, escolha um dos valores abaixo")
            escolher_um_lance()
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro: {}".format(e))
        print("Opção inválida, escolha um dos valores abaixo")
        escolher_um_lance()
    return lance

def escolhe_ganhador(escolha_player):
    jogador = 1
    maquina = 0
    empate = 2
    opc = {0: 'Pedra', 1: 'Papel', 2: 'Tesoura'}
    escolha_computador = random.randrange(0, 3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Voce escolheu {}'.format(opc[escolha_player]))
    print('O computador escolheu {}'.format(opc[escolha_computador]))
    if escolha_player == escolha_computador:
        return empate
    elif escolha_player == 0 and escolha_computador == 1:
        return maquina
    elif escolha_player == 0 and escolha_computador == 2:
        return jogador
    elif escolha_player == 1 and escolha_computador == 0:
        return jogador
    elif escolha_player == 1 and escolha_computador == 2:
        return maquina
    elif escolha_player == 2 and escolha_computador == 0:
        return maquina
    elif escolha_player == 2 and escolha_computador == 1:
        return jogador    

# vencedor 0 = computer e vencedor 1 = player 2 = empate
def adiciona_ponto_placar(ganhador):
    global computer
    global player
    if ganhador == 0:
        computer = computer + 1
        print("O computador te derrotou e marcou um ponto!")
    elif ganhador == 1:
        player = player + 1
        print("Você derrotou o computador e marcou um ponto!")
    else:
        print("Empate! Ninguém marcou ponto")

# escolhe se deseja jogar novamente
def joga_novamente():
    print("Deseja jogar novamente?") 
    print("0 - SIM | 1 - NÃO")
    joga_dnv = int(input())
    if joga_dnv == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        game()
    else:
        print("Obrigado por jogar")
        placar()
        exit()

def game():
    placar()
    lance = escolher_um_lance()
    ganhador = escolhe_ganhador(lance)
    adiciona_ponto_placar(ganhador)
    joga_novamente()

if __name__ == "__main__":
    game()

