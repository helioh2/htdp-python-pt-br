#!/usr/bin/env python
# -*- coding: utf-8 -*-
from htdp_pt_br.image import *

def big_bang(inic,
             tela=tela,
             quando_tick=lambda e: e,
             frequencia=28,
             desenhar=lambda e: tela.blit(texto("NADA A MOSTRAR. VERIFIQUE SE VOCÊ PASSOU A FUNÇÃO DE DESENHHAR PARA O BIG-BANG", Fonte("monospace",30),
                                                Cor("red"), tela.get_width()), (0, tela.get_height()//2)),
             quando_tecla=lambda e, k: e, \
             quando_solta_tecla=lambda e, k: e, \
             quando_mouse=lambda e, x, y, ev: e, \
             parar_quando=lambda e: False,\
             modo_debug=False,
             fonte_debug = 15):

    # pg.init()
    estado = inic
    clock = pg.time.Clock()

    while True:

        pg.display.flip()

        if parar_quando(estado):
            print(estado)
            sys.exit(0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print(estado)
                sys.exit(0)

            if event.type == pg.KEYDOWN:
                estado = quando_tecla(estado, event.key)
            elif event.type == pg.KEYUP:
                estado = quando_solta_tecla(estado, event.key)
            elif event.type in [pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.MOUSEMOTION]:
                x, y = pg.mouse.get_pos()
                estado = quando_mouse(estado, x, y, event.type)

        estado = quando_tick(estado)

        tela.fill(cor_fundo)
        desenhar(estado)
        if modo_debug:
            escreve_estado(estado, fonte_debug)

        clock.tick(frequencia)


def animar(a_cada_tick, frequencia=28):
    clock = pg.time.Clock()
    i = 0
    while True:
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print(i)
                sys.exit(0)

        tela.fill(COR_BRANCO)
        a_cada_tick(i)
        i += 1

        clock.tick(frequencia)

# def animar2(a_cada_tick, frequencia=28):
#     while True:
#         a_cada_tick(i)
#
#         clock.tick(frequencia)


def escreve_estado(estado, fonte_debug):
    myfont = pg.font.SysFont("monospace", fonte_debug)
    # texto = str(estado).split(',')
    import re
    texto = re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+', str(estado))

    counter = fonte_debug
    for line in texto:
        label = myfont.render(line, 1, (255, 0, 0))
        tela.blit(label, (5, counter))
        counter += fonte_debug


# def escreve_estado(estado, fonte_debug):
#     texto_img = texto(str(estado), Fonte("monospace", fonte_debug), Cor("red"), tela.get_width()//2)
#     tela.blit(texto_img, (5,5))




