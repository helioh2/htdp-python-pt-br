#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg
# import sys, os

pg.init()

Fonte = pg.font.SysFont
Cor = pg.color.Color

LARGURA_PADRAO = 400
ALTURA_PADRAO = 300
COR_BRANCO = (255, 255, 255)
cor_fundo = COR_BRANCO

def criar_tela_base(largura, altura, fundo=Cor("white")):
    '''
    Cria tela base do aplicativo.
    :param largura: Int
    :param altura: Int
    :param fundo: Cor
    :return: Tela
    '''
    tela = pg.display.set_mode((largura, altura))
    tela.fill(fundo)
    global cor_fundo
    cor_fundo = fundo
    return tela

tela = criar_tela_base(LARGURA_PADRAO, ALTURA_PADRAO)

def definir_estrutura(nome, campos, mutavel=False):
    if isinstance(campos, tuple):
        campos = list(campos)
    if not mutavel:
        from collections import namedtuple
        return namedtuple(nome, campos)
    else:
        from namedlist import namedlist
        return namedlist(nome, campos)
