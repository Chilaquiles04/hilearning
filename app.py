"""
Hi Learning - Prototipo Conversacional Interactivo en Python
Desarrollado con Streamlit y Arquitectura de Programación Funcional.
Ejecución local: streamlit run app.py
"""

import time
import streamlit as st
from core.types import Turno
from core.tracking import generar_reporte_sesion, analizar_turno_usuario
from services.ai_service import SCENARIOS, responder_rol_conversacional


# 1. Configuración de la Página
st.set_page_config(
    page_title="Hi Learning | AI Conversational Coach",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Estilos visuales personalizados y limpios
st.markdown("""
<style>
    .metric-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 0.85rem;
        font-weight: 600;
        background-color: #e0f2fe;
        color: #0369a1;
    }
</style>
""", unsafe_allow_html=True)


# 2. Inicialización del Estado de Sesión (Session State)
if "historial" not in st.session_state:
    st.session_state.historial = []

if "sesion_activa" not in st.session_state:
    st.session_state.sesion_activa = True

if "ultimo_timestamp" not in st.session_state:
    st.session_state.ultimo_timestamp = time.time()

if "escenario_actual" not in st.session_state:
    st.session_state.escenario_actual = "☕ Coffee Shop"


# 3. Barra Lateral (Sidebar) de Configuración
with st.sidebar:
    st.title("🎙️ Hi Learning")
    st.caption("Micro-sesiones de práctica oral en inglés con Núcleo Funcional.")
    
    st.markdown("---")
    escenario_seleccionado = st.selectbox(
        "🎭 Selecciona tu Escenario:",
        options=list(SCENARIOS.keys()),
        index=list(SCENARIOS.keys()).index(st.session_state.escenario_actual),
        disabled=len(st.session_state.historial) > 1 and st.session_state.sesion_activa
    )

    # Si cambió de escenario y no hay historial, actualizamos
    if escenario_seleccionado != st.session_state.escenario_actual:
        st.session_state.escenario_actual = escenario_seleccionado
        st.session_state.historial = []
        st.session_state.sesion_activa = True
        st.rerun()

    limite_turnos = st.slider("🎯 Límite de Turnos por Sesión:", min_value=4, max_value=12, value=8)

    st.markdown("---")
    gemini_key = st.text_input(
        "🔑 Gemini API Key (Opcional):",
        type="password",
        help="Si no tienes una API key a la mano, la app usará el modo de simulación inteligente automáticamente."
    )

    st.markdown("---")
    if st.button("🔄 Reiniciar Sesión", use_container_width=True):
        st.session_state.historial = []
        st.session_state.sesion_activa = True
        st.session_state.ultimo_timestamp = time.time()
        st.rerun()


# Iniciar el escenario con el mensaje de bienvenida de la IA si el historial está vacío
info_escenario = SCENARIOS[st.session_state.escenario_actual]
if len(st.session_state.historial) == 0:
    st.session_state.historial.append(
        Turno(
            emisor="assistant",
            texto=info_escenario["initial_message"],
            timestamp=time.time(),
            duracion_segundos=0.0
        )
    )
    st.session_state.ultimo_timestamp = time.time()


# 4. Cabecera Principal y Barra de Progreso
st.title(f"{st.session_state.escenario_actual} - Practice Room")
st.write(f"*{info_escenario['description']}*")

turnos_usuario = [t for t in st.session_state.historial if t.emisor == "user"]
num_turnos = len(turnos_usuario)
progreso = min(num_turnos / limite_turnos, 1.0)

col_prog, col_stats = st.columns([3, 1])
with col_prog:
    st.progress(progreso, text=f"Progreso de la sesión: {num_turnos}/{limite_turnos} turnos")
with col_stats:
    if num_turnos >= limite_turnos:
        st.success("¡Meta completada!")
    else:
        st.info(f"{limite_turnos - num_turnos} turnos restantes")

st.markdown("---")


# 5. Renderizado del Historial de Conversación
for turno in st.session_state.historial:
    if turno.emisor == "assistant":
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(turno.texto)
    else:
        with st.chat_message("user", avatar="👤"):
            st.markdown(turno.texto)
            if turno.duracion_segundos > 0:
                metricas = analizar_turno_usuario(turno.texto, turno.duracion_segundos)
                st.caption(f"⚡ {metricas.total_palabras} palabras | {metricas.palabras_por_minuto} PPM")


# 6. Interacción de Entrada (Chat Input)
if st.session_state.sesion_activa and num_turnos < limite_turnos:
    prompt_usuario = st.chat_input("Escribe tu respuesta en inglés aquí...")
    
    if prompt_usuario:
        ahora = time.time()
        # Estimación de duración de turno (mínimo 3 seg)
        duracion = max(round(ahora - st.session_state.ultimo_timestamp, 1), 3.0)
        st.session_state.ultimo_timestamp = ahora

        # 1. Registrar turno del usuario
        nuevo_turno_user = Turno(
            emisor="user",
            texto=prompt_usuario,
            timestamp=ahora,
            duracion_segundos=duracion
        )
        st.session_state.historial.append(nuevo_turno_user)

        # 2. Generar respuesta de la IA
        historial_inmutable = tuple(st.session_state.historial)
        respuesta_ia = responder_rol_conversacional(
            scenario_key=st.session_state.escenario_actual,
            historial=historial_inmutable,
            api_key=gemini_key
        )

        st.session_state.historial.append(
            Turno(
                emisor="assistant",
                texto=respuesta_ia,
                timestamp=time.time(),
                duracion_segundos=0.0
            )
        )
        
        # Verificar si alcanzamos el límite
        if len([t for t in st.session_state.historial if t.emisor == "user"]) >= limite_turnos:
            st.session_state.sesion_activa = False

        st.rerun()

elif st.session_state.sesion_activa and num_turnos >= limite_turnos:
    st.session_state.sesion_activa = False
    st.rerun()





# 7. Botón de Conclusión Manual
if st.session_state.sesion_activa and num_turnos > 0:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏁 Finalizar Sesión y Generar Reporte", use_container_width=True):
        st.session_state.sesion_activa = False
        st.rerun()


# 8. Pantalla de Reporte Final (Generado con Núcleo Funcional)
if not st.session_state.sesion_activa:
    st.markdown("---")
    st.header("📊 Reporte de Rendimiento y Feedback")
    st.caption("Procesado de forma inmutable mediante tuberías puras (map, filter, reduce).")

    # Ejecutar pipeline funcional de reporte
    historial_inmutable = tuple(st.session_state.historial)
    reporte = generar_reporte_sesion(historial_inmutable)

    # Métricas Principales en Columnas
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Total de Turnos", f"{reporte.total_turnos_usuario}")
    with m2:
        st.metric("Palabras Producidas", f"{reporte.total_palabras}")
    with m3:
        st.metric("Fluidez Promedio", f"{reporte.ppm_promedio} PPM")
    with m4:
        st.metric("Nivel Evaluado", reporte.calificacion_general.split()[0])

    st.markdown("### 💡 Observaciones y Recomendaciones:")
    for sug in reporte.sugerencias_mejora:
        st.info(f"👉 {sug}")

    for fb in reporte.feedback_gramatical:
        st.write(f"✓ {fb}")

    # Desglose de Vocabulario
    with st.expander(f"📚 Vocabulario Activo Empleado ({len(reporte.vocabulario_utilizado)} términos únicos)"):
        st.write(", ".join(f"`{w}`" for w in reporte.vocabulario_utilizado))

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Iniciar Nueva Práctica", type="primary", use_container_width=True):
        st.session_state.historial = []
        st.session_state.sesion_activa = True
        st.session_state.ultimo_timestamp = time.time()
        st.rerun()
