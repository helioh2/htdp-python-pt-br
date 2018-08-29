#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *

''' Programa do Foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (400, 400)
tela = criar_tela_base(LARGURA, ALTURA)

L_FOGUETE = 100
A_FOGUETE = 100
IMG_FOGUETE = carregar_imagem('foguete.png', L_FOGUETE, A_FOGUETE)    #os.path.join('', 'cat1.png'))




# X = 200  #numero magico
X = LARGURA // 2


'''==================='''
'''# Definições de dados: '''

''' Foguete é Int[0,ALTURA] 
interp. representa a posicao y do foguete em pixels
Exemplos:
'''
F_INICIAL = 0
F_MEIO = ALTURA//2
F_FINAL = ALTURA
'''Template:
def fn_para_foguete(y):
    if y > ALTURA or y < 0:
        return "Foguete invalido"
    else:
        ... y
'''



'''===================='''
''' Funções: '''

'''
desce: Foguete -> Foguete
Faz o foguete descer 3 pixels no eixo y, se não estiver no chao
'''
def desce(y):
    if y > ALTURA or y < 0:
        return "Foguete invalido"
    else:
        if y >= ALTURA - 2:
            return ALTURA
        else:
            return y + 3


'''
desenha: Foguete -> Imagem
Desenha foguete na tela
'''
def desenha(y):
    # pg.draw.circle(TELA, (203,230,67), (X, y), 20)
    img = colocar_imagem(IMG_FOGUETE, tela, X, y - A_FOGUETE + 28)
    return img


''' ================= '''
''' Main (Big Bang):
'''

''' Foguete -> Foguete '''
''' inicie o mundo com main()'''
# def main():
#     big_bang(F_INICIAL,
#              quando_tick=desce, \
#              desenhar=desenha)
#
#
#
# main()
# mostrar(desenha, 400)
# animar(desenha)

# tela = colocar_imagem(IMG_FOGUETE, tela, 200, 200)
# mostrar_tela()

colocar_imagem_sobre_tela_e_mostrar(IMG_FOGUETE, 200, 200)
    
