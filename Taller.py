#1)
lista1 = ["manzana", "banana", "cereza", "mango", "uva"]
lista2 = [10, 20, 30, 40, 50]

lista_unida = lista1 + lista2

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista Unida: {lista_unida}")


#---------------------------------------------------------------------
#2)
tupla_datos = ("rojo", "verde", "azul", "amarillo", "blanco")

print(f"Tupla de Datos: {tupla_datos}")
print(f"Cantidad de elementos de la tupla: {len(tupla_datos)}")


#---------------------------------------------------------------
#3)
conjunto1 = {1, 2, 3, 4, 5, 6}
conjunto2 = {4, 5, 6, 7, 8, 9}

interseccion = conjunto1.intersection(conjunto2)

print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")
print(f"Intersección: {interseccion}")

#------------------------------------------------------------------
#4)
diccionario_persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Chone",
    "profesion": "Ingeniero",
    "estatura": 1.75
}

print(f"Diccionario: {diccionario_persona}") 

#--------------------------------------------------------------------
#5)
diccionario_persona["pais"] = "España"

print(f"Diccionario actualizado: {diccionario_persona}")
print("\nLa estructura de datos que **NO acepta elementos duplicados** es el **Conjunto (Set)**.")
print("Cuando intentas añadir un elemento ya existente a un conjunto, este simplemente ignora el nuevo elemento.")

#--------------------------------------------------------------------------------------
#6)
nombre_ingresado = input("Por favor, ingresa tu nombre: ")

edad_ingresada = float(input("Por favor, ingresa tu edad : "))

print("\n--- Datos Ingresados ---")
print(f"Mi nombre es: {nombre_ingresado}")
print(f"Mi edad es: {edad_ingresada} años")

#---------------------------------------------------------------------------------------------
#7)
class Vehiculo:
    
    def __init__(self, marca, modelo, color, placa):
        self.marca = marca     
        self.modelo = modelo    
        self.color = color      
        self.placa = placa      

    
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Placa: {self.placa}")

mi_coche = Vehiculo("Ford", "Fiesta", "Rojo", "XYZ-789")

print("\n--- Objeto de la Clase Vehiculo ---")
mi_coche.mostrar_info()