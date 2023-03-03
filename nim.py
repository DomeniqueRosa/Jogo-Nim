def computador_escolhe_jogada(jogo,m):
    #Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar
    #  sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível,
    #  deverá tirar o número máximo de peças possíveis.
    #arrumar a quantidade de peças que o computador pode tirar
    retorna =True
    cont = m
    if((jogo - cont) % (m + 1)  == 0):
        pecas_retiradas = cont
        return pecas_retiradas
    else:
        while(cont >=1):
            if((jogo - cont ) % (m + 1) == 0):
                pecas_retiradas = cont
                return pecas_retiradas
            else:
                if(cont == 1):
                    pecas_retiradas = m
                    return pecas_retiradas
                else:
                    cont -=1
def campeonato():
    i = 1
    usuario =0
    pc =0
    while(i <= 3):
        print("**** RODADA",i,"*****")
        quemGanhou = partida()
        if(quemGanhou == 1):
            usuario += 1
            i +=1
        else:
            pc += 1
            i +=1
    
    print("***** RODADA FINAL ****** ")
    print("Placar : Você", usuario,"X", pc, "Computador")
  
def usuario_escolhe_jogada(n,m):
    retorna = True
    while(retorna):

        pecas_retiradas = int(input("Quantas peças você vai retirar? "))
        
        if(pecas_retiradas <= m and pecas_retiradas >0):
            #pecas_restantes = n - pecas_retiradas
            return pecas_retiradas     
        else:
            print("valor invalido")
            retorna = True
def partida():
    retorna = True
    while(retorna):
        n =int(input("Quantas peças? "))
        m =int(input("Limite de peças por jogada? "))

        if(n<m or n < 0 or m < 0):
            print("jogada invalida")
            retorna = True
        else:
            retorna = False
    jogo = n
    
    print("O jogo tem ",jogo,"peças ")
    if  n % (m+1)  == 0:
        jogadorUsuario = True
        print("Você começa!")
    else:
        print("Computador começa!")
        jogadorUsuario = False
        
    #retornar o numero de peças que sobrara
    while(jogo >0):
        if(jogadorUsuario):
            pecasRetiradas = usuario_escolhe_jogada(jogo,m)
            pecasRestantes = jogo - pecasRetiradas
            print("Você tirou",pecasRetiradas,"peça")
            jogo = jogo - pecasRetiradas
            print("Agora restam", jogo,"peças no tabuleiro\n")
            jogadorUsuario = False
            if(jogo == 0):
                print("Você ganhou!")
                #diferenciar os jogadores para somar na partida
                UsuarioVenceu = 1 
                return UsuarioVenceu  
        else:
            pecasRetiradas = computador_escolhe_jogada(jogo,m)
            pecasRestantes = jogo - pecasRetiradas
            print("O computador retirou ",pecasRetiradas,"peça")
            jogo = jogo - pecasRetiradas
            print("Agora restam", pecasRestantes,"peças no tabuleiro\n")
            jogadorUsuario = True
            if(jogo == 0):
                print("Computador ganhou!")
                ComputadorVenceu = 0
                return ComputadorVenceu
import os # biblioteca para usar a funcao de limpar tela   

print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada.")
print("2 - para jogar um campeonato.")
escolha = int(input())
continuar = True
while(continuar):
    if(escolha == 1):
        input("Você escolheu partida isolada.")

        #os.system('clear') funcao para limpar tela
        partida()
        break
    if(escolha == 2):
        input("Você escolheu campeonato.")
        campeonato()
        break;
    else:
        #os.system('clear')
        print("Valor Invalido!")
        print("1 - para jogar uma partida isolada.")
        print("2 - para jogar um campeonato.")
        input()
        continuar == True
