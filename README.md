# Jogo-Nim
def computador_escolhe_jogada(jogo,m):
    #arrumar a quantidade de peças que o computador pode tirar
    retorna =True
    cont = 1
    if(jogo <= m):
        pecas_retiradas = jogo
        return pecas_retiradas
    else:
        while(retorna):
            if(jogo % (cont+1) == 0):
                pecas_retiradas = cont
                return pecas_retiradas
            else:
                cont = cont + 1
                retorna = True
def usuario_escolhe_jogada(n,m):
    retorna = True
    while(retorna):
        pecas_retiradas = int(input("Quantas peças você vai retirar? "))
        if(pecas_retiradas <= m):
            pecas_restantes = n - pecas_retiradas
            return pecas_restantes       
        else:
            print("valor invalido")
            retorna = True
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    jogo = n
    print("O jogo tem ",jogo,"peças ")
    if  n % (m+1)  == 0:
        print("Computador começa!")
        jogadorUsuario = False
    else:
        jogadorUsuario = True
        print("Você começa!")
    #retornar o numero de peças que sobrara
    while(jogo >0):
        if(jogadorUsuario):
            pecasRestantes = usuario_escolhe_jogada(jogo,m)
            pecasRetiradas = jogo - pecasRestantes
            print("Você tirou",pecasRetiradas,"peça")
            jogo = jogo - pecasRetiradas
            print("Agora restam", jogo,"peças no tabuleiro\n")
            jogadorUsuario = False
            if(jogo == 0):
                print("Você ganhou!")
                UsuarioVenceu = 1   
        else:
            pecasRestantes = computador_escolhe_jogada(jogo,m)
            pecasRetiradas = jogo - pecasRestantes
            print("O computador retirou ",pecasRetiradas,"peça")
            jogo = jogo - pecasRetiradas
            print("Agora restam", jogo,"peças no tabuleiro\n")
            jogadorUsuario = True
            if(jogo == 0):
                print("Computador ganhou!")
                ComputadorVenceu = 1
import os # biblioteca para usar a funcao de limpar tela   

print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada.")
print("2 - para jogar um campeonato.")
escolha = int(input())
continuar = True
while(continuar):
    if(escolha == 1):
        input("Você escolheu partida isolada.")
        os.system('clear')
        partida()
        break
    if(escolha == 2):
        input("Você escolheu campeonato.")
        break;
    else:
        os.system('clear')
        print("Valor Invalido!")
        print("1 - para jogar uma partida isolada.")
        print("2 - para jogar um campeonato.")
        input()
        continuar == True
