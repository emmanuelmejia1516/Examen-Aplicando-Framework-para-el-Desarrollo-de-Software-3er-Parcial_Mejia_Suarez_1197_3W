print("Mejia_Suarez_Emmanuel_Alexander_1197_29/11/24_3W\n")

class Persona:
    def __init__(self, nombre, edad):
        """Declarar el nombre y la edad de la persona"""
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        """Muestra los datos de la persona"""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def es_mayor_de_edad(self):
        """Indica si la persona es mayor de edad"""
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

# Uso de la clase
persona1 = Persona("Ana", 22)
persona1.mostrar_datos()
persona1.es_mayor_de_edad()