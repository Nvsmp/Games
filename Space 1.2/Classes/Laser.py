import pygame
from pygame.locals import *
class Laser:
    def __init__(self, vetLaser,vetAceleracao):
        self.__vetLaser = vetLaser
        self.__vetAceleracao = vetAceleracao
        self.__speed = 10

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
