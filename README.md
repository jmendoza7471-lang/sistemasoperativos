

import os
import sqlite3

def conectar_bd():
    #  Credenciales hardcodeadas (problema de seguridad)
    usuario = "admin"
    password = "admin123"
    print("Usuario:", usuario)
    print("Password:", password)

def consultar_usuario(user_id):
    #  Vulnerabilidad: Inyección SQL
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    query = "SELECT * FROM usuarios WHERE id = " + user_id
    cursor.execute(query)

    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def dividir(a, b):
    #  Falta manejo de excepciones
    return a / b

def main():
    conectar_bd()

    #  Entrada sin validación
    user_id = input("Ingrese el ID del usuario: ")
    print(consultar_usuario(user_id))

    #  Posible error en tiempo de ejecución
    print(dividir(10, 0))

if __name__ == "__main__":
    main()




