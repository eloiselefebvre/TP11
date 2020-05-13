#DEFINITION DE LA CLASSE
class Rational :

    #CONSTRUCTEUR
    def __init__(self,numerator,denominator) :
        self.__numerator = numerator
        self.__denominator = denominator

    #SETTERS ET GETTERS
    def setNumerator(self,numerator):
        self.__numerator = numerator

    def setDenominator(self,denominator):
        self.__denominator = denominator

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    #AUTRES METHODES
    def __add__(self,n2):
        if self.__denominator == n2.__denominator :
            return Rational(self.getNumerator()+n2.getNumerator(),self.getDenominator())
        else :
            c=n2.getDenominator()
            n2.__denominator = self.getDenominator()%n2.getDenominator()
            self.__denominator = c
            return Rational(self.getNumerator()+n2.getNumerator(),n2.getDenominator())

    def __sub__(self,n2):
        if self.__denominator == n2.__denominator :
            return Rational(self.getNumerator()-n2.getNumerator(),self.getDenominator())
        else :
            c=n2.__denominator
            n2.__denominator=self.__denominator%n2.__denominator
            self.__denominator=c
            return Rational(self.getNumerator()-n2.getNumerator(),n2.getDenominator())

    def __mul__(self,n2):
        return Rational(self.getNumerator()*n2.getNumerator(),self.getDenominator()*n2.getDenominator())

#PROGRAMME PRINCIPAL
if __name__ == '__main__' :

    n1 = Rational(4,2)
    n2 = Rational(2,8)
    print(n1 + n2)
    print(n1-n2)
    print(n1 * n2)


