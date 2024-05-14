

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.favorito = False



    def eliminar_contacto(self):
        self.mostrar_contactos()
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                encontrado = True
                self.contactos.remove(contacto)
                print(f"El contacto {nombre} ha sido eliminado.")
                self.eliminar_contacto_db(nombre)
                break
        if not encontrado:
            print("Contacto no encontrado.")

    def editar_contacto(self):
        self.mostrar_contactos()
        nombre = input("Ingrese el nombre del contacto que desea editar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                encontrado = True
                print("Editar contacto:")
                nuevo_nombre = input(f"Nuevo nombre ({contacto.nombre}): ") or contacto.nombre
                nuevo_telefono = input(f"Nuevo teléfono ({contacto.telefono}): ") or contacto.telefono
                nuevo_email = input(f"Nuevo email ({contacto.email}): ") or contacto.email
                favorito = input("¿Desea marcar el contacto como favorito? (s/n): ").lower()

                contacto.nombre = nuevo_nombre
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                if favorito == "s":
                    contacto.favorito = True
                elif favorito == "n":
                    contacto.favorito = False
                print("Contacto actualizado correctamente.")
                self.editar_contacto_db(contacto)
                break
        if not encontrado:
            print("Contacto no encontrado.")

