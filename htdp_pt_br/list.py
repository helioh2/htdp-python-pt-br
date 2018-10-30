#!/usr/bin/env python
# -*- coding: utf-8 -*-

###Based on https://github.com/zhemao/funktown


class ListaImutavel(object):
    def __init__(self, *args):
        if len(args) == 0:
            self._vazia = True
            self._cabeca = None
            self._cauda = None
            self._tamanho = 0

        elif len(args) == 1 and isinstance(args[0], (list, tuple, set)):
            if len(args[0]) == 0:
                self._vazia = True
                self._cabeca = None
                self._cauda = None
                self._tamanho = 0
            else:
                self._cabeca = args[0][0]
                if len(args[0]) > 1:
                    self._cauda = ListaImutavel(args[0][1:])
                else:
                    self._cauda = ListaImutavel()
                self._vazia = False
                self._tamanho = len(args[0])

        elif len(args) == 2 and isinstance(args[1], ListaImutavel):
            self._cabeca = args[0]
            self._cauda = args[1]
            self._vazia = False
            self._tamanho = len(args[1]) + 1

    def juntar(self, itm):
        return ListaImutavel(itm, self)

    junta = cons = conj = juntar

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
            new_list = new_list.juntar(item)
        return new_list

    def concat(self, lista2):
        new_list = lista2
        for item in self.reverte():
            new_list = new_list.juntar(item)
        return new_list

    def map(self, func):
        if self.vazia:
            return self
        else:
            return juntar(func(self.primeiro),
                          self.resto.map(func))

    def reduce(self, func, acc=0):
        result = acc
        for valor in self:
            result = func(valor, result)
        return result

    def filter(self, func):
        if self.vazia:
            return self
        else:
            if func(self.primeiro):
                return juntar(self.primeiro,
                              self.resto.filter(func))
            else:
                return self.resto.filter(func)

    def andmap(self, func):
        if self.vazia:
            return True
        else:
            return func(self.primeiro) and self.resto.andmap(func)

    def ormap(self, func):
        if self.vazia:
            return False
        else:
            return func(self.primeiro) or self.resto.ormap(func)

    def remove_all(self, item):
        return self.filter(lambda x: x != item)

    def remove(self, item):
        if self.vazia:
            return self
        else:
            if self.primeiro == item:
                return self.resto
            else:
                return juntar(self.primeiro, self.resto.remove(item))

    def fix_index(self, i):
        if i < 0:
            i += len(self)

        if i < 0 or i >= len(self):
            raise IndexError("Tentou acessar índice fora do limite")

        return i

    def getslice(self, slice):
        start = 0 if slice.start is None else self.fix_index(slice.start)
        stop = len(self) if slice.stop is None else self.fix_index(slice.stop)
        count = 0
        nova = VAZIA
        for item in self:
            if count >= stop or count >= len(self):
                break
            if start <= count < stop:
                nova = juntar(item, nova)
            count += 1

        return nova.reverte()

    def __getitem__(self, i):

        if isinstance(i, slice):
            return self.getslice(i)

        i = self.fix_index(i)

        count = 0
        for item in self:
            if (i == count):
                return item
            count += 1

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
        return self._tamanho

    def __str__(self):
        return '[' + ', '.join([str(x) for x in self]) + ']'

    def __repr__(self):
        return 'Lista(' + str(self) + ')'


def criar_lista(*args):
    if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
        return ListaImutavel(args[0])
    return ListaImutavel(args)


VAZIA = criar_lista()


def vazia(lista):
    if not isinstance(lista, ListaImutavel):
        raise ValueError("ERRO: Você passou algo que não é uma lista.")
    return lista.vazia


def juntar(item, lista):
    '''
    Immutable list creator.
    :param item:
    :param list:
    :return:
    '''
    if not isinstance(lista, ListaImutavel):
        raise ValueError("ERRO: Você passou algo que não é uma lista.")
    return lista.juntar(item)

junta = cons = conj = juntar

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
    if not isinstance(lista1, ListaImutavel) or not isinstance(lista2, ListaImutavel):
        raise ValueError("ERRO: Você passou algo que não é uma lista.")
    return lista1.concat(lista2)
