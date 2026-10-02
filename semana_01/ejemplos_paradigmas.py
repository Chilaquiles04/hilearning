"""
Ejemplos Comparativos de Paradigmas en Python - Semana 1
Materia: Programación Funcional
Facultad de Ingeniería Mecánica y Eléctrica - Universidad de Colima
"""

from typing import Tuple, List, Dict, Any


# ==============================================================================
# 1. COMPARACIÓN DE PARADIGMAS: PROCESAMIENTO DE CONVERSACIONES
# ==============================================================================

datos_conversacion = [
    {"turno": 1, "emisor": "user", "palabras": 14, "errores": 1},
    {"turno": 2, "emisor": "agent", "palabras": 20, "errores": 0},
    {"turno": 3, "emisor": "user", "palabras": 25, "errores": 0},
    {"turno": 4, "emisor": "user", "palabras": 8, "errores": 2},
    {"turno": 5, "emisor": "agent", "palabras": 18, "errores": 0},
]

# --- 1.1 Enfoque Estructurado (Imperativo con acumulación y bucles) ---
def analizar_estructurado(historial: List[Dict[str, Any]]) -> Dict[str, float]:
    total_palabras_usuario = 0
    total_errores_usuario = 0
    turnos_usuario = 0

    for turno in historial:
        if turno["emisor"] == "user":
            total_palabras_usuario += turno["palabras"]
            total_errores_usuario += turno["errores"]
            turnos_usuario += 1

    promedio_palabras = total_palabras_usuario / turnos_usuario if turnos_usuario > 0 else 0
    return {
        "turnos_usuario": turnos_usuario,
        "total_palabras": total_palabras_usuario,
        "promedio_palabras": promedio_palabras,
        "total_errores": total_errores_usuario
    }


# --- 1.2 Enfoque Orientado a Objetos (Encapsulamiento de estado) ---
class SesionConversacion:
    def __init__(self, turnos: List[Dict[str, Any]]):
        self._turnos = list(turnos)

    def agregar_turno(self, turno: Dict[str, Any]) -> None:
        self._turnos.append(turno)

    def obtener_metricas_usuario(self) -> Dict[str, float]:
        turnos_user = [t for t in self._turnos if t["emisor"] == "user"]
        total_p = sum(t["palabras"] for t in turnos_user)
        total_e = sum(t["errores"] for t in turnos_user)
        cant = len(turnos_user)
        return {
            "turnos_usuario": cant,
            "total_palabras": total_p,
            "promedio_palabras": (total_p / cant) if cant > 0 else 0,
            "total_errores": total_e
        }


# --- 1.3 Enfoque Funcional (Funciones puras, datos inmutables y transformaciones) ---
Turno = Tuple[int, str, int, int]  # (id, emisor, palabras, errores)

def filtrar_turnos_usuario(historial: Tuple[Turno, ...]) -> Tuple[Turno, ...]:
    """Filtra únicamente los turnos emitidos por el usuario."""
    return tuple(t for t in historial if t[1] == "user")

def calcular_metricas_usuario(turnos_usuario: Tuple[Turno, ...]) -> Dict[str, float]:
    """Calcula métricas agregadas de forma pura a partir de una tupla inmutable."""
    cantidad = len(turnos_usuario)
    total_palabras = sum(t[2] for t in turnos_usuario)
    total_errores = sum(t[3] for t in turnos_usuario)
    return {
        "turnos_usuario": cantidad,
        "total_palabras": total_palabras,
        "promedio_palabras": (total_palabras / cantidad) if cantidad > 0 else 0.0,
        "total_errores": total_errores
    }


# ==============================================================================
# 2. STRUCTURAL PATTERN MATCHING (Python 3.10+) EN CONTEXTO FUNCIONAL
# ==============================================================================

def despachador_eventos(evento: Tuple[str, Any]) -> str:
    """Ejemplo de Pattern Matching para manejar el ciclo de vida de la sesión."""
    match evento:
        case ("INICIO", {"rol": rol, "nivel": nivel}):
            return f"[INICIO] Sesión iniciada -> Rol: {rol} | Nivel: {nivel}"
        case ("MENSAJE", str(texto)) if len(texto.strip()) > 0:
            return f"[MENSAJE] Mensaje recibido ({len(texto)} caracteres): '{texto}'"
        case ("PAUSA", int(segundos)):
            return f"[PAUSA] Sesión en pausa por {segundos} segundos"
        case ("FIN", {"razon": razon, "puntaje": score}):
            return f"[FIN] Sesión finalizada por '{razon}' con puntaje {score}/100"
        case _:
            return "[ADVERTENCIA] Evento desconocido o formato no válido"


# ==============================================================================
# EJECUCIÓN Y DEMOSTRACIÓN
# ==============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DEMOSTRACIÓN DE PARADIGMAS DE PROGRAMACIÓN")
    print("=" * 60)

    # 1. Estructurado
    res_est = analizar_estructurado(datos_conversacion)
    print(f"\n1. Resultado Estructurado:\n   {res_est}")

    # 2. POO
    sesion = SesionConversacion(datos_conversacion)
    res_poo = sesion.obtener_metricas_usuario()
    print(f"\n2. Resultado POO:\n   {res_poo}")

    # 3. Funcional
    historial_inmutable: Tuple[Turno, ...] = (
        (1, "user", 14, 1),
        (2, "agent", 20, 0),
        (3, "user", 25, 0),
        (4, "user", 8, 2),
        (5, "agent", 18, 0)
    )
    turnos_u = filtrar_turnos_usuario(historial_inmutable)
    res_func = calcular_metricas_usuario(turnos_u)
    print(f"\n3. Resultado Funcional:\n   {res_func}")

    # 4. Pattern Matching
    print("\n" + "=" * 60)
    print("DEMOSTRACIÓN DE STRUCTURAL PATTERN MATCHING")
    print("=" * 60)
    eventos = [
        ("INICIO", {"rol": "Entrevista de Trabajo", "nivel": "B1"}),
        ("MENSAJE", "Hello! I am ready for the interview."),
        ("PAUSA", 30),
        ("FIN", {"razon": "Tiempo completado (5 min)", "puntaje": 88}),
        ("DESCONOCIDO", None)
    ]
    for ev in eventos:
        print(despachador_eventos(ev))
