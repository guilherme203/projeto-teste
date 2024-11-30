from animal import Animal
class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca=raca
    def setRaca(self, raca):
        self.__raca=raca
    def getRaca(self):
        return self.__raca
    def mostrar(self):
        return (f"Gato: {self.getNome()}, Idade: {self.getIdade()}, Raca: {self.getRaca()}")
    
#g=Gato("Romeu", 5, "Siames")
#print(g.mostrar())