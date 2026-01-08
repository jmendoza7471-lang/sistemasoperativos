# CLASE BASE - Trabajador (Padre)
class Trabajador:
    def __init__(self, nombre, cargo, salario_base):
        # Atributos generales para todos los trabajadores
        self.nombre = nombre
        self.cargo = cargo
        self.salario_base = salario_base
    
    def trabajar(self):
        # Método base que será sobrescrito por las clases hijas
        return f"{self.nombre} está realizando tareas generales"

# CLASE HIJA - IngenieroCivil (Hereda de Trabajador)
class IngenieroCivil(Trabajador):
    def __init__(self, nombre, salario_base):
        # Llama al constructor de la clase padre
        super().__init__(nombre, "Ingeniero Civil", salario_base)
    
    def trabajar(self):
        # Sobrescribe el método trabajar() con comportamiento específico
        return f"{self.nombre} diseña estructuras y supervisa cálculos estructurales"

# CLASE HIJA - Arquitecto (Hereda de Trabajador)
class Arquitecto(Trabajador):
    def __init__(self, nombre, salario_base):
        # Llama al constructor de la clase padre
        super().__init__(nombre, "Arquitecto", salario_base)
    
    def trabajar(self):
        # Sobrescribe el método trabajar() con comportamiento específico
        return f"{self.nombre} crea planos y diseños arquitectónicos"

# CLASE HIJA - Obrero (Hereda de Trabajador)
class Obrero(Trabajador):
    def __init__(self, nombre, salario_base):
        # Llama al constructor de la clase padre
        super().__init__(nombre, "Obrero", salario_base)
    
    def trabajar(self):
        # Sobrescribe el método trabajar() con comportamiento específico
        return f"{self.nombre} ejecuta trabajos físicos en la obra"

# CLASE PARA GESTIONAR PROYECTOS
class ProyectoConstruccion:
    def __init__(self, nombre):
        self.nombre = nombre
        # Lista que almacenará diferentes tipos de trabajadores
        self.trabajadores = []
    
    def agregar_trabajador(self, trabajador):
        # Agrega cualquier tipo de trabajador a la lista
        self.trabajadores.append(trabajador)
        print(f" {trabajador.nombre} agregado al proyecto")
    
    def mostrar_equipo(self):
        # Muestra información básica del equipo
        print(f"\n EQUIPO DEL PROYECTO: {self.nombre}")
        for trabajador in self.trabajadores:
            print(f"- {trabajador.cargo}: {trabajador.nombre}")
    
    def simular_trabajo(self):
        print(f"\n INICIANDO TRABAJO EN {self.nombre}:")
        for trabajador in self.trabajadores:
            # POLIMORFISMO: mismo método, diferentes comportamientos
            print(f"• {trabajador.trabajar()}")

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Crear un proyecto de construcción
    proyecto = ProyectoConstruccion("Edificio Central")
    
    # Crear diferentes tipos de trabajadores
    # Cada uno es una instancia de una clase diferente
    ingeniero = IngenieroCivil("Ana García", 5000)
    arquitecto = Arquitecto("Carlos López", 4500)
    obrero = Obrero("Pedro Martínez", 1500)
    
    # Agregar trabajadores al proyecto
    # Todos son tratados como objetos Trabajador
    proyecto.agregar_trabajador(ingeniero)
    proyecto.agregar_trabajador(arquitecto)
    proyecto.agregar_trabajador(obrero)
    
    # Mostrar información del equipo
    proyecto.mostrar_equipo()
    
    # Demostrar polimorfismo: mismo método, diferentes resultados
    proyecto.simular_trabajo()