import pygame
from pygame.locals import *
class Laser:
    def __init__(self, vetLaser,vetAceleracao, angulo,dano):
        self.__vetLaser = vetLaser
        self.__vetAceleracao = vetAceleracao
        self.__angulo = angulo
        self.__speed = 10
        self.__dano = dano

    def getAngulo(self):
        return self.__angulo

    def getSpeed(self):
        return self.__speed

    def getVetLaser(self):
        return self.__vetLaser

    def getVetAceleracao(self):
        return self.__vetAceleracao

    def setVetPos(self,vetPos):
        self.__vetLaser = vetPos

    def setVetAceleracao(self,vetA):
        self.__vetAceleracao = vetA

    def getDano(self)-> int:
        return self.__dano

    def upDano(self):
        self.__dano += 1
