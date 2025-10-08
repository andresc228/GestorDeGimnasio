from dataclasses import dataclass, field
from datetime import date
from typing import List
import random



@dataclass
class Usuario:
    nombre_completo: str
    documento_identidad: str


@dataclass
class Cliente(Usuario):
    edad: int
    objetivo_entrenamiento: str
    estado_fisico_inicial: str
    rutinas: List["RutinaEjercicio"] = field(default_factory=list)
    plan_alimentacion: "PlanAlimentacion" = None
    progreso: List["ProgresoFisico"] = field(default_factory=list)
    entrenador: "Entrenador" = None

    def asignar_entrenador(self, entrenador):
        self.entrenador = entrenador
        entrenador.clientes.append(self)
        print(f"\n✅ {entrenador.nombre_completo} ha sido asignado como tu entrenador.")

    def agregar_rutina(self, rutina):
        self.rutinas.append(rutina)
        print(f"🏋️‍♂️ Rutina creada y asignada correctamente.\n")

    def registrar_progreso(self, progreso):
        self.progreso.append(progreso)
        print(f"📈 Progreso registrado para {self.nombre_completo} en {progreso.fecha_control}.")


@dataclass
class Entrenador(Usuario):
    especialidad: str
    anos_experiencia: int
    clientes: List[Cliente] = field(default_factory=list)

    def crear_rutina(self, cliente: Cliente):
        ejercicios_posibles = [
            Ejercicio("Press de banca", 4, 10),
            Ejercicio("Sentadilla", 4, 8),
            Ejercicio("Peso muerto", 4, 6),
            Ejercicio("Dominadas", 3, 10),
            Ejercicio("Curl de bíceps", 4, 12),
            Ejercicio("Extensión de tríceps", 4, 12),
            Ejercicio("Zancadas", 3, 10),
            Ejercicio("Remo con barra", 4, 8),
            Ejercicio("Elevaciones laterales", 3, 15),
        ]


        seleccion = random.sample(ejercicios_posibles, k=4)
        dias = random.choice(["Lunes-Miércoles-Viernes", "Martes-Jueves-Sábado", "Todos los días"])
        rutina = RutinaEjercicio(dias_entrenamiento=dias, ejercicios=seleccion)
        cliente.agregar_rutina(rutina)
        print(f"📅 Rutina creada por {self.nombre_completo} para {cliente.nombre_completo}.")
        rutina.mostrar_rutina()




@dataclass
class Ejercicio:
    nombre: str
    series: int
    repeticiones: int


@dataclass
class RutinaEjercicio:
    dias_entrenamiento: str
    ejercicios: List[Ejercicio] = field(default_factory=list)

    def mostrar_rutina(self):
        print(f"\nRutina de entrenamiento ({self.dias_entrenamiento}):")
        for e in self.ejercicios:
            print(f" - {e.nombre}: {e.series} series x {e.repeticiones} repeticiones")


@dataclass
class PlanAlimentacion:
    comidas_diarias: str
    calorias_macronutrientes: str
    recomendaciones_adicionales: str


@dataclass
class ProgresoFisico:
    fecha_control: date
    peso_actual: float
    medidas_corporales: str
    observaciones: str




def main():
    print("🏋️‍♂️ Bienvenido al Sistema de Gestión del Gimnasio 🏋️‍♀️\n")


    entrenadores = [
        Entrenador("Carlos Pérez", "1001", "Fuerza", 6),
        Entrenador("Laura Gómez", "1002", "Resistencia", 4),
        Entrenador("Andrés Torres", "1003", "Hipertrofia", 5)
    ]


    nombre = input("Tu nombre completo: ")
    documento = input("Documento de identidad: ")
    edad = int(input("Edad: "))
    objetivo = input("Objetivo de entrenamiento (ej: ganar músculo, bajar peso, tonificar): ")
    estado_inicial = input("Estado físico inicial (ej: principiante, intermedio, avanzado): ")

    cliente = Cliente(nombre, documento, edad, objetivo, estado_inicial)


    print("\nEntrenadores disponibles:")
    for i, ent in enumerate(entrenadores, 1):
        print(f"{i}. {ent.nombre_completo} ({ent.especialidad}, {ent.anos_experiencia} años de experiencia)")

    opcion = int(input("Selecciona tu entrenador (1-3): "))
    cliente.asignar_entrenador(entrenadores[opcion - 1])


    cliente.entrenador.crear_rutina(cliente)


    print("\n¿Deseas registrar tu progreso físico? (s/n)")
    if input("> ").lower() == "s":
        peso = float(input("Peso actual (kg): "))
        medidas = input("Medidas corporales (ej: pecho, cintura, etc): ")
        obs = input("Observaciones: ")
        progreso = ProgresoFisico(date.today(), peso, medidas, obs)
        cliente.registrar_progreso(progreso)

    print("\n✅ ¡Datos registrados exitosamente! ¡Sigue entrenando y mejorando cada día!")



if __name__ == "__main__":
    main()
