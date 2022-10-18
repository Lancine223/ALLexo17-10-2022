class Table:
    def __init__(self, ref, mt, pd, ht, long, lg, pvt, prifab, nbstock):
        self.reference = ref
        self.matiere = mt
        self.poids = pd
        self.hauteur = ht
        self.longuere = long
        self.largere = lg
        self.prixvente = pvt
        self.__prixfab = prifab
        self.__nbstock = nbstock
    def getPrixfab():
        return self.__prixfab
    def getNbstock():
        return self.__nbstock
    def setPrixfab(self, prifab):
        return self.__prixfab
    def setNbstock(self, nbstock):
        return self.__nbstock
    def affiche(self):
        print("Référence est" ,self.reference , "\n la matière est le",self.matiere, ",\n le poids est de ",self.poids, "kg",
    ",\n la hauteur est " ,self.hauteur, "cm,\n la longueur est ",self.longuere,"cm,\n la largère est ",self.largere,"cm, \nle prix fabrique est",self.__prixfab,"F et le nombre de stock est",self.__nbstock)
    def calculer(self):
        print("\n le resultat de calcule nbstock est : ",self.__prixfab-self.__nbstock)
t1 = Table("Bko","Bank", 20, 10, 15, 28, 100, 200,10)

t1.affiche()
t1.calculer()

