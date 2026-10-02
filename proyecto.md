Nombre Provisional: Hi Learning

Problema o Necesidad
Al aprender un nuevo idioma nos enfrentamos a diversas dificultades, una de ellas y la principal es que el alumno no lograr avanzar en su nivel de conversación, esto debido a razones como el miedo al error, la falta de confianza, aislamiento en la práctica, entorno poco estimulante y sin oportunidades de practica.
Con cada año que pasa el idioma ingles va tomando demasiado poder en las industrias y las comunicaciones, siendo aproximadamente desde 1990, con el auge de las tecnologías y el internet que se convirtió en la principal lengua del mundo. Según EF English Proficiency Index (EF EPI), entre el 40% y 50% de los estudiantes de Latinoamérica que logra obtener un nivel intermedio de comprensión lectora y auditiva(B1), solamente menos del 20% logra transformar esos aprendizajes en producción oral espontanea. Esto deja un porcentaje significativo de estudiantes egresados en el conocido “efecto embudo”.

Usuario

El sistema esta dirigido a estudiantes de la Universidad de Colima de todos los niveles educativos.

Funcionamiento General

Entrada del Usuario (Tema + Vocabulario + Nivel del Ingles)
El estudiante ingresa el tema de la lección (ej. "Entrevista de trabajo", "Viajes") y la lista de vocabulario o gramática que desea practicar.
Módulo de Procesamiento (Extracción de Procesamiento)
El sistema valida los datos, limpia la lista de palabras clave y construye una estructura JSON que alimentará la memoria a corto plazo del agente de IA.
Generador de Contexto (Simulación de Rol)
El sistema combina los datos del usuario con las instrucciones base de la IA para generar el perfil de la conversación:
Objetivo principal: Mantener una conversación fluida de mínimo 5 minutos (o un número equivalente de turnos, ej. 8 a 10 intercambios).
•	Restricción lingüística: Ajustar el nivel de complejidad del vocabulario y gramática al nivel indicado por el estudiante.
•	Inyección de palabras clave: Forzar a la IA a crear preguntas abiertas que obliguen o sugieran al alumno usar el vocabulario ingresado.
•	Asignación de rol: Definir el papel de la IA (ej. entrevistador, turista, amigo en una cafetería) según el tema del usuario.

Bucle de Conversación (5 minutos de conversación / Turnos)
La IA inicia la interacción con una pregunta abierta ambientada en el escenario elegido.
Estrategia pedagógica:
•	La IA no interrumpe para corregir gramática de inmediato, priorizando la fluidez y la confianza.
•	Si el usuario se traba o responde de forma muy corta, la IA repregunta utilizando opciones o pistas.
•	Registra internamente qué palabras de la lista del alumno ya han sido utilizadas correctamente.
Un contador del sistema rastrea la duración de la sesión. Al llegar a los 5 minutos de interacción activa, la IA encamina la conversación hacia una despedida natural para no cortar abruptamente al usuario.
Evaluación Final (Feedback y Reporte)
Una vez cerrada la sesión, el agente procesa la transcripción completa y genera un reporte estructurado para el alumno.

Responsabilidades del Agente

1. Facilitador y dinamizador de la conversación
El agente debe asumir un rol interactivo (ej. entrevistador, cliente, amigo) adaptado al tema y nivel del usuario, formulando preguntas abiertas que obliguen al estudiante a hablar y guíen la charla para que incorpore el vocabulario objetivo de forma natural sin romper el ritmo de la conversación.
2. Evaluador en tiempo real (seguimiento en segundo plano)
Mientras la interacción ocurre, el agente debe registrar en segundo plano el desempeño del alumno: monitorear qué palabras clave de la lista han sido utilizadas, calcular el tiempo o turnos transcurridos y detectar errores gramaticales o de léxico sin interrumpir al usuario durante los 5 minutos de práctica.
3. Generador de retroalimentación estructurada
Al finalizar la sesión, el agente debe consolidar los datos recopilados para entregar un reporte claro y procesable. Su responsabilidad es categorizar el vocabulario utilizado vs. el pendiente, señalar las correcciones lingüísticas de forma constructiva y ofrecer una métrica del desempeño del estudiante.

Información Necesaria

Recibir(Inputs)	Datos de configuración inicial: Tema de la conversación, lista de vocabulario/gramática objetivo y nivel del estudiante (A1-C2).
Entradas del usuario durante la charla: Mensajes de texto o voz enviados por el alumno en cada turno.
Metadatos de sesión: Identificador del usuario (User ID), marca de tiempo de inicio (Timestamp) y límites de tiempo o turnos.
Consultar	Plantillas de Prompts: Reglas base de comportamiento del LLM (System Prompts).
Historial del usuario: Sesiones previas para medir evolución o no repetir temas.
Diccionario/Ontología: Validación de vocabulario y reglas gramaticales para el análisis.
Transformar	Ensamblado del Prompt Dinámico: Conversión de los inputs iniciales a una estructura JSON con el contexto del rol y metas pedagógicas.
Procesamiento del lenguaje (LLM): Transformación del texto del usuario en respuestas contextuales ajustadas al nivel.
Análisis de cobertura de vocabulario: Mapeo en tiempo real para marcar qué palabras objetivo ya fueron utilizadas.
Extracción de correcciones: Identificación y reformulación de errores gramaticales (Texto original vs. Forma natural).
Almacenar	Transcripción de la sesión: Registro completo de los turnos de conversación (Chat History).
Métricas de desempeño: Porcentaje de vocabulario completado, duración de la sesión y cantidad de turnos.
Reporte de Feedback: Registro de errores recurrentes para seguimiento y evaluación futura del estudiante.

Resultado Esperado

El estudiante obtendrá una conversación estimulante en idioma inglés, respecto al los temas y contenido visto en clase, podrá desarrollar confianza en si mismo al hablar y gracias a la retroalimentación y las recomendaciones del final podrá localizar los puntos débiles que tiene en speaking respecto a su nivel.

Valor de la propuesta

Hi Learning aborda directamente el principal problema en la enseñanza del inglés, donde hasta un 80% de los alumnos con nivel B1 sufren el "efecto embudo" y no logran hablar con fluidez. Mediante una propuesta útil, interesante y diferente basada en un entorno seguro de práctica. Su gran utilidad radica en conectar directamente con el currículo del estudiante al personalizar las charlas según el vocabulario visto en clase y entregar al final un reporte con métricas de desempeño y correcciones gramaticales, superando el miedo al error. Lo que la hace interesante es su arquitectura de IA en dos capas, la cual simula roles inmersivos (como entrevistas o viajes) adaptados al nivel del usuario (A1-C2) mientras en segundo plano rastrea el uso de palabras clave sin interrumpir la charla. Finalmente, su factor diferenciador reside en su formato dinámico de alta intensidad enfocado en micro-sesiones de 5 minutos (8 a 10 turnos) que priorizan la fluidez y la confianza sobre la corrección inmediata, combatiendo la fatiga y convirtiendo el conocimiento teórico en habilidades orales reales dentro del ecosistema universitario.