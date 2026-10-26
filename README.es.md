**🌐 Language：** [中文](README.md) | [English](README.en.md) | [日本語](README.ja.md) | **Español** | [Français](README.fr.md) | [Deutsch](README.de.md) | [한국어](README.ko.md) | [Русский](README.ru.md)

> ⚠️ **Declaración de Generación por IA**
> Este documento (incluyendo el texto de la especificación y la plantilla) fue redactado y generado por IA, y revisado por un humano. Predicamos con el ejemplo practicando los principios de transparencia que promueve esta especificación.

> 💡 **Restricciones del Entorno de Desarrollo:** Si este proyecto no puede completar todas las pruebas debido a limitaciones de hardware o entorno, consulte [Restricciones de Desarrollo](DEVELOPMENT_CONSTRAINTS.es.md).

---

# Directrices de Desarrollo con IA

### Una especificación para divulgar, revisar y asumir la responsabilidad del código generado por IA

## Tabla de Contenidos

- [Por qué existe esta especificación](#por-qué-existe-esta-especificación)
- [Principios Rectores](#principios-rectores)
- [La Especificación](#la-especificación)
  - [1. Responsabilidad](#1-responsabilidad)
  - [2. Alcance de Uso](#2-alcance-de-uso)
  - [3. Generación y Revisión](#3-generación-y-revisión)
  - [4. Verificación](#4-verificación)
  - [5. Divulgación](#5-divulgación)
  - [6. Seguridad y Cumplimiento](#6-seguridad-y-cumplimiento)
  - [7. Documentación y Trazabilidad](#7-documentación-y-trazabilidad)
- [Plantilla de Declaración de IA](#plantilla-de-declaración-de-ia)
- [Preguntas Frecuentes](#preguntas-frecuentes)
- [Versionado](#versionado)
- [Adoptando esta Especificación](#adoptando-esta-especificación)
- [Licencia](#licencia)

---

## Por qué existe esta especificación

La IA ahora puede escribir código que compila, se ejecuta y se publica. La pregunta ya no es *si* la IA puede escribirlo, sino:

- Quién es **responsable** cuando algo falla;
- Qué partes fueron generadas y cuáles revisadas — **nadie puede saberlo**;
- Funciones de alto riesgo llegan a producción porque la IA las escribió — **nadie las detiene**;
- Los proyectos afirman tener "desarrollo asistido por IA" **sin un estándar de divulgación verificable**.

Esta especificación define un conjunto mínimo de convenciones: **los humanos poseen las decisiones y la aceptación, la IA genera, y el contenido generado debe ser verificable, divulgable y responsable.**

Esta especificación no clasifica las herramientas de IA ni exige un modelo específico.

---

## Principios Rectores

1. **Los humanos son responsables.** La IA no es autora ni parte responsable.
2. **Generado no es lo mismo que utilizable.** El código que no ha sido compilado, revisado y verificado no está terminado.
3. **El rigor de la revisión escala con el privilegio.** Cuanto más cerca esté el código de la autenticación, el sistema de archivos, la ejecución de comandos o los pipelines de lanzamiento, más estricta será la revisión.
4. **Seguro y desactivado por defecto.** Las capacidades de alto riesgo están desactivadas por defecto; habilitarlas requiere confirmación explícita y un registro.
5. **Divulgar con veracidad.** Escribe "aproximadamente 80%" en lugar de "completamente generado por IA" sin ofrecer un rastro de verificación.

---

## La Especificación

Las palabras clave **DEBE**, **DEBERÍA** y **PUEDE** deben interpretarse como se describe en [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

### 1. Responsabilidad

1.1 Un proyecto **DEBE** designar al menos a un mantenedor humano responsable de las fusiones y lanzamientos.  
1.2 Las decisiones de fusionar, lanzar, eliminar datos o cambiar permisos **DEBEN** ser tomadas por un humano y **NO DEBEN** ser automatizadas por IA.  
1.3 Un proyecto **DEBERÍA** declarar en su documentación que la IA participa en la generación mientras los humanos poseen la aceptación.

### 2. Alcance de Uso

2.1 Lo siguiente **PUEDE** ser generado directamente por IA, sujeto a compilación y revisión básica: código repetitivo, diseños de UI, estilos, borradores de documentación, comentarios, borradores de pruebas y scripts de construcción.  
2.2 Lo siguiente **DEBE** recibir revisión humana línea por línea: autenticación y sesiones, cifrado y certificados, validación de rutas y sandbox, análisis de protocolos, ejecución de comandos, migraciones de bases de datos, y secretos/scripts de lanzamiento de CI/CD.  
2.3 Un proyecto **NO DEBE** enviar secretos reales, certificados, tokens o datos de usuarios a servicios públicos de IA.  
2.4 Las capacidades de alto riesgo (acceso root, acceso a disco completo, ejecución remota de comandos, autodestrucción, tunneling, etc.) **NO DEBEN** estar habilitadas por defecto y **DEBEN** ser advertidas por separado en la documentación de seguridad.  
2.5 Un proyecto **NO DEBE** exagerar ni subestimar su participación de IA en los documentos de divulgación.

### 3. Generación y Revisión

3.1 Cada generación de IA **DEBERÍA** basarse en un contexto explícito: objetivos, restricciones, plataforma objetivo, archivos relevantes y registros de errores.  
3.2 El código generado por IA **DEBE** ser revisado por un humano antes de llegar a la rama principal.  
3.3 La revisión **DEBERÍA** cubrir como mínimo: corrección lógica, manejo de errores, necesidad de dependencias, si las API de la plataforma existen realmente y compatibilidad de licencias.  
3.4 Los cambios generados grandes **DEBERÍAN** confirmarse por separado para facilitar el seguimiento y la reversión.  
3.5 Los mensajes de confirmación **PUEDEN** etiquetarse como `ai-assisted`, o la descripción del PR **PUEDE** indicar el alcance de la participación de la IA.

### 4. Verificación

4.1 El código generado por IA **DEBE** compilar al menos una vez en la plataforma objetivo.  
4.2 Los cambios que involucren API de plataforma, permisos, UI, supervivencia en segundo plano o redes **DEBEN** verificarse en dispositivos o entornos reales.  
4.3 La lógica central (analizadores, validación de rutas, autenticación, cargas fragmentadas, etc.) **DEBERÍA** tener pruebas repetibles.  
4.4 "La IA dijo que está bien" **NO** constituye una verificación.  
4.5 Después de recortar, portar o refactorizar, **DEBERÍA** realizarse una regresión completa.

### 5. Divulgación

5.1 Un proyecto **DEBERÍA** proporcionar un archivo de declaración de IA en el repositorio (recomendado: `AI_DISCLOSURE.md`).  
5.2 La divulgación **DEBE** incluir: el alcance de la participación de la IA, el trabajo realizado por los humanos, las limitaciones y riesgos conocidos, y los términos de licencia.  
5.3 La divulgación **DEBE** actualizarse cuando: la participación cambie materialmente, se agregue un nuevo módulo de alto riesgo, se cree una nueva rama o port, o se lance una versión principal.  
5.4 La divulgación **DEBERÍA** incluir una fecha de última actualización.  
5.5 El archivo de divulgación **NO DEBE** sustituir a la documentación de seguridad; las capacidades de alto riesgo **DEBEN** documentarse por separado.

### 6. Seguridad y Cumplimiento

6.1 Los secretos y certificados **DEBEN** inyectarse a través de almacenes de secretos o variables de entorno y **NO DEBEN** ingresar al repositorio.  
6.2 Antes de adoptar una dependencia de terceros sugerida por IA, un proyecto **DEBERÍA** evaluar su licencia, tamaño, estado de mantenimiento y registro de seguridad.  
6.3 El audio, las imágenes y el texto generados **DEBEN** llevar un aviso de que los usuarios deben cumplir con los términos de servicio y los requisitos de derechos de autor correspondientes.  
6.4 Los certificados autofirmados, las listas negras de cadenas y la validación del lado del cliente **NO DEBEN** describirse como "auditados de seguridad".

### 7. Documentación y Trazabilidad

7.1 La documentación **DEBERÍA** reflejar con precisión el código actual y **NO DEBE** describir características planificadas como enviadas.  
7.2 El número de versión **DEBERÍA** tener una única fuente de verdad (por ejemplo, `CHANGELOG.md`) inyectada por CI.  
7.3 Las ramas, ediciones lite y ports **DEBEN** documentar su relación de herencia con el upstream.  
7.4 El Markdown generado por IA **DEBERÍA** revisarse manualmente para nombres de ramas, enlaces de repositorio y rutas relativas.

---

## Plantilla de Declaración de IA

Los nuevos proyectos pueden copiar lo siguiente en `AI_DISCLOSURE.md`:

```markdown
# Declaración de IA

Este proyecto ({{nombre del proyecto}}) utilizó modelos de lenguaje grandes durante {{desarrollo/refactorización/port/recorte}}.

**Declaración central: aproximadamente el {{porcentaje}} del código fue generado directamente por IA; los desarrolladores humanos se encargaron de {{definición del producto, revisión, pruebas, aceptación y lanzamiento}}.**

## Dónde estuvo involucrada la IA
- `{{archivo o módulo}}`: {{qué se generó y por qué}}

## Qué hicieron los humanos
- {{requisitos / decisiones de arquitectura / depuración de compilación / pruebas en dispositivos / aceptación final}}

## Limitaciones Conocidas
1. {{La IA no puede ejecutarse en hardware real; las diferencias de plataforma requieren verificación humana}}
2. {{cambios en la API de la plataforma, casos extremos, riesgos de seguridad, etc.}}

## Licencia
Este proyecto se publica bajo {{licencia}}.
```

---

## Preguntas Frecuentes

**¿El porcentaje de IA necesita ser exacto?**  
No. Debe ser conservador y honesto, y declarar la base (por línea, por módulo o por característica).

**¿Los proyectos pequeños también necesitan divulgación?**  
Recomendado. La divulgación es barata; no poder explicar lo que sucedió es costoso.

**¿Puede un humano ser responsable sin escribir una sola línea?**  
Sí, siempre que el humano haya realizado la definición de requisitos, la revisión, la verificación y las decisiones de lanzamiento. La responsabilidad proviene de las decisiones y la aceptación, no de las pulsaciones de teclas.

---

## Versionado

Esta especificación sigue el [Versionado Semántico](https://semver.org/lang/es/):

- **Mayor**: cambios incompatibles en las cláusulas;
- **Menor**: nuevas cláusulas o secciones;
- **Parche**: aclaraciones de redacción y correcciones de errores tipográficos.

Versión actual: **1.0.0**

---

## Adoptando esta Especificación

En tu proyecto:

1. Copia este archivo a `docs/AI-DEVELOPMENT-GUIDELINES.md`;
2. Enlázalo desde `README.md` y `CONTRIBUTING.md`;
3. Crea `AI_DISCLOSURE.md` usando la [plantilla](#plantilla-de-declaración-de-ia);
4. Agrega tres comprobaciones a tu plantilla de PR: "participación de IA declarada", "compilado en la plataforma objetivo" y "código sensible a la seguridad revisado".

---

## Licencia

Esta especificación se publica bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es). Puedes citarla, modificarla y redistribuirla libremente, siempre que se preserve la atribución.
