#!/usr/bin/env python
# -*- coding: utf-8 -*-
from htdp_pt_br.base import *
import sys


'''
String, Fonte, Cor, Int -> Surface
'''
def texto(str, fonte, cor, largura=tela.get_width()):
    """
    Cria uma imagem com base em um texto.
    :param str: String -- o texto.
    :param fonte: Fonte -- a fonte (classe Fonte) do texto.
    :param cor: Cor -- a cor (classe Cor) do texto.
    :param largura: Int -- a largura na qual o texto deve estar contido. 
    """
    def embrulha_texto(texto, fonte, largura):
        
        linhas = texto.replace('\t', '    ').split('\n')
        if largura is None or largura == 0:
            return linhas

        linhas_embrulhadas = []
        for linha in linhas:
            linha = linha.rstrip() + ' '
            if linha == ' ':
                linhas_embrulhadas.append(linha)
                continue

            # Pega o espaço mais à esquerda, ignorando o espaço em branco inicial
            inicio = len(linha) - len(linha.lstrip())
            inicio = linha.index(' ', inicio)
            while inicio + 1 < len(linha):
                # Get the next potential splitting point
                proximo = linha.index(' ', inicio + 1)
                if fonte.size(linha[:proximo])[0] <= largura:
                    inicio = proximo
                else:
                    linhas_embrulhadas.append(linha[:inicio])
                    linha = linha[inicio + 1:]
                    inicio = linha.index(' ')
            linha = linha[:-1]
            if linha:
                linhas_embrulhadas.append(linha)
        return linhas_embrulhadas

    def desenha_lista_de_textos(linhas, fonte, cor=(255, 255, 255)):
        desenhado = [fonte.render(line, True, cor).convert_alpha()
                    for line in linhas]

        altura_linha = fonte.get_linesize()
        largura = max(linha.get_width() for linha in desenhado)
        topos = [int(round(i * altura_linha)) for i in range(len(desenhado))]
        altura = topos[-1] + fonte.get_height()

        surface = pg.Surface((largura, altura)).convert_alpha()
        surface.fill((0, 0, 0, 0))
        for y, linha in zip(topos, desenhado):
            surface.blit(linha, (0, y))

        return surface
    linhas = embrulha_texto(str, fonte, largura)
    return desenha_lista_de_textos(linhas, fonte, cor)



'''
FUNÇÕES PARA CRIAÇÃO DE IMAGENS E FIGURAS GEOMÉTRICAS
'''

'''
Int, Int, Cor -> Imagem
'''
def elipse(largura, altura, cor):
    '''
    Cria imagem de uma elipse.
    :param largura: Int
    :param altura: Int
    :param cor: Cor
    :return: Imagem
    '''
    img = pg.Surface((largura, altura), pg.SRCALPHA)  # imagem vazia
    pg.draw.ellipse(img, cor, (0, 0, largura, altura))
    return img

'''
Int, Int, Cor -> Imagem
'''
def retangulo(largura, altura, cor):
    '''
    Cria imagem de um retângulo.
    :param largura: Int
    :param altura: Int
    :param cor: Cor
    :return: Imagem
    '''
    img = pg.Surface((largura, altura), pg.SRCALPHA)  # imagem vazia
    pg.draw.rect(img, cor, (0, 0, largura, altura))
    return img

'''
Int, Cor -> Imagem
'''
def circulo(raio, cor):
    '''
    Cria imagem de um círculo.
    :param raio: Int
    :param cor: Cor
    :return: Imagem
    '''
    img = pg.Surface((raio*2, raio*2), pg.SRCALPHA)  # imagem vazia
    pg.draw.circle(img, cor, (raio, raio), raio)
    return img

'''
Int, Cor -> Imagem
'''
def quadrado(lado, cor):
    '''
    Cria imagem de um quadrado.
    :param lado: Int
    :param cor: Cor
    :return: Imagem
    '''
    return retangulo(lado, lado, cor)


