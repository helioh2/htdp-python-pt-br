#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import random

from htdp_pt_br.universe import *

''' Meu programa da vaquinha 2.0 (com um chupacabra) '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_VACA_INO = pg.image.load('vaca-ino.png')    #os.path.join('', 'cat1.png'))
    IMG_VACA_VORTANO = pg.transform.flip(IMG_VACA_INO, True, False)
    IMG_CC_VORTANO = pg.image.load('chupacabra.jpg')
    IMG_CC_VORTANO = pg.transform.scale(IMG_CC_VORTANO, (20,20))
    IMG_CC_INO = pg.transform.flip(IMG_CC_VORTANO, True, False)
except:
    IMG_VACA_INO = pg.Surface((100,100),pg.SRCALPHA)  #imagem vazia para o caso de nao funcionar o carregamento
    IMG_VACA_VORTANO = pg.Surface((100,100),pg.SRCALPHA)
    IMG_CC_VORTANO = pg.Surface((100,100),pg.SRCALPHA)
    IMG_CC_INO = pg.Surface((100,100),pg.SRCALPHA)
    print("ERRO: Imagens nao foram carregadas.")

CHAO = ALTURA - IMG_VACA_INO.get_height() // 2
X_CC = LARGURA // 2

PAREDE_ESQUERDA = 0 + IMG_VACA_INO.get_width()//2
PAREDE_DIREITA = LARGURA - IMG_VACA_INO.get_width()//2

PAREDE_CIMA = IMG_CC_INO.get_height()//2
PAREDE_BAIXO = ALTURA - IMG_CC_INO.get_height()//2

DX = 3
G = 3


'''==================='''
'''# Definições de dados: '''

from namedlist import namedlist
Vaca = definir_estrutura("Vaca", "x, dx, y, dy")  #estrutura da Vaca

