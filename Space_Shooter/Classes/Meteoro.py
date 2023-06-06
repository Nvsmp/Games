import pygame
from pygame.locals import *
class Meteoro:
    def __init__(self,vetMeteoro,vetAceleraçao,vida) -> None:
        self.__vetMeteoro = vetMeteoro
        self.__vetAceleracao = vetAceleraçao
        self.__speed = 2
        self.__vida = vida
        self.__vidaTotal = vida

    def getVet(self):
        return self.__vetMeteoro

    def getAceleracao(self):
        return self.__vetAceleracao
    
    def getSpeed(self):
        return self.__speed

    def setVet(self, vetorNovo):
        self.__vetMeteoro = vetorNovo

    def getVida(self)-> int:
        return self.__vida

    def upVida(self):
        self.__vida += 1

    def getDano(self):
        return self.__dano

    def upDano(self):
        self.__dano += 1

    def getHited(self,dano:int):
        self.__vida -= dano

    def getVT(self):
        return  self.__vidaTotal