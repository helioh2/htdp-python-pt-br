#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *

''' Programa do Foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (400, 400)
TELA = criar_tela_base(LARGURA, ALTURA)

L_FOGUETE = 60
A_FOGUETE = 100
# IMG_FOGUETE = retangulo(60, 100, pg.color.Color("darkred"))
# IMG_FOGUETE = girar(IMG_FOGUETE, 45)
# BOLA = circulo(50, Cor("yellow"))
# IMG_FOGUETE = sobrepor(IMG_FOGUETE, BOLA)

# IMG_FOGUETE = poligono([(0,0), (100, 0), (100,100), (0,100)], Cor("darkred"), 2)
IMG_FOGUETE = linha((100,0), (0,100), Cor("darkred"), 5)
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
    colocar_imagem(IMG_FOGUETE, TELA, X, y - A_FOGUETE + 28)

''' ================= '''
''' Main (Big Bang):
'''

''' Foguete -> Foguete '''
''' inicie o mundo com main()'''
def main():
    big_bang(F_INICIAL, tela=TELA,
             quando_tick=desce, \
             desenhar=desenha,
             modo_debug=True)



main()
# colocar_imagem_sobre_tela_e_mostrar(IMG_FOGUETE, 50, 50)
# pg.draw.rect(TELA, "Red", )
    
