#DEFINITION DE LA CLASSE
class Complex:

    #CONSTRUCTEUR
    def __init__(self,reel,imaginaire):
        self.__Re = reel
        self.__Im = imaginaire

    #GETTERS ET SETTERS
    def getRe(self):
        return self.__Re

    def setRe(self,reel):
        self.__Re = reel

    def getIm(self):
        return self.__Im

    def setIm(self,imaginaire):
        self.__Im = imaginaire

    #AUTRES METHODES
    def __add__(self, Nb2):
        return Complex(self.__Re + Nb2.getRe(), self.__Im + Nb2.getIm())

    def __sub__(self, Nb2):
        return Complex(self.__Re - Nb2.getRe(), self.__Im - Nb2.getIm())

    def __mul__(self, Nb2):
            return Complex(self.__Re * Nb2.getRe() - Nb2.getIm()*self.__Im, self.__Im * Nb2.getRe() + self.__Re*Nb2.getIm())

    def __truediv__(self, Nb2):
        Numerateur = self * Complex(Nb2.getRe(),Nb2.getIm())
        return Complex(Numerateur.getRe() * (Nb2.getRe()**2-Nb2.getIm()**2), Numerateur.getIm() * (Nb2.getRe()**2-Nb2.getIm()**2))

    def __abs__(self):
        return (self.__Re**2+self.__Im**2)**(1/2)

    def __eq__(self, Nb2):
        return self.__Re == Nb2.getRe() and self.__Im == Nb2.getIm()

    def __ne__(self, Nb2):
        return self.__Re != Nb2.getRe() and self.__Im != Nb2.getIm()

    def __str__(self):
        return "Re = "+str(self.__Re)+" , Im = "+str(self.__Im)

#PROGRAMME PRINCIPAL
if __name__== '__main__':
   c1 = Complex(2, 5)
   c2 = Complex(3, 7)
   print(c1)
   print(c2)
   c3 = c1 + c2
   print(c3)
   c4 = c1 - c2
   print(c4)
   c5 = c1 * c2
   print(c5)
   c6 = c1 / c2
   print(c6)
   c7 = abs(c1)
   print(c7)
   c8 = c1 == c2
   print(c8)
   c9 = c1 != c2
   print(c9)
