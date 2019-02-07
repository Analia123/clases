class persona:
    #nombre, edad, profesion 
    def __init__(self,un_nombre,una_edad,una_profesion):
        self.edad= una_edad
        self.nombre=un_nombre
        self.profesion=una_profesion
        print("Hola, yo me llamo", self.nombre,"tengo",self.edad,"anhos y soy",self.profesion)
    def cumpleanhos(self):
        self.edad= self.edad + 1
        print("Barbie cumplira", self.edad)

#personita=persona("Beatriz", 26 ,"programadora")
personita2=persona("Barbie",32,"de todo")



#Agregar un metodo a la clase persona que se llame cumpleanhos 
#y que aumente la edad de la persona en un anho y retorne la edad nueva 



personita2=persona("barbie", 32, "profesora")



