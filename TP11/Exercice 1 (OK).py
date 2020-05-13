#DEFINITION DE LA CLASSE
class Cercle:

    #CONSTRUCTEUR
    def __init__(self, rayon):
        self.__rayon = rayon

    #GETTERS ET SETTERS
    def getRayon(self):
        return self.__rayon

    def setRayon(self,rayon):
        self.__rayon = rayon

    #AUTRES METHODES
    def __add__(self, c):
        return Cercle(self.__rayon + c.getRayon())

    def __lt__(self, c):
        return self.__rayon < c.getRayon()

    def __gt__(self, c):
        return self.__rayon > c.getRayon()

    def __str__(self):
        return "Rayon du cercle = "+str(self.__rayon)


#PROGRAMME PRINCIPAL
if __name__== '__main__':
   c1 = Cercle(2)
   c2 = Cercle(3)
   c3 = c1 + c2
   c4 = c1 < c2
   c5 = c2 > c3
   print(c1)
   print(c2)
   print(c3)
   print(c4)
   print(c5)
