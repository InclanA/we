import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('sistema.db')
 
class Bibloteca:
    def __init__(self):
        self.__cursor = conn.cursor()
        self.Crear_Tabla()

    def Crear_Tabla(self):
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY AUTOINCREMENT,titulo TEXT NOT NULL, autor TEXT NOT NULL, cantidad TEXT)')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS calculadoras(id INTEGER PRIMARY KEY AUTOINCREMENT, modelo TEXT NOT NULL, marca TEXT NOT NULL, cantidad TEXT)')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS computadoras(id INTEGER PRIMARY KEY AUTOINCREMENT,modelo TEXT NOT NULL, marca TEXT NOT NULL, cantidad TEXT NOT NULL, cargadores TEXT)')

    def libros(self, titulo, autor, cantidad):
        self.__cursor.execute("INSERT INTO libros (titulo, autor, cantidad) VALUES (?, ?, ?)", (titulo, autor, cantidad))
        conn.commit()
        print(f"{titulo}  {autor} {cantidad}")

    def leer_libro(self):
        datos = self.__cursor.execute("SELECT * FROM libros").fetchall()
        return datos

    def LibrosActualizar(self, titulo, autor, cantidad, id):
        self.__cursor.execute("UPDATE libros SET titulo = ?, autor = ?, cantidad = ? WHERE id = ?", (titulo, autor, cantidad, id))
        conn.commit()

    def librosEliminar(self, id):
        self.__cursor.execute("DELETE FROM libros WHERE id = ?", (id,))
        conn.commit()

    def computadoras(self, modelo, marca, cantidad, cargadores):
        self.__cursor.execute("INSERT INTO computadoras (modelo, marca, cantidad, cargadores) VALUES (?, ?, ?, ?)", (modelo, marca, cantidad, cargadores))
        conn.commit()
        print(f"{modelo}  {marca} {cantidad} {cargadores}")

    def leer_computadoras(self):
        datos = self.__cursor.execute("SELECT * FROM computadoras").fetchall()
        return datos

    def CompuActualizar(self, modelo, marca, cantidad, cargadores, id):
        self.__cursor.execute("UPDATE computadoras SET modelo = ?, marca = ?, cantidad = ?, cargadores = ? WHERE id = ?", (modelo, marca, cantidad, cargadores, id))
        conn.commit()

    def CompuEliminar(self, id):
        self.__cursor.execute("DELETE FROM computadoras WHERE id = ?", (id,))
        conn.commit()

    def calculadoras(self, modelo, marca, cantidad):
        self.__cursor.execute("INSERT INTO calculadoras (modelo, marca, cantidad) VALUES (?, ?, ?)", (modelo, marca, cantidad))
        conn.commit()
        print(f"{modelo}  {marca} {cantidad}")

    def leer_Calculadoras(self):
        datos = self.__cursor.execute("SELECT * FROM calculadoras").fetchall()
        return datos

    def CalcuActualizar(self, modelo, marca, cantidad, id):
        self.__cursor.execute("UPDATE calculadoras SET modelo = ?, marca = ?, cantidad = ? WHERE id = ?", (modelo, marca, cantidad, id))
        conn.commit()

    def CalcuEliminar(self, id):
        self.__cursor.execute("DELETE FROM calculadoras WHERE id = ?", (id,))
        conn.commit()

bibloteca = Bibloteca()
bibloteca.libros("Rebelión en la granja", "George Orwell", 10)
bibloteca.calculadoras("cassio", "cassio", 30)
bibloteca.computadoras("g9", "noblex", 30, "30 cargadores")

print("Libro:")
print(tabulate(bibloteca.leer_libro(), headers=["ID", "Título", "Autor", "Cantidad"], tablefmt="grid"))

print("Calcul:")
print(tabulate(bibloteca.leer_Calculadoras(), headers=["ID", "Modelo", "Marca", "Cantidad"], tablefmt="grid"))

print("Compu:")
print(tabulate(bibloteca.leer_computadoras(), headers=["ID", "Modelo", "Marca", "Cantidad", "Cargadores"], tablefmt="grid"))

while True:
    print("opcion1:Crear info libro")
    print("opcion2:Crear info compu")
    print("opcion3:Crear info calcu")
    print("opcion4:Leer info libros")
    print("opcion5:Leer info calcu")
    print("opcion6:Leer info compu")
    print("opcion7:Actualizar info libros")
    print("opcion8:Actualizar info calcu")
    print("opcion9:Actualizar info compu")
    print("opcion10:Eliminar info libros")
    print("opcion11:Eliminar info calcu")
    print("opcion12:Eliminar info compu")
    print("opcion13:Salir")

    opcion = input("oe elige una opción :v : ")

    if opcion == "1":
        titulo = input("Título:")
        autor = input("Autor:")
        cantidad = int(input("Cantidad:"))
        bibloteca.libros(titulo, autor, cantidad)
    elif opcion == "2":
        modelo = input("Modelo:")
        marca = input("Marca:")
        cantidad = int(input("Cantidad:"))
        cargadores = int(input("Cargadores:"))
        bibloteca.computadoras(modelo, marca, cantidad, cargadores)
    elif opcion == "3":
        modelo = input("Modelo:")
        marca = input("Marca:")
        cantidad = int(input("Cantidad:"))
        bibloteca.calculadoras(modelo, marca, cantidad)
    elif opcion == "4":
        print(tabulate(bibloteca.leer_libro(), headers=["ID", "Título", "Autor", "Cantidad"], tablefmt="grid"))
    elif opcion == "5":
        print(tabulate(bibloteca.leer_Calculadoras(), headers=["ID", "Modelo", "Marca", "Cantidad"], tablefmt="grid"))
    elif opcion == "6":
        print(tabulate(bibloteca.leer_computadoras(), headers=["ID", "Modelo", "Marca", "Cantidad", "Cargadores"], tablefmt="grid"))
    elif opcion == "7":
        id = int(input(""))
        titulo = input("Nuevo título:")
        autor = input("Nuevo autor:")
        cantidad = int(input("Nueva cantidad:"))
        bibloteca.LibrosActualizar(titulo, autor, cantidad, id)
    elif opcion == "8":
        id = int(input(""))
        modelo = input("Nuevo modelo:")
        marca = input("Nueva marca:")
        cantidad = int(input("Nueva cantidad:"))
        bibloteca.CalcuActualizar(modelo, marca, cantidad, id)
    elif opcion == "9":
        id = int(input(""))
        modelo = input("Nuevo modelo:")
        marca = input("Nueva marca:")
        cantidad = int(input("Nueva cantidad:"))
        cargadores = int(input("Nuevo número de cargadores:"))
        bibloteca.CompuActualizar(modelo, marca, cantidad, cargadores, id)
    elif opcion == "10":
        id = int(input(""))
        bibloteca.librosEliminar(id)
    elif opcion == "11":
        id = int(input(""))
        bibloteca.CalcuEliminar(id)
    elif opcion == "12":
        id = int(input(""))
        bibloteca.CompuEliminar(id)
    elif opcion == "13":
        print("Saliste :v")
        break
    else:
        print("a")
