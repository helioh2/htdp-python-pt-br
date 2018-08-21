#!/usr/bin/env python
# -*- coding: utf-8 -*-
from htdp_pt_br.base import *

'''
String, Fonte, Cor, Int -> Surface
'''
def texto(str, fonte, cor, largura):
    def wrap_text(text, font, width):
        """Wrap text to fit inside a given width when rendered.
        :param text: The text to be wrapped.
        :param font: The font the text will be rendered in.
        :param width: The width to wrap to.
        """
        text_lines = text.replace('\t', '    ').split('\n')
        if width is None or width == 0:
            return text_lines

        wrapped_lines = []
        for line in text_lines:
            line = line.rstrip() + ' '
            if line == ' ':
                wrapped_lines.append(line)
                continue

            # Get the leftmost space ignoring leading whitespace
            start = len(line) - len(line.lstrip())
            start = line.index(' ', start)
            while start + 1 < len(line):
                # Get the next potential splitting point
                next = line.index(' ', start + 1)
                if font.size(line[:next])[0] <= width:
                    start = next
                else:
                    wrapped_lines.append(line[:start])
                    line = line[start + 1:]
                    start = line.index(' ')
            line = line[:-1]
            if line:
                wrapped_lines.append(line)
        return wrapped_lines

    def render_text_list(lines, font, colour=(255, 255, 255)):
        """Draw multiline text to a single surface with a transparent background.
        Draw multiple lines of text in the given font onto a single surface
        with no background colour, and return the result.
        :param lines: The lines of text to render.
        :param font: The font to render in.
        :param colour: The colour to render the font in, default is white.
        """
        rendered = [font.render(line, True, colour).convert_alpha()
                    for line in lines]

        line_height = font.get_linesize()
        width = max(line.get_width() for line in rendered)
        tops = [int(round(i * line_height)) for i in range(len(rendered))]
        height = tops[-1] + font.get_height()

        surface = pg.Surface((width, height)).convert_alpha()
        surface.fill((0, 0, 0, 0))
        for y, line in zip(tops, rendered):
            surface.blit(line, (0, y))

        return surface

    lines = wrap_text(str, fonte, largura)
    return render_text_list(lines, fonte, cor)



'''
FUNÇÕES PARA CRIAÇÃO DE IMAGENS E FIGURAS GEOMÉTRICAS
'''

'''
Int, Int, Cor -> Surface
'''
def elipse(largura, altura, cor):
    img = pg.Surface((largura, altura), pg.SRCALPHA)  # imagem vazia
    pg.draw.ellipse(img, cor, (0, 0, largura, altura))
    return img

'''
Int, Int, Cor -> Surface
'''
def retangulo(largura, altura, cor):
    img = pg.Surface((largura, altura), pg.SRCALPHA)  # imagem vazia
    pg.draw.rect(img, cor, (0, 0, largura, altura))
    return img

'''
Int, Cor -> Surface
'''
def circulo(raio, cor):
    img = pg.Surface((raio*2, raio*2), pg.SRCALPHA)  # imagem vazia
    pg.draw.circle(img, cor, (raio, raio), raio)
    return img

'''
Int, Cor -> Surface
'''
def quadrado(lado, cor):
    return retangulo(lado, lado, cor)


def poligono(lista_de_pontos, cor):
    return

'''
Int, Int -> Surface
'''
def folha_transparente(largura, altura):
    folha = pg.Surface((largura, altura), pg.SRCALPHA)
    return folha

'''
Surface, Int, Int -> Surface
'''
def definir_dimensoes(imagem, largura, altura):
    return pg.transform.scale(imagem, (largura, altura))


def girar(imagem, angulo):
    return pg.transform.rotate(imagem, angulo)

'''
String, [Int, Int, Surface] -> Surface
Carrega imagem de arquivo. Se não for possível carregar, insere uma imagem substituta.
'''
def carregar_imagem(nome_arquivo, largura=100, altura=None, img_substituta=None):
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
Surface, Surface -> Surface
Coloca uma imagem ao lado da outra
'''
def lado(img1, img2):
    fundo = folha_transparente(img1.get_width() + img2.get_width(),
                                    max(img1.get_height(), img2.get_height()))
    colocar_imagem(img1, fundo, img1.get_width()//2, fundo.get_height()//2)
    colocar_imagem(img2, fundo, img1.get_width() + img2.get_width()//2, fundo.get_height()//2)
    return fundo


'''
Surface, Surface -> Surface
Coloca uma imagem acima da outra
'''
def encima(img1, img2):
    fundo = folha_transparente(max(img1.get_width(), img2.get_width()),
                               img1.get_height() + img2.get_height())
    colocar_imagem(img1, fundo, fundo.get_width()//2, img1.get_height()//2)
    colocar_imagem(img2, fundo, fundo.get_width()//2, img1.get_height() + img2.get_height()//2)
    return fundo

'''
Surface, Surface -> Surface
Sobrepõe imagens, de modo a facilitar a geração de imagens.
'''
def sobrepor(img1, img2):
    altura_maxima = max(img1.get_height(), img2.get_height())
    largura_maxima = max(img1.get_width(), img2.get_width())
    fundo = folha_transparente(largura_maxima, altura_maxima)
    fundo = colocar_imagem(img2, fundo, largura_maxima//2, altura_maxima//2)
    fundo = colocar_imagem(img1, fundo, largura_maxima//2, altura_maxima//2)
    return fundo


def largura_imagem(img):
    return img.get_width()

def altura_imagem(img):
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
    img2.blit(img1, (x - img1.get_width()//2, y - img1.get_height()//2))
    return img2


def mostrar(funcao_desenha, *args):
    '''
    :param funcao_desenha: Funcao que retorna imagem
    :param args:
    :return:
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
    mostrar(colocar_imagem, img, tela, x, y)