def poligono(lista_de_pontos, cor, contorno = 0):
    '''
    Cria um polígono com base em uma lista de pontos (considere o canto inferior esquerdo como o ponto (0,0)).
    :param lista_de_pontos: List<Tuple(Int, Int)> -- lista de pares ordenados indicando os pontos que formam o polígono
    :param cor: Cor
    :param contorno [=0]: Int --- use um valor maior que 0 para que o poligono seja contornado. Caso seja 0 (padrão), o polígono sera preenchido.
    :return: Imagem
    '''
    max_x = max_y = 0
    min_x = min_y = sys.maxsize
    for x,y in lista_de_pontos:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
    if contorno > 0:
        for k in range(len(lista_de_pontos)):
            ponto = lista_de_pontos[k]
            if ponto[0] == min_x:
                lista_de_pontos[k] = (ponto[0] + contorno // 2, ponto[1])
            ponto = lista_de_pontos[k]
            if ponto[1] == min_y:
                lista_de_pontos[k] = (ponto[0], ponto[1] + contorno // 2)
    img = pg.Surface((max_x + contorno, max_y + contorno), pg.SRCALPHA)  # imagem vazia
    pg.draw.polygon(img, cor, lista_de_pontos, contorno)
    return img

def arco(largura, altura, angulo_inicio, angulo_fim, cor, contorno=1):
    '''
    Desenha um arco dentro de um espaço definido por largura e altura, dado um angulo inicial e um final.
    :param largura: Int
    :param altura: Int
    :param angulo_inicio: Int -- em graus
    :param angulo_fim: Int -- em graus
    :param contorno: Int
    :return: Imagem
    '''
    import math
    img = pg.Surface((largura, altura), pg.SRCALPHA)  # imagem vazia
    pg.draw.arc(img, cor, (0, 0, largura, altura), math.radians(angulo_inicio), math.radians(angulo_fim), contorno)
    return img


def linha(ponto_inicial, ponto_final, cor, contorno=1):
    '''
    Desenha uma linha, dado um ponto inicial e um ponto final (considere o canto inferior esquerdo como o ponto (0,0)).
    :param ponto_inicial: Tuple(Int, Int)
    :param ponto_final: Tuple(Int, Int)
    :param cor: Cor
    :param contorno: Int
    :return: Imagem
    '''
    max_x = max([ponto_inicial[0], ponto_final[0]])
    max_y = max([ponto_inicial[1], ponto_final[1]])
    img = pg.Surface((max_x, max_y), pg.SRCALPHA)  # imagem vazia
    pg.draw.line(img, cor, ponto_inicial, ponto_final, contorno)
    return img


'''
Int, Int -> Imagem
'''
def folha_transparente(largura, altura):
    '''
    Cria um fundo transparente no qual podem ser colocadas outras imagens.
    :param largura: Int
    :param altura: Int
    :return: Imagem
    '''
    folha = pg.Surface((largura, altura), pg.SRCALPHA)
    return folha

'''
Imagem, Int, Int -> Imagem
'''
def definir_dimensoes(imagem, largura, altura):
    '''
    Define dimensões (largura e altura) de uma imagem.
    :param imagem: Imagem
    :param largura: Int
    :param altura: Int
    :return: Imagem
    '''
    return pg.transform.scale(imagem, (largura, altura))

'''
Imagem, Int -> Imagem
'''
def girar(imagem, angulo):
    '''
    Girar imagem em um determinado ângulo
    :param imagem: Imagem
    :param angulo: Int -- em graus
    :return: Imagem
    '''
    return pg.transform.rotate(imagem, angulo)


def espelhar(imagem, horizontal=True, vertical=False):
    '''

    :param imagem:
    :param horizontal:
    :return:
    '''
    return pg.transform.flip(imagem, horizontal, vertical)

'''
String, [Int, Int, Imagem] -> Imagem
Carrega imagem de arquivo. Se não for possível carregar, insere uma imagem substituta.
'''
def carregar_imagem(nome_arquivo, largura=100, altura=None, img_substituta=None):
    '''
    Carregar imagem pelo nome do arquivo. Pode-se definir as dimensões (largura e altura) e uma
    imagem substituta para o caso de não conseguir carregar do arquivo.
    Caso não seja fornecida imagem substituta e o arquivo não puder ser carregado, será desenhado
    um texto informando o problema.
    :param nome_arquivo: String
    :param largura: Int (opcional)
    :param altura: Int (opcional)
    :param img_substituta: Imagem (opcional)
    :return: Imagem
    '''
    try:
        img = pg.image.load(nome_arquivo)
        if largura and altura:
            img = definir_dimensoes(img, largura, altura)
        return img
    except:
        img = img_substituta if img_substituta \
                else texto("Não foi possível carregar imagem", Fonte("monospace", 15), Cor("red"), largura)
        return img

'''
Imagem, Imagem -> Imagem
Coloca uma imagem ao lado da outra
'''
def lado(img1, img2):
    '''
    Recebe duas imagens e as posiciona uma ao lado da outra.
    :param img1: Imagem
    :param img2: Imagem
    :return: Imagem
    '''
    fundo = folha_transparente(img1.get_width() + img2.get_width(),
                                    max(img1.get_height(), img2.get_height()))
    colocar_imagem(img1, fundo, img1.get_width()//2, fundo.get_height()//2)
    colocar_imagem(img2, fundo, img1.get_width() + img2.get_width()//2, fundo.get_height()//2)
    return fundo


'''
Imagem, Imagem -> Imagem
Coloca uma imagem acima da outra
'''
def encima(img1, img2):
    '''
    Recebe duas imagens e as posiciona uma acima (no plano 2D) da outra.
    :param img1: Imagem
    :param img2: Imagem
    :return: Imagem
    '''
    fundo = folha_transparente(max(img1.get_width(), img2.get_width()),
                               img1.get_height() + img2.get_height())
    colocar_imagem(img1, fundo, fundo.get_width()//2, img1.get_height()//2)
    colocar_imagem(img2, fundo, fundo.get_width()//2, img1.get_height() + img2.get_height()//2)
    return fundo

'''
Imagem, Imagem -> Imagem
Sobrepõe imagens, de modo a facilitar a geração de imagens personalizadas.
'''
def sobrepor(img1, img2):
    '''
    Recebe duas imagens e as sobrepõe (img1 encima de img2).
    :param img1: Imagem
    :param img2: Imagem
    :return: Imagem
    '''
    altura_maxima = max(img1.get_height(), img2.get_height())
    largura_maxima = max(img1.get_width(), img2.get_width())
    fundo = folha_transparente(largura_maxima, altura_maxima)
    fundo = colocar_imagem(img2, fundo, largura_maxima//2, altura_maxima//2)
    fundo = colocar_imagem(img1, fundo, largura_maxima//2, altura_maxima//2)
    return fundo


def largura_imagem(img):
    '''
    Retorna a largura da imagem
    :param img: Imagem
    :return: Int
    '''
    return img.get_width()

def altura_imagem(img):
    '''
    Retorna a altura da imagem
    :param img: Imagem
    :return: Int
    '''
    return img.get_height()


'''
FUNÇÕES DE CRIAÇÃO DE TELA E SOBREPOSIÇÕES
'''

'''
Surface, Surface, Int, Int -> Surface		
Coloca uma imagem (tipo pg.Surface) sobre outra na posição x e y, considerando 
a posição da imagem como seu centro.
'''
def colocar_imagem(img1, img2, x, y):
    '''
    Coloca img1 sobre a img2 na posição x e y.
    :param img1: Imagem
    :param img2: Imagem
    :param x: Int
    :param y: Int
    :return: Imagem
    '''
    img2.blit(img1, (x - img1.get_width()//2, y - img1.get_height()//2))
    return img2


def mostrar(funcao_desenha, *args):
    '''
    Recebe uma função que retorna uma imagem e mostra na tela.
    :param funcao_desenha: Function: QualquerCoisa -> Imagem -- função que retorna imagem
    :param args: parâmetros da 'funcao_desenha'
    :return: mostra imagem na tela
    '''
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
        pg.display.flip()
        funcao_desenha(*args)

'''
Surface, Int, Int -> void
'''
def colocar_imagem_sobre_tela_e_mostrar(img, x, y):
    '''
    Coloca a imagem sobre a tela principal na posição x e y e mostra na tela.
    :param img: Imagem
    :param x: Int
    :param y: Int
    :return: mostra imagem na tela
    '''
    mostrar(colocar_imagem, img, tela, x, y)


def mostrar_tela():
    '''
    Mostra tela principal com a imagem atual.
    :return: mostra imagem na tela
    '''
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
        pg.display.flip()
        # tela.blit(folha_transparente(0, 0), (0, 0))

