#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg
# from pysistence import make_list as cria_lista
# from pysistence.persistent_list import PList, EmptyList

from htdp_pt_br.list import *

pg.init()

Fonte = pg.font.SysFont
Cor = pg.color.Color

LARGURA_PADRAO = 400
ALTURA_PADRAO = 300
COR_BRANCO = (255, 255, 255)

def criar_tela_base(largura, altura):
    '''
    Cria tela base do aplicativo.
    :param largura: Int
    :param altura: Int
    :return: Tela
    '''
    tela = pg.display.set_mode((largura, altura))
    tela.fill(COR_BRANCO)
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





# VAZIA = cria_lista()
#
#
# def vazia(lista):
#     return not lista
#
# def cons(item, lista):
#     '''
#     Immutable list creator.
#     :param item: Object
#     :param list: Tuple[Object]
#     :return:
#     '''
#     if not isinstance(lista, PList) and not isinstance(lista, EmptyList):
#         raise ValueError("ERRO: Você passou algo que não é uma lista.")
#     return lista.cons(item)
#
#
# def primeiro(lista):
#     '''
#
#     :param list:
#     :return:
#     '''
#     if vazia(lista) or not isinstance(lista, PList):
#         raise ValueError("ERRO: Parece que você tentou pegar o primeiro de uma lista vazia")
#     return lista.first
#
# def resto(lista):
#     '''
#
#     :param list:
#     :return:
#     '''
#     if vazia(lista) or not isinstance(lista, PList):
#         raise ValueError("ERRO: Parece que você tentou pegar o resto de uma lista vazia")
#     return lista.rest
#
#
# def reverte(lista):
#     if vazia(lista):
#         return VAZIA
#     elif not isinstance(lista, PList):
#         raise ValueError("ERRO: Parece que você passou algo que não é uma lista")
#     else:
#         return lista.reverse()
#
#
# def remove(itens, lista):
#     if vazia(lista):
#         return VAZIA
#     elif not isinstance(lista, PList):
#         raise ValueError("ERRO: Parece que você passou algo que não é uma lista")
#     else:
#         return lista.without(itens)
#
# def concatena(lista1, lista2):
