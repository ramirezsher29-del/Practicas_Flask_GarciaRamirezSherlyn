#1.definimos la clase
class alumno:
    def __init__(self,nombre,edad,sexo):
        #definimos los atributos
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo

    #metodo de comportamiento
    def presentar(self):
        return f"{self.nombre} dice: ¡Jorge!"

    def materia(self):
        return f"{self.nombre} ¡filosofía!"

#2.creamos los objetos(instancia de la clase)
alumno1=alumno("jorge",16,"masculino")
alumno2=alumno("dana",15,"femenino")
alumno3=alumno("luis",16,"masculino")

#3.usar los objetos
print(alumno1.nombre)#accede al atributo nombre
print(alumno2.materia())#accede al metodo
print(alumno3.materia())