#!/usr/bin/env python
# -*- coding: utf-8 -*-

###Based on https://github.com/zhemao/funktown


class ListaImutavel(object):
    def __init__(self, *args):
        if len(args) == 0:
            self._vazia = True
            self._cabeca = None
            self._cauda = None

        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            if len(args[0]) == 0:
                self._vazia = True
                self._cabeca = None
                self._cauda = None
            else:
                self._cabeca = args[0][0]
                if len(args[0]) > 1:
                    self._cauda = ListaImutavel(args[0][1:])
                else: self._cauda = ListaImutavel()
                self._vazia = False

        elif len(args) == 2 and isinstance(args[1], ListaImutavel):
            self._cabeca = args[0]
            self._cauda = args[1]
            self._vazia = False

    def conj(self, itm):
        return ListaImutavel(itm, self)

    @property
    def primeiro(self):
        return self._cabeca

    @property
    def resto(self):
        if self._vazia:
            return self
        return self._cauda

    @property
    def segundo(self):
        if self._vazia:
            return None
        return self._cauda._head

    @property
    def vazia(self):
        return self._vazia


    def reverte(self):
        new_list = ListaImutavel()
        for item in self:
            new_list = new_list.conj(item)
        return new_list

    def concat(self, lista2):
        new_list = lista2
        for item in self.reverte():
            new_list = new_list.conj(item)
        return new_list

    def __contains__(self, itm):
        if self._vazia:
            return False
        if self._cabeca == itm:
            return True
        return itm in self._cauda

    def __iter__(self):
        node = self
        while not node._vazia:
            yield node._cabeca
            node = node._cauda

    def __eq__(self, other):
        if other is None:
            return False

        if not hasattr(other, '__iter__'):
            return False

        node = self

        for itm in other:
            if node._vazia:
                return False
            if node._cabeca != itm:
                return False
            node = node._cauda

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        if self._vazia:
            return 0
        else:
            return 1 + len(self._cauda)

    def __str__(self):
        return '[' + ', '.join([str(x) for x in self]) + ']'

    def __repr__(self):
        return 'Lista(' + str(self) + ')'



def criar_lista(*args):
    return ListaImutavel(args)

VAZIA = criar_lista()

def vazia(lista):
    if not isinstance(lista, ListaImutavel):
        raise ValueError("ERRO: Você passou algo que não é uma lista.")
    return lista.vazia

def conj(item, lista):
    '''
    Immutable list creator.
    :param item:
    :param list:
    :return:
    '''
    if not isinstance(lista, ListaImutavel):
        raise ValueError("ERRO: Você passou algo que não é uma lista.")
    return lista.conj(item)


def primeiro(lista):
    '''

    :param list:
    :return:
    '''
    if not isinstance(lista, ListaImutavel):
        raise ValueError("ERRO: Você passou algo que não é uma lista.")
    return lista.primeiro

def resto(lista):
    '''

    :param list:
    :return:
    '''
    if not isinstance(lista, ListaImutavel):
        raise ValueError("ERRO: Você passou algo que não é uma lista.")
    return lista.resto


def reverte(lista):
    if not isinstance(lista, ListaImutavel):
        raise ValueError("ERRO: Você passou algo que não é uma lista.")
    else:
        return lista.reverte()


def concat(lista1, lista2):
    if not isinstance(lista1, ListaImutavel) or not isinstance(lista2, ListaImutavel) :
        raise ValueError("ERRO: Você passou algo que não é uma lista.")
    return lista1.concat(lista2)