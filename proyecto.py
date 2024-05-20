import mysql.connector
import re

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.favorito = False

class Agenda:
    def __init__(self):
        self.contactos = []
        self.db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="ignacio",
            database="agenda_contactos"
        )
        self.cursor = self.db_connection.cursor()




    def mostrar_contactos(self):
        if self.contactos:
            for contacto in self.contactos:
                if contacto.favorito:
                    print(f"{contacto} (Favorito)")
                else:
                    print(contacto)
        else:
            print("No hay contactos en la agenda.")

    def buscar_contacto(self):
        self.mostrar_contactos()
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                encontrado = True
                if contacto.favorito:
                    print(f"{contacto} (Favorito)")
                else:
                    print(contacto)
        if not encontrado:
            print("Contacto no encontrado.")

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

    def cargar_agenda(self):
        query = "SELECT nombre, telefono, email, favorito FROM contactos"
        self.cursor.execute(query)
        for nombre, telefono, email, favorito in self.cursor.fetchall():
            contacto = Contacto(nombre, telefono, email)
            contacto.favorito = favorito
            self.contactos.append(contacto)

def menu():
    print("\n1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Editar contacto")
    print("6. Salir")

def main():
    agenda = Agenda()
    agenda.cargar_agenda()