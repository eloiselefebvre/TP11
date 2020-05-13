import numpy as np

#DEFINTION DE LA CLASSE
class Matrice :

    #CONSTRUCTEUR
    def __init__(self,data):
        self.__data = data

    #SETTERS ET GETTERS
    def getData(self):
        return self.__data

    #AUTRES METHODES
    def __add__(self,data2):
        return Matrice(self.getData()+data2.getData())

    def __iadd__(self,data2):
        self.__data += data2
        return Matrice(self.getData())

    def __sub__(self,data2):
        return Matrice(self.getData()-data2.getData())

    def __isub__(self,data2):
        self.__data -= data2
        return Matrice(self.getData())

    def __mul__(self,data2):
        return Matrice(self.getData()*data2.getData())

    def __imul__(self,data2):
        self.__data *= data2
        return Matrice(self.getData())

    def __rlshift__(self,data2):
        return self.getData() << data2.getData()

    def __rrshift__(self,data2):
        return self.getData() >> data2.getData()

    def print(self):
        print(data)

    def __len__(self):
        print(len(data))

#PROGRAMME PRINCIPAL
if __name__ == '__main__' :
    data = np.array([[0,1],[2,4]])
    data2 = np.array([[3,1],[8,9]])
    print(data+data2)
    print(data-data2)
    print(data+data2)
    print(data*data2)
    print(data >> data2)
