#DEFINITION DE LA CLASSE
class Duree :

    #CONSTRUCTEUR
    def __init__(self,heure,minute,seconde):
        self.__h = heure
        self.__m = minute
        self.__s = seconde

    #SETTERS ET GETTERS
    def getH(self):
        return self.__h

    def getM(self):
        return self.__m

    def getS(self):
        return self.__s

    #AUTRES METHODES
    def affichage(self):
        print(self.__h,'h',self.__m,'m',self.__s,'s')

    def __add__(self,d2):
        Heure = self.getH() + d2.getH()
        Minute = self.getM() + d2.getM()
        Seconde = self.getS() + d2.getS()
        if Minute >= 60 :
            Heure +=1
            Minute -= 60
        else :
            pass

        if Seconde >= 60 :
            Minute += 1
            Seconde -= 60
        else :
            pass

#PROGRAMME PRINCIPAL
n1 = Duree (3,3,18)
n2 = Duree (2,43,50)
n2.affichage()
print(n1+n2)
