print("Mejia_Suarez_Emmanuel_Alexander_1197_29/11/24_3W\n")

class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        """declarar datos"""
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        """imprimir datos"""
        mayor=max(self.lado1,self.lado2,self.lado3)
        print(f"Lado mayor:{mayor}")
    
    def tipo_triangulo(self):
        """determina y muestra el tipo de triangulo"""
        if self.lado1 == self.lado2 == self.lado3:
            print("El triangulo es equilatero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triangulo es isoseles")
        else:
            print("El triangulo es escaleno")

# Uso de la clase
triangulo1 = Triangulo(5,5,8)
triangulo1.lado_mayor()
triangulo1.tipo_triangulo()