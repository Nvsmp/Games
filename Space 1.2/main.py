import pygame
import sys,os,time
from pygame.locals import *
from Classes import Laser, Meteoro
pygame.init()

#Funcoes
#Deleta o tiro
def update_laser(laser_list):
    for laser in laser_list:
        velocidade = laser.getVetAceleracao() * laser.getSpeed()
        pos = laser.getVetLaser() + velocidade
        laser.setVetPos(pos)
        if laser.getVetLaser().x < 0 or laser.getVetLaser().x > largura or laser.getVetLaser().y < 0 or laser.getVetLaser().y > altura:
            laser_list.remove(laser)
#Pontuacao
def display_score(tela, font):
    score_text = str(f'S T A R - G A M E {pygame.time.get_ticks()//1000}')
    texto = font.render(score_text, True, (255,255,255))
    recText = texto.get_rect(midleft=(30,15))
    tela.blit(texto, recText)

def spawnMeteoro():
    tela.fill((255,255,255))

#Tela
pygame.display.set_caption('Space Shooter')
largura, altura = 1280,720 #FULL HD
tela = pygame.display.set_mode((largura, altura))

#VARS
loop = True
r,g,b = 0,0,0
relogio = pygame.time.Clock()
velocidade = 10
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
fundo = pygame.image.load(os.path.join('assets', 'img', 'espaco.png')).convert_alpha()

#Nave
nave = pygame.image.load(os.path.join('assets', 'img', 'ship.png')).convert_alpha()
scaleNave = (40, 40)
nave = pygame.transform.scale(nave, scaleNave)

#Disparo da nave
lasersurf = pygame.image.load(os.path.join("assets", "img", "laser.png")).convert_alpha()
wLaser = 20
hLaser = 20
lasersurf = pygame.transform.scale(lasersurf, (wLaser, hLaser))
laser_list = []

#Meteoro
meteoro = pygame.image.load(os.path.join("assets", "img", "meteor.png")).convert_alpha()
larguraM = 50
alturaM = 50
meteoro = pygame.transform.scale(meteoro, (larguraM, alturaM))
meteoro_list = []
posMx = 200
posMy = 200
meteoroB = True

#timerSpawnMeteoro
spawnMeteoro = pygame.USEREVENT + 1
pygame.time.set_timer(spawnMeteoro,5000)

#Escudo
surfaceEscudo = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(surfaceEscudo, (200, 200, 200, 50), (100, 100), 40)

#?
naveRec = nave.get_rect(center=(largura / 2, altura / 2)) #Define o rect padrao no meio da tela
#meteoroRec = meteoro.get_rect(topleft=(200,200))
while(loop):
    tela.blit(fundo, (0, 0))
    dt = relogio.tick(120)/1000
    mousex, mousey = pygame.mouse.get_pos()
    vetorMouse = pygame.math.Vector2(mousex, mousey)
    vetorNave = pygame.math.Vector2(naveRec.x, naveRec.y)
    vtNaveMouse = vetorMouse - vetorNave
    angulo = -vtNaveMouse.angle_to(pygame.math.Vector2(0, 0)) #??
    correcaoAngulo = -90
    angulo = angulo - correcaoAngulo
    naveRot = pygame.transform.rotate(nave, -angulo)
    naveRecRot = naveRot.get_rect(center=naveRec.center)
    sombraRetNaveRot = naveRecRot
    centerRectNave = naveRec.center

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            vetorAceleracao = vetorMouse - pygame.math.Vector2(centerRectNave)
            vetorNormalizado = vetorAceleracao.normalize()
            #offset = pygame.math.Vector2(naveRecRot.width / 2, 0).rotate(-vetorNormalizado.as_polar()[1])
            laser = Laser(pygame.math.Vector2(centerRectNave), vetorNormalizado, angulo)
            laser_list.append(laser)
        if event.type == pygame.MOUSEBUTTONUP:
            pass
            #print(f'Tiro em {event.pos}')

        if event.type == pygame.QUIT:
            loop = False
            sys.exit()
        #EVENTO MOVIMENTO (KEYDOWN e KEYUP)
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
        if event.type == spawnMeteoro:
            pass
    if mov_esquerda:
        naveRec.x -= velocidade
    if mov_direita:
        naveRec.x += velocidade
    if mov_cima:
        naveRec.y -= velocidade
    if mov_baixo:
        naveRec.y += velocidade

    navex = naveRec.x
    navey = naveRec.y
    display_score(tela=tela, font=font)

    #Nao permite que a nave saia da tela // calibrar
    if naveRec.y <= 0:
        naveRec.y = altura - 20
    if naveRec.y >= altura:
        naveRec.y = 20
    if naveRec.x <= 0:
        naveRec.x = largura - 20
    if naveRec.x >= largura:
        naveRec.x = 0

    tela.blit(surfaceEscudo, (navex - 70, navey - 70))

    #pygame.display.flip()
    #pygame.time.Clock().tick(60)

    for laser in laser_list:
        rectTiroAtual = pygame.Rect(laser.getVetLaser().x,laser.getVetLaser().y,wLaser,hLaser)
        laserRot = pygame.transform.rotate(lasersurf, -laser.getAngulo())
        #rectTiroAtual = pygame.transform.rotate(rectTiroAtual, -laser.getAngulo())
        pygame.draw.rect(tela,(255,0,0),rectTiroAtual)
        tela.blit(laserRot,laser.getVetLaser() )
        if rectTiroAtual.colliderect(rectHBm):
            meteoroB = False
            laser_list.remove(laser)
        #print(f"Lista: {laser_list}")
    update_laser(laser_list)

    tela.blit(naveRot, (naveRecRot.x + 10, naveRecRot.y + 10))

    #Hitbox nave
    rectHBn = pygame.Rect(naveRec.x + 10, naveRec.y + 10, scaleNave[0], scaleNave[1])
    #pygame.draw.rect(tela, (200,200,200), rectHBn)


    #Hitbox Meteoro
    rectHBm = pygame.Rect(posMx, posMy, larguraM, alturaM)
    pygame.draw.rect(tela, (200,200,200), rectHBm)
    if meteoroB:
        tela.blit(meteoro,(posMx,posMy))

    # start = int(round(time.time() * 1000))
    # end = int(round(time.time()*1000))    Pega o "ping" entre as cenas
    # print(f'{end-start} ms')
    pygame.display.update()

pygame.quit()