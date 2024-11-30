print("Mejia_Suarez_Emmanuel_Alexander_1197_29/11/24_3W\n")

class Calculadora:
    def __init__(self):
        """solicitar dos valores enteros al usuario"""
        self.num1 = int(input("Ingrese el primer numero:"))
        self.num2 = int(input("Ingrese el segundo numero:"))

    def sumar(self):
        """Realiza la suma de los numeros"""
        print(f"Suma: {self.num1 + self.num2}")

    def restar(self):
        """Realiza la resta de los numeros"""
        print(f"Resta: {self.num1 - self.num2}")

    def multiplicar(self):
        """Realiza la multiplicacion de los numeros"""
        print(f"Multiplicacion: {self.num1 * self.num2}")
    
    def dividir(self):
        """Realiza la division de los numeros"""
        if self.num2 !=0:
            print(f"Division: {self.num1 / self.num2}")
        else:
            print("Division por cero no es permitido")

# Uso de la clase
calc = Calculadora()
calc.sumar()
calc.restar()
calc.multiplicar()
calc.dividir()