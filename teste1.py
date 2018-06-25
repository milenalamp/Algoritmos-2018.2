# Milena Lamp / E-mail: lamp.milena@gmail.com
#Objetivo: Desenvolver um Jogo da Velha em Python, utilizando Pygame com o auxilio de funções.


import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#criando a tela e definindo o tamanho dela
tela = pygame.display.set_mode((600,600), 0 , 32)
pygame.display.set_caption('Jogo da velha')

ESTADO = 'JOGANDO'
VEZ = 'JOGADOR1'
ESCOLHA = 'X'
espaco = 0

marca_tabu = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]
#Rect é uma ferramenta de "Recorte" ela recorta cada quadrado desenhado
#pra poder manipular depois no jogo

rect1 = Rect((0,0), (200,200))
rect2 = Rect((200,0), (200,200))
rect3 = Rect((400,0), (200,200))
rect4 = Rect((0,200), (200,200))
rect5 = Rect((200,200), (200,200))
rect6 = Rect((400,200), (200,200))
rect7 = Rect((0,400), (200,200))
rect8 = Rect((200,400), (200,200))
rect9 = Rect((400,400), (200,200))

#Lista para acessar cada quadradinho criado a cima;
rec = [
    rect1,rect2,rect3,rect4,
    rect5,rect6,rect7,rect8,rect9,
]

def desenhar_tabu():
                            #COR          #ONDE
    pygame.draw.line(tela, (255,255,255),(200, 0), (200,600),10)
    pygame.draw.line(tela, (255,255,255),(400, 0), (400,600),10)
    pygame.draw.line(tela, (255,255,255),(0, 200), (600,200),10)
    pygame.draw.line(tela, (255,255,255),(0, 400), (600,400),10)

def desenhar_peca (posicao):
    global VEZ
    x, y = posicao
    if VEZ == 'JOGADOR2':
        pygame.draw.circle(tela, (0, 0, 255), posicao, 50)
    else:
        img = pygame.image.load('X.png').convert_alpha()
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))

def confirmar(indice, pos):            #confirma se ja existe algum desenho no quadradinho clicado.
    global ESCOLHA, VEZ, espaco
    if marca_tabu[indice] == 'X':
        print('x')
    elif marca_tabu[indice] == 'O':
        print('o')
    else:
        marca_tabu[indice] = ESCOLHA
        desenhar_peca(pos)
        print (marca_tabu)
        if VEZ == 'JOGADOR1':
            VEZ = 'JOGADOR2'
        else:
            VEZ = 'JOGADOR1'
        espaco += 1

def testa_posicao():
    for p in rec:
        if e.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_posicao):
            if p == rect1:
                confirmar(0,[100, 100])
            if p == rect2:
                confirmar(1, [300, 100])
            if p == rect3:
                confirmar(2,[500, 100])
            if p == rect4:
                confirmar(3, [100, 300])
            if p == rect5:
                confirmar(4, [300, 300])
            if p == rect6:
                confirmar(5, [500, 300])
            if p == rect7:
                confirmar(6, [100, 500])
            if p == rect8:
                confirmar(7, [300, 500])
            if p == rect9:
                confirmar(8, [500, 500])

def teste_vitoria(l):
        return ((marca_tabu [0] == l and marca_tabu[1] == l and marca_tabu[2] == l) or
            (marca_tabu[3] == l and marca_tabu[4] == l and marca_tabu[5] == l ) or
            (marca_tabu[6] == l and marca_tabu[7] == l and marca_tabu[8] == l ) or
            (marca_tabu[0] == l and marca_tabu[3] == l and marca_tabu[6] == l ) or
            (marca_tabu[1] == l and marca_tabu[4] == l and marca_tabu[7] == l ) or
            (marca_tabu[2] == l and marca_tabu[5] == l and marca_tabu[8] == l ) or
            (marca_tabu[0] == l and marca_tabu[4] == l and marca_tabu[8] == l ) or
            (marca_tabu[2] == l and marca_tabu[4] == l and marca_tabu[6] == l ))

def texto_vitoria(v):
    arial = pygame.font.SysFont('arial',50)
    mensagem = 'JOGADOR {} VENCEU!'.format(v)

    if v == 'EMPATE':
        mens_vitoria = arial.render('DEU VELHA', True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (115, 265))
    else:
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (0, 265))

# Controle do Jogo;
while True:
    mouse_posicao = pygame.mouse.get_pos()

    if ESTADO == 'JOGANDO':
        desenhar_tabu()
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                if VEZ == 'JOGADOR1':
                    ESCOLHA = 'X'
                    testa_posicao()
                else:
                    ESCOLHA = 'O'
                    testa_posicao()

        if teste_vitoria('X'):
            texto_vitoria('X')

        elif teste_vitoria('O'):
            texto_vitoria('O')

        elif espaco >= 9:
            texto_vitoria('EMPATE')

    pygame.display.flip()
