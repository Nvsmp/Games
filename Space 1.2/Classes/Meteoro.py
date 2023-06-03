import pygame
from pygame.locals import *
class Meteoro:
    def __init__(self,vetMeteoro,vetAceleraçao) -> None:
        self.__vetMeteoro = vetMeteoro
        self.__vetAceleracao = vetAceleraçao
        self.__speed = 2

    def getVet(self):
        return self.__vetMeteoro

    def getAceleracao(self):
        return self.__vetAceleracao
    
    def getSpeed(self):
        return self.__speed

    def setVet(self, vetorNovo):
        self.__vetMeteoro = vetorNovo
