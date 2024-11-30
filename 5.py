print("Mejia_Suarez_Emmanuel_Alexander_1197_29/11/24_3W\n")

class Agenda:
    def __init__(self):
        """Inicializa la agenda como un diccionario vacío"""
        self.contactos = {}

    def añadir_contacto(self):
        """Añade un nuevo contacto a la agenda"""
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        self.contactos[nombre] = {"Teléfono": telefono, "Email": email}
        print("Contacto añadido")

    def listar_contactos(self):
        """Muestra todos los contactos en la agenda"""
        if self.contactos:
            for nombre, datos in self.contactos.items():
                print(f"{nombre} - Teléfono: {datos['Teléfono']}, Email: {datos['Email']}")
        else:
            print("No hay contactos en la agenda")

    def buscar_contacto(self):
        """Busca un contacto por nombre"""
        nombre = input("Nombre del contacto: ")
        if nombre in self.contactos:
            datos = self.contactos[nombre]
            print(f"{nombre} - Teléfono: {datos['Teléfono']}, Email: {datos['Email']}")
        else:
            print("Contacto no encontrado")

    def editar_contacto(self):
        """Edita un contacto existente"""
        nombre = input("Nombre del contacto a editar: ")
        if nombre in self.contactos:
            print("Deje en blanco los campos que no desee modificar")
            telefono = input("Nuevo teléfono: ")
            email = input("Nuevo email: ")
            if telefono:
                self.contactos[nombre]["Teléfono"] = telefono
            if email:
                self.contactos[nombre]["Email"] = email
            print("Contacto actualizado")
        else:
            print("Contacto no encontrado")

    def cerrar_agenda(self):
        """Cierra la agenda"""
        print("Cerrando agenda...")
        exit()

    def menu(self):
        """Muestra el menú de opciones"""
        while True:
            print("\n1. Añadir contacto\n2. Lista de contactos\n3. Buscar contacto\n4. Editar contacto\n5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                self.cerrar_agenda()
            else:
                print("Opción no válida")

# Uso de la clase
agenda = Agenda()
agenda.menu()