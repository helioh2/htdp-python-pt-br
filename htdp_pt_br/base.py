#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg

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
    '''
    Define uma estrutura de dados compostos (uma classe).
    Por padrão, a estrutura é imutável, mas pode-se criar mutáveis setando 'mutavel=True'.
    :param nome: String -- nome do tipo
    :param campos: List<String> -- lista com os nomes dos campos
    :param mutavel: Boolean [=False]
    :return: retorna um tipo de dado definido pelo programador.
    '''
    if isinstance(campos, tuple):
        campos = list(campos)
    if not mutavel:
        from collections import namedtuple
        return namedtuple(nome, campos)
    else:
        from namedlist import namedlist
        return namedlist(nome, campos)
