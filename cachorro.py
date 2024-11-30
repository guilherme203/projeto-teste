from animal import Animal
class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte=porte
        
    def setPorte(self, porte):
        self.__porte=porte
    def getPorte(self):
        return self.__porte
    def mostrar(self):
        return (f"Cachorro: {self.getNome()}, Idade: {self.getIdade()} e Porte: {self.getPorte()}")
    
#c=Cachorro("Relampago", 5, "Grande")
#print(c.mostrar())