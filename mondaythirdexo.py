class Personne:
    def __init__(self, nom, prenom, cin):
        self.nom = nom
        self.prenom = prenom
        self.cin = cin
    def Tostring(self):
        print("----Personne-----")
        print ("Nom: ",self.prenom,"\n Prénom: ",self.prenom,"\nCin : ",self.cin)
p1 = Personne("TOURE", "ALI", "B312")
class Vaccine(Personne):
    def __init__(self, nom, prenom, cin, code, date):
        super().__init__(nom, prenom, cin)
        self.__code = code
        self.__date = date
    def getCode(self):
        return self.__code
    def getDate(self):
        return self.__date
    def setCode(self, code):
        self.__code = code
    def setDate(self, date):
        self.__date = date
    def Tostring(self):
        print("-----VACCINE-----")
        print(super().Tostring(),"Code Vaccination: ",self.__code,"\n Date Vaccination:",self.__date)
v2 = Vaccine("Pierre","Jean","Noval", 23, "Le 10/10/2022" )
class   Vaccin(Personne):
    def __init__(self, nom, prenom, cin, codevaccin, nomvaccin, dureevaccin ):
        super().__init__(nom, prenom, cin)
        self.__codevaccin = codevaccin
        self.__nomvaccin = nomvaccin
        self.__dureevaccin = dureevaccin
    def Tostring(self):
        print("\n-----Vaccin-----")
        print(super().Tostring(),"\n Code vaccin: ",self.__codevaccin,"\n Nom vaccin: ",self.__nomvaccin,"\n Durée est",self.__dureevaccin)
v3 = Vaccin("harry","poudiougou","B220", 24,"B320", "24h")

p1.Tostring()
v2.Tostring()
v3.Tostring()