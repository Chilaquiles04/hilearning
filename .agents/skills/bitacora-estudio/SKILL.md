---
name: bitacora-estudio
description: >-
  Gestiona y actualiza automáticamente la bitácora de estudio (bitacora_de_estudio.md)
  en cada indicación o solicitud del usuario, registrando el prompt exacto, el objetivo,
  las acciones tomadas y cómo se atendió la petición.
---

# Skill: Bitácora de Estudio y Registro de Prompts

Este skill define el procedimiento obligatorio para registrar cada indicación (prompt) del usuario y documentar cómo se atendió en el archivo `bitacora_de_estudio.md`.

## Ubicación del Archivo
- **Archivo principal**: `bitacora_de_estudio.md` en la raíz del proyecto.

## Estructura de Cada Entrada

En cada interacción o cambio significativo solicitado por el usuario, se debe registrar una nueva sección en `bitacora_de_estudio.md` siguiendo este formato estándar, asegurando incluir siempre el **Timestamp exacto** de la indicación:

```markdown
### Registro #[N] - [Título Corto de la Tarea]
- **Timestamp**: [YYYY-MM-DD HH:mm:ss (ej. 2026-09-08 08:55:13 -06:00)]
- **Indicación del Usuario (Prompt)**:
  > [Texto exacto del prompt recibido]
- **Objetivo**: [Resumen de la intención o meta técnica]
- **Acciones Realizadas / Cómo se atendió**:
  1. [Paso 1 ejecutado]
  2. [Paso 2 ejecutado / Archivos creados o modificados]
  3. [Verificación realizada]
- **Material / Entregables Generados**:
  - [Enlaces a archivos creados o actualizados]
- **Estado**: ✅ Completado / ⏳ En Progreso
```

## Procedimiento de Actualización

1. **Antes o durante la ejecución**: Identificar la indicación del usuario, obtener el timestamp actual y planificar las acciones necesarias.
2. **Durante la ejecución**: Implementar los cambios de código, documentación o materiales solicitados.
3. **Al finalizar la respuesta**: Asegurar que `bitacora_de_estudio.md` contenga la entrada actualizada con su respectivo **Timestamp**, reflejando fielmente lo implementado.
