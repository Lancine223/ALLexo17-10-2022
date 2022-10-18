class Pet:
    def __init__(self):
        name = input("Veuillez entrer le nom de l'animal")
        animalType = input("Entre animal type")
        age = int(input("Veillez indiquer l'age de l'animal"))
        self.__name = name
        self.__animalType = animalType
        self.__age = age
    def getName(self):
        return self.__age
    def getAnimalType(self):
        return self.__animalType
    def getAge(self):
        return self.__age
    def setName(self, name):
            self.__name=name
    def setAnimalType(self, animalType):
        self.__animalType_animalType=animalType
    def setAge(self, age):
        self.__age=age
p1 = Pet()
print(p1.getName())
print(p1.getAnimalType())
print(p1.getAge())