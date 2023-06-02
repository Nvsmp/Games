class Meteoro:
    def __init__(self,vetMeteoro,vetAceleraçao) -> None:
        self.__vetMeteoro = vetMeteoro
        self.__vetAceleracao = vetAceleraçao
        self.__speed = 5

    def getVet(self):
        return self.__vetMeteoro

    def getAceleracao(self):
        return self.__vetAceleracao
    

