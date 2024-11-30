print("Mejia_Suarez_Emmanuel_Alexander_1197_29/11/24_3W\n")

class Alumno:
    def __init__(self, nombre, nota):
        """Declara el nombre y la nota del alumno"""
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        """Imprime el nombre y la nota del alumno"""
        print(f"Alumno: {self.nombre}, Nota: {self.nota}")

    def resultado(self):
        """Muestra si el alumno ha aprobado o no"""
        if self.nota >= 6:
            print("Resultado: Aprobado")
        else:
            print("Resultado: Reprobado")

# Uso de la clase
alumno1 = Alumno("Juan", 7)
alumno1.imprimir_datos()
alumno1.resultado()