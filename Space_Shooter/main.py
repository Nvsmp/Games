import pygame,sys,os,time,random
from pygame.locals import *
from Classes import Laser, Meteoro

pygame.init()

#Funcoes
#Deleta o tiro
def update_L(laser_list):
    for lasers in laser_list:
        velocidade = lasers.getVetAceleracao() * laser.getSpeed()
        pos = lasers.getVetLaser() + velocidade
        lasers.setVetPos(pos)
        if lasers.getVetLaser().x < 0 or lasers.getVetLaser().x > largura or lasers.getVetLaser().y < 0 or lasers.getVetLaser().y > altura:
            laser_list.remove(lasers)

def limpaCometas(meteoro_list, laser_list):
    for m in meteoro_list:
        rectM = pygame.Rect(m.getVet().x + 40, m.getVet().y + 30, larguraM - 50, alturaM - 40)
        for l in laser_list:
            rectL = pygame.Rect(l.getVetLaser().x, l.getVetLaser().y, larguraN, alturaN)
            if rectL.colliderect(rectM):
                m.getHited(l.getDano())
                if m.getVida() <= 0:
                    meteoro_list.remove(m)
                laser_list.remove(l)
                continue
        if m.getVet().x > largura + larguraM or m.getVet().x < 0 - larguraM or m.getVet().y > altura + alturaM or m.getVet().y < 0 - alturaM:
            meteoro_list.remove(m)
            continue
def update_M(meteoro_list):
    for meteoros in meteoro_list:
        aM = meteoros.getAceleracao() * meteoros.getSpeed()
        vetM = meteoros.getVet() + aM
        meteoros.setVet(vetM)
#Pontuacao
def display_score(tela, font, vidaNave, tvn):
    textoTempo = str(f'TEMPO: {pygame.time.get_ticks()//1000} | TEMPO DE ATUALIZACAO : {tempoA}')
    textoTempo = font.render(textoTempo, True, (255,255,255))
    recTextTempo = textoTempo.get_rect(midleft=(30, 15))
    textVida = str(f"VIDA NAVE : {vidaNave}/{tvn}")
    textVida = font.render(textVida, True, (255,255,255))
    rectTextoVida = textVida.get_rect(midleft=(30,35))
    tela.blit(textoTempo, recTextTempo)
    tela.blit(textVida,rectTextoVida)
#Tela
pygame.display.set_caption('Space Shooter')
largura, altura = 1280,720 #FULL HD
tela = pygame.display.set_mode((largura, altura))

#VARS
r,g,b = 0,0,0
relogio = pygame.time.Clock()
velocidade = 5
speed = 300 #velocidade tiro
pos_y,pos_x  = altura / 2, largura /2
tempoA = 0

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
larguraN = 40
alturaN = 40
scaleNave = (larguraN, alturaN)
nave = pygame.transform.scale(nave, scaleNave)
vidaN = 15
totalVidaN = vidaN

#Disparo da nave
lasersurf = pygame.image.load(os.path.join("assets", "img", "laser.png")).convert_alpha()
wLaser = 5
hLaser = 10
lasersurf = pygame.transform.scale(lasersurf, (wLaser, hLaser))
laser_list = []

#Meteoro
meteoro = pygame.image.load(os.path.join("assets", "img", "meteor.png")).convert_alpha()
larguraM = 120
alturaM = 120
meteoro = pygame.transform.scale(meteoro, (larguraM, alturaM))
meteoro_list = []
posMx = 200
posMy = 200
vidaM = 1

#timerSpawnMeteoro
spawnMeteoro = pygame.USEREVENT + 1
print(f"USER EVENT 1 : {spawnMeteoro}")
tempoSpawn = 500
pygame.time.set_timer(spawnMeteoro,tempoSpawn)

#timerDificuldade
subirDificuldade = pygame.USEREVENT + 2
print(f"USER EVENT 2 : {subirDificuldade}")
tempoSubirD = 30000
pygame.time.set_timer(subirDificuldade, tempoSubirD)

#Escudo
surfaceEscudo = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(surfaceEscudo, (200, 200, 200, 50), (100, 100), 40)

