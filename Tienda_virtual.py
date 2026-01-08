class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al carrito.")

    def calcular_total(self):
        return sum(p.precio for p in self.productos)

    def mostrar(self):
        if not self.productos:
            print("El carrito está vacío.")
            return
        print("\n--- PRODUCTOS EN EL CARRITO ---")
        for p in self.productos:
            print(f"- {p.nombre}: ${p.precio}")
        print(f"Total sin descuento: ${self.calcular_total()}")


class Cliente:
    def __init__(self, cedula):
        self.cedula = cedula
        self.compras_realizadas = 0
        self.frecuente = False

    def registrar_compra(self):
        self.compras_realizadas += 1
        if self.compras_realizadas >= 3:  
            self.frecuente = True



def validar_cedula(cedula):
    return len(cedula) == 10 and cedula.isdigit()



clientes = {}

print(" REGISTRO DE CLIENTE ")
cedula = input("Ingrese su número de cédula: ")

while not validar_cedula(cedula):
    print("Cédula incorrecta. Intente nuevamente.")
    cedula = input("Ingrese su número de cédula: ")


cliente = clientes.get(cedula, Cliente(cedula))
clientes[cedula] = cliente

print("Cliente registrado.\n")

carrito = Carrito()

while True:
    print("\n MENÚ DE COMPRA ")
    print("1. Agregar producto")
    print("2. Ver carrito")
    print("3. Pagar")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio del producto: "))
            producto = Producto(nombre, precio)
            carrito.agregar(producto)
        except ValueError:
            print("Precio inválido.")

    elif opcion == "2":
        carrito.mostrar()

    elif opcion == "3":
        total = carrito.calcular_total()

        if cliente.frecuente:
            print("\nCliente frecuente detectado. Descuento aplicado.")
            descuento = total * 0.15  
            total -= descuento
            print(f"Descuento: ${descuento}")

        print(f"\nTotal a pagar: ${total}")
        print("Compra realizada con éxito.")

        cliente.registrar_compra()
        print(f"Compras realizadas: {cliente.compras_realizadas}")
        print(f"Cliente frecuente: {'Sí' if cliente.frecuente else 'No'}")

        carrito = Carrito()  
        print("\nCarrito vacío. Puede continuar comprando.")

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
