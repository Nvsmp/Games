import pygame
import sys,os,time
from pygame.locals import *

pygame.init()

#Funcoes
#Deleta o tiro
def update_laser(laser_list):
    for laserRec in laser_list:
        laserRec.y -= round(speed*dt)
        if laserRec.midbottom[1] < 0:
            laser_list.remove(laserRec)
#Pontuacao
def display_score(tela, font):
    score_text = str(f'S T A R - G A M E {pygame.time.get_ticks()//1000}')
    texto = font.render(score_text, True, (255,255,255))
    recText = texto.get_rect(midleft=(30,15))
    tela.blit(texto, recText)

#Tela
pygame.display.set_caption('ACOBRINHA AKI')
largura, altura = 1280,720 #FULL HD
tela = pygame.display.set_mode((largura, altura))

#VARS
loop = True
r,g,b = 0,0,0
relogio = pygame.time.Clock()
velocidade = 50
speed = 300 #velocidade tiro
pos_y,pos_x  = altura / 2, largura /2

#MOVIMENTACAO WASD
mov_esquerda = False
mov_direita = False
mov_cima = False
mov_baixo = False

#Fonte
font = pygame.font.Font(os.path.join('assets','Font','Sigmar','Sigmar-Regular.ttf'),16)

#texto = font.render('S T A R - G A M E', True,(65,105,225))
#recText = texto.get_rect(center = (100,10))
#bgR1 = fundo.get_rect(center = ((largura/2,(altura/2))))

#Fundo
fundo = pygame.image.load(os.path.join('assets' ,'img','espaco.png')).convert_alpha()

#Nave
nave = pygame.image.load(os.path.join('assets' ,'img','ship.png')).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))

#Disparo da nave
lasersurf = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasersurf = pygame.transform.scale(lasersurf,(400,400))
laser_list = []

#?
naveRec = nave.get_rect(center = (500,500))
#laserRec = lasersurf.get_rect(midbottom=naveRec.midtop)


while(loop):

    dt = relogio.tick(120)/1000
    naveRec.center = pygame.mouse.get_pos()
    mousex ,mousey = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            laserRec = lasersurf.get_rect(midbottom=naveRec.midtop) #?
            laser_list.append(laserRec)

        if event.type == pygame.MOUSEBUTTONUP:
            print(f'Tiro em {event.pos}')

        if event.type == pygame.QUIT:
            loop = False
            sys.exit()

        #EVENTO MOVIMENTO (KEYDOWN e KEYUP) | n funciona enquanto posicao do naveRec.center seguir o mouse
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mov_esquerda = True
            if event.key == pygame.K_d:
                mov_direita = True
            if event.key == pygame.K_w:
                mov_cima = True
            if event.key == pygame.K_s:
                mov_baixo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mov_esquerda = False
            if event.key == pygame.K_d:
                mov_direita = False
            if event.key == pygame.K_w:
                mov_cima = False
            if event.key == pygame.K_s:
                mov_baixo = False
    if mov_esquerda:
        naveRec.x -= velocidade
    if mov_direita:
        naveRec.x += velocidade
    if mov_cima:
        naveRec.y -= velocidade
    if mov_baixo:
        naveRec.y += velocidade

    tela.blit(fundo, (0,0))
    tela.blit(nave, naveRec)
    #tela.blit(texto,bgR1)
    display_score(tela=tela, font=font)
    #laserRec.y -= velocidadeDisparo
    #tela.blit(lasersurf,laserRec)
    if naveRec.y <= 0:
        naveRec.y = altura - 20
    if naveRec.y >= altura:
        naveRec.y = 20
    if naveRec.x <= 0:
        naveRec.x = largura - 20
    if naveRec.x >= largura:
        naveRec.x = 0

    update_laser(laser_list)

    surfaceEscudo = pygame.Surface((200, 200), pygame.SRCALPHA)
    pygame.draw.circle(surfaceEscudo, (200, 200, 200, 100), (100, 100), 50)
    tela.blit(surfaceEscudo, (mousex -100, mousey - 100))
    #pygame.display.flip()
    #pygame.time.Clock().tick(60)

    for laserRec in laser_list:
        tela.blit(lasersurf,laserRec)
        print(laser_list)

    #start = int(round(time.time() * 1000))
    #end = int(round(time.time()*1000))    Pega o "ping" entre as cenas
    #print(f'{end-start} ms')

    pygame.display.update()
pygame.quit()