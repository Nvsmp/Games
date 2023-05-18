import pygame
import sys,os,time

pygame.init()

largura, altura = 1280,720
pos_y,pos_x  = altura / 2, largura /2

tela = pygame.display.set_mode((largura, altura))



font = pygame.font.Font(os.path.join('assets','Font','Sigmar','Sigmar-Regular.ttf'),16)
texto = font.render('S T A R - G A M E', True,(65,105,225))
recText = texto.get_rect(center = (100,10))
fundo = pygame.image.load(os.path.join('assets' ,'img','espaco.png')).convert_alpha()

bgR1 = fundo.get_rect(center = ((largura/2,(altura/2))))

nave = pygame.image.load(os.path.join('assets' ,'img','ship.png')).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))

naveRec = nave.get_rect(center = (500,500))

pygame.display.set_caption('<- A COBRINHA AKI Q FOFA')
loop = True
r,g,b = 0,0,0
relogio = pygame.time.Clock()
velocidade = 50
mov_esquerda = False
mov_direita = False
mov_cima = False
mov_baixo = False

while(loop):
    relogio.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            print(f'Tiro em {event.pos}')

        if event.type == pygame.QUIT:
            loop = False
            sys.exit()
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


    start = int(round(time.time()*1000))
    tela.blit(fundo, (0,0))
    tela.blit(nave, naveRec)
    tela.blit(texto,bgR1)

    
    naveRec.y -= 10

    if naveRec.y <= 0:
        naveRec.y = altura - 20
    if naveRec.y >= altura:
        naveRec.y = 20
    if naveRec.x <= 0:
        naveRec.x = largura - 20
    if naveRec.x >= largura:
        naveRec.x = 0


    pygame.display.update()
    end = int(round(time.time()*1000))
    
    #print(f'{end-start} ms')
    relogio.tick(30)


pygame.quit()