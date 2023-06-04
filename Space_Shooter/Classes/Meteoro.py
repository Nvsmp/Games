import pygame
from pygame.locals import *
class Meteoro:
    def __init__(self,vetMeteoro,vetAceleraçao) -> None:
        self.__vetMeteoro = vetMeteoro
        self.__vetAceleracao = vetAceleraçao
        self.__speed = 2
        self.__vida = 1
        self.__dano = 1

    def getVet(self):
        return self.__vetMeteoro

    def getAceleracao(self):
        return self.__vetAceleracao
    
    def getSpeed(self):
        return self.__speed

    def setVet(self, vetorNovo):
        self.__vetMeteoro = vetorNovo

    def getVida(self):
        return self.__vida

    def upVida(self):
        self.__vida += 1

    def getDano(self):
        return self.__dano

    def upDano(self):
        self.__dano += 1
