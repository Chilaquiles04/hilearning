"""
Ejercicios Prácticos de Auto-evaluación - Semana 1
Materia: Programación Funcional
Instrucciones: Completa las funciones que contienen 'pass' o 'raise NotImplementedError'.
Ejecuta este archivo con 'python semana_01/ejercicios_practicos.py' para validar con los asserts.
"""

from typing import Tuple, List, Dict, Any


# ==============================================================================
# EJERCICIO 1: Función Pura de Transformación
# Enunciado: Crea una función pura 'calcular_fluidez_palabras' que reciba una tupla
# de palabras y una duración en segundos (float/int). Debe retornar la velocidad en
# Palabras Por Minuto (PPM), redondeada a 2 decimales.
# Nota: PPM = (total_palabras / duracion_segundos) * 60
# Si la duracion_segundos es <= 0, debe retornar 0.0.
# ==============================================================================

def calcular_fluidez_palabras(palabras: Tuple[str, ...], duracion_segundos: float) -> float:
    if duracion_segundos <= 0 or not palabras:
        return 0.0
    ppm = (len(palabras) / duracion_segundos) * 60.0
    return round(ppm, 2)


# ==============================================================================
# EJERCICIO 2: Inmutabilidad y Filtrado Funcional
# Enunciado: Crea una función pura 'filtrar_mensajes_largos' que reciba una tupla
# de cadenas de texto y un número entero 'longitud_minima'.
# Debe retornar una NUEVA tupla que contenga solo los textos cuya cantidad de
# caracteres sea mayor o igual a 'longitud_minima', convertidos a mayúsculas.
# No uses bucles for tradicionales ni mutaciones sobre listas.
# ==============================================================================

def filtrar_mensajes_largos(mensajes: Tuple[str, ...], longitud_minima: int) -> Tuple[str, ...]:
    return tuple(m.upper() for m in mensajes if len(m) >= longitud_minima)


# ==============================================================================
# EJERCICIO 3: Pattern Matching Declarativo
# Enunciado: Crea una función 'evaluar_estado_conversacion' que use 'match / case'
# para evaluar una tupla que representa el estado de una micro-sesión:
# - ("TIEMPO_RESTANTE", segundos) si segundos > 60 -> "En curso normal"
# - ("TIEMPO_RESTANTE", segundos) si 0 < segundos <= 60 -> "Alerta: Último minuto"
# - ("TIEMPO_RESTANTE", 0) -> "Tiempo finalizado"
# - ("ERROR", codigo, descripcion) -> f"Fallo {codigo}: {descripcion}"
# - Cualquier otro formato -> "Estado inválido"
# ==============================================================================

def evaluar_estado_conversacion(estado: Tuple[Any, ...]) -> str:
    match estado:
        case ("TIEMPO_RESTANTE", segundos) if segundos > 60:
            return "En curso normal"
        case ("TIEMPO_RESTANTE", segundos) if 0 < segundos <= 60:
            return "Alerta: Último minuto"
        case ("TIEMPO_RESTANTE", 0):
            return "Tiempo finalizado"
        case ("ERROR", int(codigo), str(descripcion)):
            return f"Fallo {codigo}: {descripcion}"
        case _:
            return "Estado inválido"


# ==============================================================================
# SUITE DE PRUEBAS AUTOMATIZADAS (ASSERTS)
# ==============================================================================

def ejecutar_pruebas():
    print("Iniciando validacion de ejercicios de la Semana 1...")

    # Pruebas Ejercicio 1
    palabras_test = ("Hello", "I", "am", "practicing", "my", "English", "speaking", "skills")
    assert calcular_fluidez_palabras(palabras_test, 10.0) == 48.0, "Fallo en Test 1.1"
    assert calcular_fluidez_palabras(palabras_test, 0) == 0.0, "Fallo en Test 1.2"
    assert calcular_fluidez_palabras((), 30.0) == 0.0, "Fallo en Test 1.3"
    print("[OK] Ejercicio 1: Superado con exito.")

    # Pruebas Ejercicio 2
    mensajes_test = ("hi", "welcome to the simulation", "ok", "let us start the interview")
    resultado_2 = filtrar_mensajes_largos(mensajes_test, 10)
    assert resultado_2 == ("WELCOME TO THE SIMULATION", "LET US START THE INTERVIEW"), "Fallo en Test 2.1"
    assert isinstance(resultado_2, tuple), "Debe retornar una tupla inmutable"
    print("[OK] Ejercicio 2: Superado con exito.")

    # Pruebas Ejercicio 3
    assert evaluar_estado_conversacion(("TIEMPO_RESTANTE", 180)) == "En curso normal", "Fallo en Test 3.1"
    assert evaluar_estado_conversacion(("TIEMPO_RESTANTE", 45)) == "Alerta: Ultimo minuto", "Fallo en Test 3.2"
    assert evaluar_estado_conversacion(("TIEMPO_RESTANTE", 0)) == "Tiempo finalizado", "Fallo en Test 3.3"
    assert evaluar_estado_conversacion(("ERROR", 404, "Voz no detectada")) == "Fallo 404: Voz no detectada", "Fallo en Test 3.4"
    assert evaluar_estado_conversacion(("DESCONOCIDO",)) == "Estado invalido", "Fallo en Test 3.5"
    print("[OK] Ejercicio 3: Superado con exito.")

    print("\n[EXITO] Todos los ejercicios de la Semana 1 han pasado las pruebas unitarias satisfactoriamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