#?
naveRec = nave.get_rect(center=(largura / 2, altura / 2)) #Define o rect padrao no meio da tela
#meteoroRec = meteoro.get_rect(topleft=(200,200))
while vidaN > 0:
    start = int(round(time.time() * 1000)) #START PARA PEGAR O DELAY
    tela.blit(fundo, (0, 0))
    dt = relogio.tick(120)/1000
    mousex, mousey = pygame.mouse.get_pos()
    vetorMouse = pygame.math.Vector2(mousex, mousey)
    vetorNave = pygame.math.Vector2(naveRec.x + 25, naveRec.y + 25)
    vtNaveMouse = vetorMouse - vetorNave
    angulo = -vtNaveMouse.angle_to(pygame.math.Vector2(0, 0)) #??
    correcaoAngulo = - 93
    angulo = angulo - correcaoAngulo
    naveRot = pygame.transform.rotate(nave, -angulo)
    naveRecRot = naveRot.get_rect(center=naveRec.center)
    sombraRetNaveRot = naveRecRot
    centerRectNave = naveRec.centerx + 8,naveRec.centery + 7

    #EVENTOS
    for event in pygame.event.get():
        #TIRO
        if event.type == pygame.MOUSEBUTTONDOWN:
            vetorAceleracao = vetorMouse - pygame.math.Vector2(centerRectNave)
            vetorNormalizado = vetorAceleracao.normalize()
            laser = Laser(pygame.math.Vector2(centerRectNave), vetorNormalizado, angulo)
            laser_list.append(laser)
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        #QUITAR
        if event.type == pygame.QUIT:
            loop = False
            sys.exit()
        #MOVIMENTO NAVE(KEYDOWN e KEYUP)
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
        #SPAWN METEORO
        if event.type == spawnMeteoro:
            randX = random.randrange(0 - larguraM ,largura + larguraM )
            randY = random.randrange(0 - alturaM ,altura + alturaM )
            while( randX > 0 and randX < largura):
                randX = random.randrange(0 - larguraM * 2, largura + larguraM * 2)
            while(randY > 0 and randY < altura):
                randY = random.randrange(0 - alturaM * 2, altura + alturaM * 2)
            vetorMeteoroA = pygame.math.Vector2(centerRectNave) - pygame.math.Vector2(randX,randY)
            vetorMeteoroA = vetorMeteoroA.normalize()
            vetorMeteoro = pygame.math.Vector2(randX,randY)
            #print(f"EVENTO randX: {randX}  randY: {randY}  vetorMeteoroA: {vetorMeteoroA}  vetorMeteoro: {vetorMeteoro}")
            meteoroT = Meteoro(vetorMeteoro,vetorMeteoroA,vidaM)
            meteoro_list.append(meteoroT)
        if event.type == subirDificuldade:
            vidaM += 1
            #FIM DOS EVENTOS
    #ATUALIZA POSICAO NAVE
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
    #PONTUACAO
    display_score(tela=tela, font=font, vidaNave=vidaN, tvn=totalVidaN)

    #Nao permite que a nave saia da tela // calibrar
    if naveRec.y <= 0:
        naveRec.y = altura - 20
    if naveRec.y >= altura:
        naveRec.y = 20
    if naveRec.x <= 0:
        naveRec.x = largura - 20
    if naveRec.x >= largura:
        naveRec.x = 0

    tela.blit(surfaceEscudo, (navex - 70, navey - 70))   #BLITA ESCUDO
    #BLITA LASER
    for laser in laser_list:
        laserRot = pygame.transform.rotate(lasersurf, -laser.getAngulo())
        tela.blit(laserRot,laser.getVetLaser() )
        #print(f"Lista: {laser_list}")

    tela.blit(naveRot, (naveRecRot.x + 10, naveRecRot.y + 10))  # BLITA NAVE - TEM QUE SER DEPOIS DO LASER

    for meteoros in meteoro_list: #BLITA METEORO
        tela.blit(meteoro, meteoros.getVet())
        rectHBn = pygame.Rect(naveRec.x + 13, naveRec.y + 13, scaleNave[0] - 5, scaleNave[1] - 5)  #Hitbox nave
        rectHBm = pygame.Rect(meteoros.getVet().x + 6,meteoros.getVet().y + 6,larguraM - 12,alturaM - 12)


        textVidaM = str(f'{str(meteoros.getVida())}')
        textoVidaM = font.render(textVidaM, True, (255, 100, 100))
        rectTextoVidaM = textoVidaM.get_rect(midleft=(meteoros.getVet().x + (larguraM/2) , meteoros.getVet().y + alturaM))
        tela.blit(textoVidaM,rectTextoVidaM)

        if rectHBm.colliderect(rectHBn):
            vidaN -= meteoros.getDano()
            meteoro_list.remove(meteoros)
            continue
        #pygame.draw.rect(tela, (200,200,200), rectHBm)
        #pygame.draw.rect(tela, (200, 200, 200), rectHBn)

    update_L(laser_list) #ATUALIZA LASER
    update_M(meteoro_list) #ATUALIZA METEORO
    limpaCometas(meteoro_list, laser_list)
    # Pega o "ping" entre as cenas
    end = int(round(time.time()*1000))
    tempoA = end-start
    pygame.display.update()

pygame.quit()