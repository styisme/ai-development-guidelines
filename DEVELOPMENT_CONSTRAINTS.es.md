**🌐 Language：** [中文](DEVELOPMENT_CONSTRAINTS.md) | [English](DEVELOPMENT_CONSTRAINTS.en.md) | [日本語](DEVELOPMENT_CONSTRAINTS.ja.md) | **Español** | [Français](DEVELOPMENT_CONSTRAINTS.fr.md) | [Deutsch](DEVELOPMENT_CONSTRAINTS.de.md) | [한국어](DEVELOPMENT_CONSTRAINTS.ko.md) | [Русский](DEVELOPMENT_CONSTRAINTS.ru.md)

---

# Restricciones del Entorno de Desarrollo y Plantilla de Divulgación Honesta

> Copia esta plantilla en tu proyecto, marca y completa según las condiciones reales. Este documento explica las condiciones reales de desarrollo y los límites de responsabilidad de este repositorio.

## I. Entorno de Desarrollo (Marcar según corresponda)

- [ ] Tiene IDE / SDK local, puede compilar localmente
- [ ] Tiene herramientas diff locales, puede revisar línea por línea
- [ ] Puede ejecutar lint / pruebas unitarias
- [ ] Sigue el flujo estándar de PR (fork → PR → review)
- [ ] **Depende únicamente de la compilación en CI en la nube (sin toolchain local)**
- [ ] **Desarrolla únicamente en móvil / smartwatch**
- [ ] **Push directo a master (sin flujo de PR)**

> Los elementos no marcados significan que **físicamente es imposible ejecutarlos en este repositorio**, no que se "ignoraron".

## II. Mecanismos Realmente Implementados (Marcar lo que se hizo)

### Divulgación
- [ ] Proporciona `AI_DISCLOSURE.md` explicando la participación y el porcentaje de IA
- [ ] Enlaza a este archivo en la parte superior del README
- [ ] Mensaje de confirmación etiquetado con `[ai-assisted]`

### Funciones de Alto Riesgo
- [ ] Funciones de alto riesgo desactivadas por defecto (a nivel de código, no solo en documentos)
- [ ] Sección de advertencia separada para funciones de alto riesgo (ver `SECURITY.md` o equivalente)
- [ ] Confirmación explícita requerida antes de usar funciones de alto riesgo

### Puertas (Gates)
- [ ] **Lanzamiento solo después de que pase la compilación de CI** (la única puerta automatizada en este proyecto)
- [ ] Los artefactos de lanzamiento tienen números de versión y etiquetas
- [ ] `CHANGELOG.md` registra cada cambio

### Pruebas
- [ ] **Pruebas en dispositivos reales** (dispositivos físicos reales)
- [ ] **Pruebas en emuladores** (cuando no hay dispositivos físicos disponibles)
- [ ] **Sin probar** (ver divulgación honesta abajo)

> Los elementos no marcados significan que **este repositorio no tiene condiciones para hacerlo**, no que se "olvidó hacerlo".

## III. Divulgación Honesta

**Las siguientes situaciones deben declararse con veracidad, sin adornos:**

- Si este repositorio **no ha realizado ninguna prueba en dispositivos reales o emuladores**, indíquelo claramente aquí:
  > "El código de este repositorio no ha sido probado en dispositivos reales. Pasar la compilación de CI solo significa que la sintaxis y las dependencias son correctas, no que las funciones funcionen. Evalúe los riesgos usted mismo antes de usarlo."

- Si un módulo es **sensible pero no está verificado**, márquelo como `⚠️ No verificado` en la lista de abajo.

- Si una función está **habilitada por defecto** (violando el principio de "alto riesgo desactivado por defecto"), indique el motivo claramente.

## IV. Lista de Módulos Sensibles (Completar según las condiciones reales)

| Módulo | Estado de Verificación |
|---|---|
| `{{tu módulo de autenticación}}` | ✅ Dispositivo real / ⚠️ Solo CI / ❌ No verificado |
| `{{tu módulo de sistema de archivos}}` | ✅ Dispositivo real / ⚠️ Solo CI / ❌ No verificado |
| `{{tu módulo de análisis de protocolos}}` | ✅ Dispositivo real / ⚠️ Solo CI / ❌ No verificado |
| `{{tu script de lanzamiento de CI/CD}}` | ✅ Dispositivo real / ⚠️ Solo CI / ❌ No verificado |

> Los módulos marcados como `❌ No verificado` **no son necesariamente no publicables**, pero evalúe los riesgos antes de usarlos.

## V. Admitimos que esto no es perfecto

Los procesos formales de PR, las revisiones de código línea por línea y el análisis estático local **pueden estar totalmente ausentes** en algunos repositorios.

Asumimos **responsabilidad sustantiva** a través de "**Divulgación + Puertas (lo que podemos hacer) + Desactivado por defecto**", en lugar de fingir que cumplimos con todas las **responsabilidades formales**.

Esta es una elección bajo restricciones, no un rechazo a los estándares.
