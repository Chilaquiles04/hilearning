# Bitácora de Estudio y Registro de Prompts

## Información General del Proyecto
- **Nombre del Proyecto**: Hi Learning
- **Institución / Contexto**: Universidad de Colima (Estudiantes de todos los niveles educativos)
- **Propósito**: Plataforma interactiva de práctica conversacional en inglés con IA para superar el "efecto embudo" (alumnos con comprensión pero dificultad en producción oral), ofreciendo micro-sesiones de 5 minutos (8-10 turnos), simulación de roles adaptativos y retroalimentación estructurada sin interrupciones punitivas.
- **Documento Base**: [`proyecto.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/proyecto.md)
- **Fecha de Inicio**: 8 de Septiembre de 2026

---

## Historial de Indicaciones y Respuestas

### Registro #1 - Orientación Inicial del Proyecto
- **Timestamp**: 2026-09-08 08:17:23 -06:00
- **Indicación del Usuario (Prompt)**:
  > `como inicio este proyecto`
- **Objetivo**: Proporcionar una ruta de arranque clara, estructurada y técnica a partir del documento de especificaciones `proyecto.md`.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se analizó a detalle el archivo de especificación `proyecto.md`.
  2. Se esquematizó el flujo operativo general: Configuración Inicial ➔ Sala de Conversación Inmersiva (Voz/Texto + Temporizador + Rastreador en segundo plano) ➔ Motor de IA en Dos Capas ➔ Pantalla de Reporte y Feedback.
  3. Se recomendó el stack tecnológico (HTML5/CSS3/JS o Vite, Web Speech API para práctica oral, API LLM para rol y evaluación, LocalStorage para persistencia).
  4. Se definieron las 4 fases de desarrollo para su ejecución secuencial.
- **Material / Entregables Generados**:
  - Propuesta de arquitectura y roadmap inicial de desarrollo.
- **Estado**: ✅ Completado

---

### Registro #2 - Creación de Bitácora y Skill Automatizado
- **Timestamp**: 2026-09-08 08:43:43 -06:00
- **Indicación del Usuario (Prompt)**:
  > `-usa la bitacora de estudio para crear el material y cada indicacion (prompt) grabala ahi con tu respuesta (como atendiste la peticion)`  
  > `-crea un skill para realizar esta bitácora y actualizarla en cada indicación que te de`
- **Objetivo**: Configurar un sistema persistente de registro donde cada prompt y su resolución queden documentados en la bitácora de estudio, apoyado en un Skill especializado y una regla permanente de espacio de trabajo.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se creó el Skill personalizado [`bitacora-estudio`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/.agents/skills/bitacora-estudio/SKILL.md) siguiendo la especificación estándar de Antigravity Customizations.
  2. Se configuró el archivo de regla global del proyecto [`GEMINI.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/GEMINI.md) para garantizar que en cada indicación futura se actualice la bitácora automáticamente.
  3. Se inicializó y estructuró este documento [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md) con el historial completo (Registro #1 y Registro #2).
- **Material / Entregables Generados**:
  - [`SKILL.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/.agents/skills/bitacora-estudio/SKILL.md)
  - [`GEMINI.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/GEMINI.md)
  - [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md)
- **Estado**: ✅ Completado

---

### Registro #3 - Inclusión de Timestamp en Skill y Bitácora
- **Timestamp**: 2026-09-08 08:55:13 -06:00
- **Indicación del Usuario (Prompt)**:
  > `-agrega un timestamp a la skill de la bitacora en la que se actualiza cada indicacion`
- **Objetivo**: Integrar la captura y registro explícito del timestamp (fecha y hora exacta) en cada entrada de la bitácora y en la directiva del Skill.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se modificó el archivo [`SKILL.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/.agents/skills/bitacora-estudio/SKILL.md) para requerir y especificar el formato estándar del campo `Timestamp: YYYY-MM-DD HH:mm:ss (Zona Horaria)` en cada registro.
  2. Se homologaron los registros previos de [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md) con sus marcas de tiempo exactas.
  3. Se registró esta nueva interacción como Registro #3.
- **Material / Entregables Generados**:
  - [`SKILL.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/.agents/skills/bitacora-estudio/SKILL.md) (Actualizado con directiva de Timestamp)
  - [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md) (Actualizado con Registro #3 y marcas de tiempo)
- **Estado**: ✅ Completado

### Registro #4 - Análisis del Plan de Materia y Recomendaciones de Gestión del Tiempo
- **Timestamp**: 2026-09-10 11:39:02 -06:00
- **Indicación del Usuario (Prompt)**:
  > `Analiza plan_materia.md y dame recomendaciones de como deberia dedicar mi tiempo`
- **Objetivo**: Realizar un desglose analítico del documento `plan_materia.md` (Programación Funcional - 3º Semestre ICI) y formular una estrategia estructurada y optimizada de distribución del tiempo académico basada en ponderaciones (50% proyecto, 25% práctico, 25% teórico), cronograma de unidades y fechas de evaluación.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se examinó a detalle el archivo [`plan_materia.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/plan_materia.md), identificando carga horaria, fechas de parciales (1º Parcial: 01/10/2026, 2º Parcial: 26/11/2026, Ordinario: 11/12/2026), distribución de unidades temáticas (I, II y III) y criterios de evaluación.
  2. Se diseñó un plan de distribución del tiempo alineado con las ponderaciones reales de calificación (50% Proyecto con IA Agéntica, 25% Examen Práctico, 25% Examen Teórico).
  3. Se estructuró un cronograma táctico por fases con enfoque en el presente inmediato (cierre de Unidad I y entrada a Unidad II de cara al 1er parcial en 3 semanas) y una rutina semanal de estudio recomendada.
  4. Se documentó la intervención en la bitácora de estudio.
- **Material / Entregables Generados**:
  - Recomendaciones estratégicas de gestión del tiempo y desglose analítico en respuesta interactiva.
  - Registro #4 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md).
- **Estado**: ✅ Completado

### Registro #5 - Inicio del Contenido de Estudio: Semana 1 (Unidad I)
- **Timestamp**: 2026-09-10 11:52:10 -06:00
- **Indicación del Usuario (Prompt)**:
  > `inicia el contenido de la semana 1`
- **Objetivo**: Desarrollar e implementar el paquete integral de contenidos teóricos, ejemplos prácticos ejecutables y ejercicios de auto-evaluación para la Semana 1 (Unidad I: Fundamentos del paradigma de programación funcional, comparación con POO/estructurado, funciones puras, inmutabilidad y pattern matching en Python).
- **Acciones Realizadas / Cómo se atendió**:
  1. Se estructuró la guía teórica y pedagógica en [`semana_01/contenido_semana_1.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/semana_01/contenido_semana_1.md) abordando conceptos de funciones puras, inmutabilidad, transparencia referencial, comparación exhaustiva POO vs PF y sintaxis de Python (expresiones condicionales, pattern matching).
  2. Se desarrolló el script de ejemplos ejecutables [`semana_01/ejemplos_paradigmas.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/semana_01/ejemplos_paradigmas.py) implementando el procesamiento de métricas conversacionales en los 3 paradigmas y despacho de eventos con `match / case`.
  3. Se diseñó el script de auto-evaluación [`semana_01/ejercicios_practicos.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/semana_01/ejercicios_practicos.py) con suite de pruebas automáticas (`assert`) orientado al examen práctico y conectado con el proyecto Hi Learning.
  4. Se actualizó la bitácora de estudio con el registro correspondiente.
- **Material / Entregables Generados**:
  - [`semana_01/contenido_semana_1.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/semana_01/contenido_semana_1.md)
  - [`semana_01/ejemplos_paradigmas.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/semana_01/ejemplos_paradigmas.py)
  - [`semana_01/ejercicios_practicos.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/semana_01/ejercicios_practicos.py)
  - [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md)
### Registro #6 - Propuesta y Recomendación de Arquitectura para Hi Learning
- **Timestamp**: 2026-09-10 12:04:09 -06:00
- **Indicación del Usuario (Prompt)**:
  > `que arquitectura me recomindas para mi proyecto?`
- **Objetivo**: Diseñar y proponer una arquitectura de software robusta, modular y altamente alineada con los requerimientos de `proyecto.md` (Hi Learning: micro-sesiones de 5 min, agente de doble capa, Web Speech API, tracking no intrusivo) y las competencias de `plan_materia.md` (Programación Funcional en Python: Núcleo Funcional + Shell Imperativo, inmutabilidad, pipelines de datos y generadores).
- **Acciones Realizadas / Cómo se atendió**:
  1. Se analizaron las responsabilidades del sistema en [`proyecto.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/proyecto.md) (simulación de rol, evaluador en segundo plano, generador de feedback estructurado) y la ponderación del 50% de proyecto en [`plan_materia.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/plan_materia.md).
  2. Se diseñó la arquitectura basada en el patrón **Functional Core, Imperative Shell (FCIS)** combinado con **Pipes & Filters (Tuberías de Datos)** y streaming con generadores.
  3. Se elaboraron diagramas estructurales en Mermaid y se especificaron las 4 capas del sistema (Frontend UI, API Gateway/WebSockets, Núcleo Funcional en Python y Servicios Externos/LLM).
  4. Se documentó cómo cada tema del programa de estudios (Unidades I, II y III) se mapea directamente en los módulos del proyecto.
  5. Se registró la interacción en la bitácora de estudio.
- **Material / Entregables Generados**:
  - Propuesta arquitectónica detallada con diagramas de flujo y desglose de capas.
  - Registro #6 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md).
### Registro #7 - Estrategia de Arranque del Proyecto (Primeros Pasos Arquitectónicos)
- **Timestamp**: 2026-09-10 12:19:32 -06:00
- **Indicación del Usuario (Prompt)**:
  > `y hablando de la arquitectura con que me recomiendas iniciar`
- **Objetivo**: Definir una ruta de implementación pragmática, paso a paso, priorizando la construcción del Núcleo Funcional (Domain Types y Funciones Puras de Tracking) antes de la infraestructura web, asegurando el cumplimiento temprano de los requerimientos de evaluación de la materia.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se estructuró la estrategia de arranque en 4 etapas ordenadas según el principio *Inside-Out / Functional Core First*:
     - **Paso 1**: Modelado de Tipos e Invariantes Inmutables (`core/types.py`).
     - **Paso 2**: Tubería Funcional Pura de Seguimiento de Vocabulario y Métricas (`core/tracking.py`).
     - **Paso 3**: Suite de Pruebas Automatizadas con `assert` (`tests/test_core.py`).
     - **Paso 4**: Interfaz de Usuario MVP en Web con Web Speech API (`client/`).
  2. Se formularon los esquemas de código base listos para inicializar el proyecto de inmediato.
  3. Se documentó la intervención en la bitácora de estudio.
- **Material / Entregables Generados**:
  - Hoja de ruta de arranque inmediato y propuesta de código para `core/types.py` y `core/tracking.py`.
  - Registro #7 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md).
- **Estado**: ✅ Completado

### Registro #8 - Creación del Documento de Especificaciones Técnicas
- **Timestamp**: 2026-09-10 12:28:51 -06:00
- **Indicación del Usuario (Prompt)**:
  > `crea un archivo especificaciones.md con especificaciones generales donde pongas puntos importantes de mi proyecto derivado d elas preguntas que te hago, por ejemplo  la tecnologia que me recomiendas usar en front y la tecnolgia que me recomiendas en el back`
- **Objetivo**: Consolidar en un documento formal de especificaciones técnicas (`especificaciones.md`) todos los requerimientos, decisiones de arquitectura (FCIS + Pipes & Filters), tecnologías recomendadas para Frontend (HTML5/Vanilla CSS/JS + Web Speech API) y Backend (FastAPI + Python Core Funcional + Gemini API), estructura del repositorio y plan de fases.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se recopilaron y estructuraron los acuerdos y recomendaciones técnicas generados en las interacciones previas.
  2. Se redactó y creó el archivo [`especificaciones.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/especificaciones.md) conteniendo:
     - Resumen ejecutivo y contexto del proyecto Hi Learning.
     - Diagrama y detalle de la arquitectura *Functional Core, Imperative Shell (FCIS)*.
     - Tabla comparativa y justificación de tecnologías recomendadas para Frontend y Backend.
     - Mapeo del Núcleo Funcional en Python con los criterios de evaluación de la materia (50%).
     - Flujo funcional de usuario y diagrama de estados.
     - Árbol de carpetas del repositorio y roadmap de fases de implementación.
  3. Se actualizó la bitácora de estudio con el registro correspondiente.
- **Material / Entregables Generados**:
  - [`especificaciones.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/especificaciones.md)
  - [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md)
- **Estado**: ✅ Completado

### Registro #9 - Justificación Técnica de Python en el Backend
- **Timestamp**: 2026-09-10 12:30:29 -06:00
- **Indicación del Usuario (Prompt)**:
  > `porque me recomiendas python para el backtend mas que algun otro  lenguaje`
- **Objetivo**: Fundamentar con argumentos técnicos, de ingeniería de software y de alineación académica por qué Python (con FastAPI y su Núcleo Funcional) es la opción óptima para el backend de Hi Learning frente a alternativas como Node.js, Go o Java.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se analizaron los 5 factores determinantes:
     - **Alineación académica**: Cumplimiento del plan de estudios de Programación Funcional en Python ([`plan_materia.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/plan_materia.md)) que pondera el proyecto con el 50%.
     - **Ecosistema nativo de IA**: Soporte de primera clase para SDKs de LLM (Gemini API / OpenAI).
     - **Soporte funcional multiparadigma**: Implementación natural de HOF (`map`, `filter`, `reduce`), generadores (`yield`), decoradores y *Pattern Matching*.
     - **Rendimiento asíncrono moderno**: Alta eficiencia con FastAPI y WebSockets sobre `asyncio`.
     - **Simplicidad y legibilidad**: Menor *boilerplate* y facilidad de pruebas unitarias puras.
  2. Se elaboró una tabla comparativa directa (Python vs Node.js vs Go/Java).
  3. Se documentó la respuesta en la bitácora de estudio.
- **Material / Entregables Generados**:
  - Análisis comparativo técnico y justificación académica en respuesta.
  - Registro #9 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md).
- **Estado**: ✅ Completado

### Registro #10 - Ubicación y Utilidad de Vite.js en la Arquitectura
- **Timestamp**: 2026-09-10 12:32:26 -06:00
- **Indicación del Usuario (Prompt)**:
  > `donde puedo usar vite js`
- **Objetivo**: Explicar con precisión dónde se integra Vite.js dentro del stack de Hi Learning (exclusivamente en la **Capa 1: Frontend / Cliente**), qué beneficios aporta al flujo de trabajo de desarrollo (HMR ultrarrápido, bundling moderno, proxy a FastAPI para evitar CORS) y cómo convive armoniosamente con el backend en Python.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se definió la ubicación exacta de Vite.js en la carpeta `client/` como herramienta de construcción (*build tool*) y servidor de desarrollo para la interfaz web.
  2. Se detallaron los 4 casos de uso clave de Vite en el proyecto:
     - Recarga en caliente instantánea (HMR) para estilizado y manipulación de Web Speech API.
     - Organización modular del código JavaScript en módulos ES (`speech.js`, `timer.js`, `chat.js`).
     - Configuración de proxy inverso en `vite.config.js` para redirigir WebSockets a FastAPI sin problemas de CORS.
     - Generación del paquete estático optimizado para producción (`dist/`).
  3. Se documentó la respuesta en la bitácora de estudio.
- **Material / Entregables Generados**:
  - Explicación de integración de Vite.js y ejemplo de configuración de proxy.
  - Registro #10 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md).
- **Estado**: ✅ Completado

---

### Registro #11 - Guía Maestra de Aprendizaje de Python (Desde Cero a Backend Hi Learning)
- **Timestamp**: 2026-09-11 12:43:35 -06:00
- **Indicación del Usuario (Prompt)**:
  > `me dijiste que el principal para el back  es  python, asi que dame un guia para aprender python desde cero y que me encamine a utilizarlo en favor de mi proyecto`
- **Objetivo**: Diseñar una ruta pedagógica estructurada y un manual de aprendizaje integral que lleve al estudiante desde los fundamentos absolutos de Python (sintaxis, tipado, colecciones, control de flujo) hasta el desarrollo del núcleo funcional (pureza, inmutabilidad, HOF, generadores) y el backend asíncrono con FastAPI, WebSockets y Gemini API para el proyecto **Hi Learning**, maximizando el rendimiento académico (50% de la materia).
- **Acciones Realizadas / Cómo se atendió**:
  1. Se estructuró un roadmap de 5 fases progresivas:
     - **Fase 1**: Fundamentos y Tipado Estricto (Sintaxis, Tuplas, Sets, `match/case`).
     - **Fase 2**: Paradigma Funcional Puro (`frozen dataclasses`, `map`/`filter`/`reduce`, generadores `yield`).
     - **Fase 3**: Asincronía y Conectividad con IA (`async/await`, SDK oficial de Gemini).
     - **Fase 4**: Backend Gateway y WebSockets con FastAPI (Arquitectura FCIS).
     - **Fase 5**: Pruebas Unitarias con `pytest` y validación de pureza.
  2. Se redactó y publicó el archivo de referencia técnica [`guia_aprendizaje_python.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/guia_aprendizaje_python.md) con explicaciones conceptuales, fragmentos de código listos para ejecutar y un cronograma de 10 semanas.
  3. Se vinculó cada concepto teórico con módulos concretos del repositorio (`core/types.py`, `core/tracking.py`, `server/main.py`, `tests/test_tracking.py`).
  4. Se actualizó la bitácora de estudio con el registro correspondiente.
- **Material / Entregables Generados**:
  - [`guia_aprendizaje_python.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/guia_aprendizaje_python.md)
  - Registro #11 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md).
- **Estado**: ✅ Completado

---

### Registro #12 - Política de Modificación para la Hoja de Especificaciones
- **Timestamp**: 2026-09-17 11:26:31 -06:00
- **Indicación del Usuario (Prompt)**:
  > `ya no vas agregar la informacion automaticamente en la hoja de especificaciones ahora solo lomque yo te indique`
- **Objetivo**: Configurar la regla de restricción de edición para el archivo `especificaciones.md`, asegurando que no se modifique de manera automática y que únicamente se actualice cuando el usuario lo solicite expresamente.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se registró formalmente la directiva en las reglas del espacio de trabajo en [`GEMINI.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/GEMINI.md).
  2. Se estableció el criterio operativo: el archivo [`especificaciones.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/especificaciones.md) permanecerá estático y solo se editará bajo instrucción directa e inequívoca del usuario.
  3. Se actualizó la bitácora de estudio con el registro correspondiente.
- **Material / Entregables Generados**:
  - [`GEMINI.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/GEMINI.md) (Regla añadida)
  - Registro #12 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md)
- **Estado**: ✅ Completado

---

### Registro #13 - Comparativa de Lenguajes para Frontend y Backend
- **Timestamp**: 2026-09-17 11:27:42 -06:00
- **Indicación del Usuario (Prompt)**:
  > `ahora has una comparativa de que lenguajes me recomeindas para inciar con el back y el front`
- **Objetivo**: Desarrollar un análisis comparativo estructurado y ponderado de los principales lenguajes y frameworks para el desarrollo del Frontend y Backend en el proyecto **Hi Learning**, contrastando curva de aprendizaje, soporte de APIs de voz/IA, ecosistema funcional y alineación académica.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se compararon opciones para **Frontend**:
     - *JavaScript / TypeScript (Nativo / React / Vite)*: Máxima compatibilidad con Web Speech API, interacción fluida y bajo overhead.
     - *Dart (Flutter Web)*: Multiplataforma nativa pero más pesado y complejo para APIs de voz web.
     - *Python (Streamlit/Flet)*: Rápido de prototipar pero deficiente en interacción en tiempo real y microfonía.
  2. Se compararon opciones para **Backend**:
     - *Python (FastAPI + AsyncIO)*: 100% alineado con la materia de Programación Funcional (50%), integración directa con SDKs de IA (Gemini API) y funciones puras.
     - *JavaScript / Node.js (Express/Fastify)*: Isomorfismo de lenguaje pero sin alineación funcional académica.
     - *Go (Golang)*: Excelente concurrencia pero paradigma imperativo sin enfoque funcional para la materia.
     - *Elixir / Clojure*: Puramente funcionales pero curva de aprendizaje empinada para inicio rápido.
  3. Se concluyó con la recomendación óptima para el proyecto: **JavaScript (Vite) para Frontend** y **Python (FastAPI) para Backend**.
  4. Se actualizó la bitácora de estudio con el registro correspondiente.
- **Material / Entregables Generados**:
  - Matriz comparativa y recomendaciones detalladas en respuesta.
  - Registro #13 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md).
- **Estado**: ✅ Completado

---

### Registro #14 - Viabilidad de Streamlit para Prototipo Local 100% Python
- **Timestamp**: 2026-09-17 11:52:04 -06:00
- **Indicación del Usuario (Prompt)**:
  > `quiero que este programa sea un prototipo local, el cual va correr en la maquina y no en la web, no quiero extenderme tanto por elmomento, quieor irme por el camino facil pero que quede bien. pensaba usar para el front streamlit para usar completamente python en todo, dime que piensas`
- **Objetivo**: Evaluar de forma crítica y práctica el uso de **Streamlit** para construir un prototipo de escritorio/local 100% en Python, analizando su idoneidad para cumplir los objetivos académicos (50% de la materia), simplicidad de desarrollo, componentes nativos de chat y opciones de voz/métricas.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se analizaron las ventajas clave de Streamlit para este caso de uso:
     - 100% Python (sin necesidad de HTML/CSS/JS ni servidores separados).
     - Componentes nativos de chat (`st.chat_message`, `st.chat_input`) que ofrecen una interfaz visualmente atractiva al instante.
     - Integración directa con el Núcleo Funcional en Python (`core/`) y la API de Gemini sin capas intermedias de red/CORS.
     - Visualización nativa de métricas y gráficos de rendimiento (`st.metric`, `st.progress`, `st.bar_chart`).
  2. Se identificaron consideraciones prácticas de audio para Streamlit (uso de componentes de grabación de voz ligeros como `streamlit-mic-recorder` o enfoque híbrido texto/voz con síntesis de audio `gTTS`/`st.audio`).
  3. Se diseñó la estructura recomendada para el proyecto con arquitectura simplificada `app.py` + `core/`.
  4. Se documentó la respuesta en la bitácora de estudio.
- **Material / Entregables Generados**:
  - Análisis de viabilidad, pros/contras y arquitectura simplificada de Streamlit en respuesta.
  - Registro #14 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md).
- **Estado**: ✅ Completado

---

### Registro #15 - Implementación del Prototipo Inicial 100% Python (Streamlit + Núcleo Funcional)
- **Timestamp**: 2026-09-17 11:56:49 -06:00
- **Indicación del Usuario (Prompt)**:
  > `muy bien, entonces se queda 100% python, dame un prototipo de codigo con el cual inciar`
- **Objetivo**: Desarrollar e implementar la base de código ejecutable para el prototipo local de **Hi Learning** 100% en Python, integrando un Núcleo Funcional puro, servicio de IA (Gemini y modo simulado), e interfaz interactiva en Streamlit.
- **Acciones Realizadas / Cómo se atendió**:
  1. Se crearon las estructuras inmutables de datos en [`core/types.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/core/types.py) (`Turno`, `MetricasTurno`, `ReporteFinal` con `frozen=True`).
  2. Se implementó el pipeline funcional en [`core/tracking.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/core/tracking.py) con funciones puras utilizando `map`, `filter`, `reduce` y `match/case` para el cálculo de fluidez (PPM), análisis léxico y generación de reportes sin efectos secundarios.
  3. Se programó el servicio [`services/ai_service.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/services/ai_service.py) con soporte para Gemini API y diálogos contextuales simulados para pruebas inmediatas sin clave de API.
  4. Se construyó la aplicación interactiva [`app.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/app.py) con selector de roles, barra de progreso por turnos, vista de chat y panel de reporte final.
  5. Se definió el archivo [`requirements.txt`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/requirements.txt) y se validó la sintaxis e importación de todos los módulos.
  6. Se documentó la intervención en la bitácora de estudio.
- **Material / Entregables Generados**:
  - [`core/types.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/core/types.py)
  - [`core/tracking.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/core/tracking.py)
  - [`services/ai_service.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/services/ai_service.py)
  - [`app.py`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/app.py)
  - [`requirements.txt`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/requirements.txt)
  - Registro #15 en [`bitacora_de_estudio.md`](file:///c:/Users/fanyf/OneDrive/Documentos/proyecto/bitacora_de_estudio.md).
- **Estado**: ✅ Completado