''' Vaca pode ser criada como: Vaca(Int[PAREDE_ESQUERDA,PAREDE_DIREITA], Int)
interp.: representa a posicao x da vaca, e o deslocamento
a cada tick no eixo x, chamado de dx
Exemplos:
'''
VACA_INICIAL = Vaca(PAREDE_ESQUERDA, 0, 0, 0)
# VACA_MEIO = Vaca(LARGURA//2, 3)
VACA_FIM = Vaca(LARGURA, 3, CHAO, 0)
VACA_VIRANDO = Vaca(LARGURA, -3, CHAO, 0)
VACA_VOLTANDO = Vaca(LARGURA // 2, -3, CHAO, 0)
'''
Template para funções que recebem Vaca:
def fn_para_vaca(v):
    if v.x < 0 or v.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        ... v.x
            v.dx

'''

Chupacabra = definir_estrutura("Chupacabra", "x, y, dy")  #estrutura do Chupacabra

''' Chupacabra pode ser criada como: Chupacabra(Int[PAREDE_ESQUERDA, PAREDE_DIREITA], Int[PAREDE_CIMA, PAREDE_BAIXO], Int)
interp.: representa a posicao x e y do chupacabra, e o deslocamento
a cada tick no eixo y, chamado de dy
Exemplos:
'''
CC_INICIAL = Chupacabra(X_CC, PAREDE_CIMA, 3)
CC_MEIO = Chupacabra(X_CC, ALTURA//2, 3)
CC_FIM = Chupacabra(X_CC, PAREDE_BAIXO, 3)
CC_VIRANDO = Chupacabra(X_CC, PAREDE_BAIXO, -3)
CC_VOLTANDO = Chupacabra(X_CC, ALTURA//2, -3)

CC2 = Chupacabra(int(LARGURA*0.75), ALTURA//2, 3)
CC3 = Chupacabra(LARGURA//4, PAREDE_BAIXO, 3)


'''
Template para funções que recebem Chupacabra:
def fn_para_cc(cc):
    if cc.y < 0 or cc.y > LARGURA:
        return "Erro: cc invalido"
    else:
        ... cc.y
            cc.dy
'''

Jogo = definir_estrutura("Jogo", "vaca, chupacabras, game_over, spawn_timeout, cont")

''' Jogo eh criado como: Jogo(Vaca, List<Chupacabra>, Boolean)
interp. Um jogo é composto por uma vaca, vários chupacabras,
e uma flag (game_over) que indica se o jogo está acontecendo
ou nao
Exemplos:
'''
JOGO_INICIAL0 = Jogo(VACA_INICIAL, [CC_INICIAL], False, 1, 0)
JOGO_GAME_OVER = Jogo(Vaca(X_CC, 3, CHAO, 0), [Chupacabra(X_CC, CHAO, 3)], True, 1, 0)

JOGO_INICIAL = Jogo(VACA_INICIAL, criar_lista(CC2, CC_INICIAL, CC3), False, 1, 0)


'''Template para funcao que recebe Jogo:
def fn_para_jogo(jogo):
    ... jogo.vaca
        jogo.chupacabra
        jogo.game_over
'''




'''===================='''
''' Funções: '''

'''
mover_vaca_x: Vaca -> Vaca
Produz a próxima vaca (ou seja, fazer ela andar)
'''
def mover_vaca_x(vaca):
    if vaca.x < 0 or vaca.x > LARGURA:
        raise ValueError("Erro: vaca invalida")
    else:
        #calcula novo dx
        dx = vaca.dx
        if (vaca.x == PAREDE_DIREITA and vaca.dx > 0) \
                or (vaca.x == PAREDE_ESQUERDA and vaca.dx < 0):  #se vaca bateu na parede
            dx = - dx
        #usar depurador (debugger)

        #calcula novo x
        x = vaca.x + vaca.dx

        if vaca.x > PAREDE_DIREITA:
            x = PAREDE_DIREITA
        elif vaca.x < PAREDE_ESQUERDA:
            x = PAREDE_ESQUERDA

        return Vaca(x, vaca.dx, vaca.y, vaca.dy)



'''
mover_cc: Chupacabra -> Chupacabra
Mover o chupacabra no eixo y usando o dy
'''
def mover_cc(chupacabra):
    if chupacabra.y < 0 or chupacabra.y > ALTURA:
        raise ValueError("Erro: chupacabra invalida")
    else:
        #calcula novo dy
        dy = chupacabra.dy
        if (chupacabra.y == PAREDE_BAIXO and chupacabra.dy > 0) \
                or (chupacabra.y == PAREDE_CIMA and chupacabra.dy < 0):  #se vaca bateu na parede
            dy = - dy
        #usar depurador (debugger)

        #calcula novo y
        y = chupacabra.y + chupacabra.dy

        if chupacabra.y > PAREDE_BAIXO:
            y = PAREDE_BAIXO
        elif chupacabra.y < PAREDE_CIMA:
            y = PAREDE_CIMA

        return Chupacabra(chupacabra.x, y, dy)


'''distancia: Int Int Int Int -> Float
Calcula a distancia entre dois pontos
'''
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)



'''
colidirem: Vaca, Chupacabra -> Boolean
Verifica se a vaca e o chupacabra colidiram
'''
def colidirem(vaca, chupacabra):
    raio1 = IMG_VACA_INO.get_width()/2
    raio2 = IMG_CC_VORTANO.get_width()/2
    d = distancia(vaca.x, vaca.y, chupacabra.x, chupacabra.y)
    if d <= raio1 + raio2:
        return True
    #else
    return False


def colidirem2(vaca, chupacabras):
    if vazia(chupacabras):
        return False
    else:
        return colidirem(vaca, primeiro(chupacabras)) or colidirem2(vaca, resto(chupacabras))
'''
mover_vaca_y: Vaca -> Int
Movimenta vaca no eixo y de acordo com dy
'''
def mover_vaca_y(vaca):
    y = vaca.y
    if vaca.y == CHAO:
        dy = 0
    else:
        dy = vaca.dy + G
        y = vaca.y + dy

        if y >= CHAO:
            y = CHAO
            dy = 0
    return Vaca(vaca.x, vaca.dx, y, dy)


def mover_ccs(ccs):
    if ccs.vazia:
        return VAZIA
    else:
        return conj(mover_cc(primeiro(ccs)), mover_ccs(resto(ccs)))


'''
mover_jogo: Jogo -> Jogo
A funcao que eh chamada a cada tick para o jogo
'''
def mover_jogo(jogo):

    colidirem2(jogo.vaca, jogo.chupacabras)

    vaca = mover_vaca_x(mover_vaca_y(jogo.vaca))
    ccs = mover_ccs(jogo.chupacabras)

    spawn_timeout = jogo.spawn_timeout - 1
    if spawn_timeout == 0:
        x = random.randrange(PAREDE_ESQUERDA, PAREDE_DIREITA)
        y = random.randrange(PAREDE_CIMA, PAREDE_BAIXO)
        novo_cc = Chupacabra(x, y, 3)
        ccs = conj(novo_cc, ccs)
        spawn_timeout = 1

    return Jogo(vaca, ccs, jogo.game_over, spawn_timeout, jogo.cont+1)


'''
desenha_vaca: Vaca -> Imagem
Desenha a vaca na tela
'''
def desenha_vaca(vaca):
    if vaca.dx < 0:
        TELA.blit(IMG_VACA_VORTANO,
                  (vaca.x - IMG_VACA_VORTANO.get_width() // 2,
                   vaca.y - IMG_VACA_VORTANO.get_height() // 2))
    else:
        TELA.blit(IMG_VACA_INO,
                  (vaca.x - IMG_VACA_INO.get_width() // 2,
                   vaca.y - IMG_VACA_INO.get_height() // 2))


'''
desenha_chupacabra: Chupacabra -> Imagem
Desenha o chupacabra
'''
def desenha_chupacabra(chupacabra):
    TELA.blit(IMG_CC_VORTANO,
              (chupacabra.x - IMG_CC_VORTANO.get_width() // 2,
               chupacabra.y - IMG_CC_VORTANO.get_height() // 2))


'''
desenha_jogo: Jogo -> Imagem
Desenha o jogo
'''
def desenha_jogo(jogo):
    if jogo.game_over:
        fonte = pg.font.SysFont("monospace", 40)
        ## render: String, Int, Cor

        texto = fonte.render("GAME OVER", 1, (255, 0, 0))

        ## blit: String, (Int, Int)
        TELA.blit(texto, (LARGURA // 2 - 20, ALTURA // 2 - 20))

    else:
        desenha_vaca(jogo.vaca)

        # antes
        # desenha_chupacabra(jogo.chupacabra)

        # depois
        for chupacabra in jogo.chupacabras:
            desenha_chupacabra(chupacabra)


'''
trata_tecla_vaca: Vaca, EventoTecla -> Vaca
Quando teclar espaço, inverte a direção da vaca
'''
def trata_tecla_vaca(vaca, tecla):
    # if tecla == pg.K_SPACE:
    #     vaca.dx = - vaca.dx
    # if tecla == pg.K_LEFT:
    #     vaca.x = vaca.x - abs(vaca.dx)
    # elif tecla == pg.K_RIGHT:
    #     vaca.x = vaca.x + abs(vaca.dx)
    if tecla == pg.K_LEFT:
        return Vaca(vaca.x, -DX, vaca.y, vaca.dy)
    elif tecla == pg.K_RIGHT:
        return Vaca(vaca.x, DX, vaca.y, vaca.dy)
    elif tecla == pg.K_UP and vaca.y == CHAO:

        return Vaca(vaca.x, vaca.dx, vaca.y - 10, -20)
    else:
        return vaca


'''
trata_tecla: Jogo, EventoTecla -> Jogo
Trata tecla geral
'''
def trata_tecla(jogo, tecla):
    if jogo.game_over and tecla == pg.K_SPACE :
        return JOGO_INICIAL
    else:
        vaca = trata_tecla_vaca(jogo.vaca, tecla)
        return Jogo(vaca, jogo.chupacabras, jogo.game_over, jogo.spawn_timeout, jogo.cont+1)


'''                                             
trata_solta_tecla: Vaca, EventoTecla -> Vaca    
Trata solta tecla vaca                 
'''
def trata_solta_tecla_vaca(vaca, tecla):
   if tecla == pg.K_LEFT or tecla == pg.K_RIGHT:
       return Vaca(vaca.x, 0, vaca.y, vaca.dy)
   return vaca

'''trata_solta_tecla: Jogo, EventoTecla -> Jogo
Trata solta tecla geral
'''
def trata_solta_tecla(jogo, tecla):
    vaca = trata_solta_tecla_vaca(jogo.vaca, tecla)
    return Jogo(vaca, jogo.chupacabras, jogo.game_over, jogo.spawn_timeout, jogo.cont+1)

''' ================= '''
''' Main (Big Bang):
'''

''' Jogo -> Jogo '''
''' inicie o mundo com main(JOGO_INICIAL) '''

def main(inic):

    big_bang(inic, tela=TELA,
             frequencia=0,
             quando_tick=mover_jogo,
             # desenhar=desenha_jogo,
             quando_tecla=trata_tecla,
             quando_solta_tecla=trata_solta_tecla,
             parar_quando=lambda j: j.cont > 500,
             modo_debug=True,
             fonte_debug=15
             )

main(JOGO_INICIAL)

