# Design Document (Documento de Diseño) del Proyecto: Bot de Chat Multifuncional

## 1. Título y Resumen
**Título**: Bot de Chat Multifuncional

**Resumen**: Este proyecto es un bot de chat que proporciona funcionalidades de conversión de divisas, búsqueda en Wikipedia y mantiene un registro de las conversaciones. Está diseñado para mejorar la eficiencia y facilidad de acceso a información mediante una interfaz gráfica intuitiva.

## 2. Introducción
**Descripción General**: El bot de chat multifuncional permite a los usuarios realizar conversiones de divisas, buscar información en Wikipedia y mantener un historial de conversaciones, todo desde una interfaz gráfica simple. El proyecto utiliza Python y diversas bibliotecas para implementar estas funcionalidades.

**Alcance**: El proyecto incluye las funcionalidades de conversión de divisas, búsqueda en Wikipedia y registro de conversaciones. No incluye integración con servicios de mensajería externa ni funcionalidades avanzadas de procesamiento de lenguaje natural.

## 3. Requisitos del Proyecto
**Funcionales**:
- El bot debe responder a preguntas básicas en español.
- El bot debe ser capaz de convertir cantidades de una moneda a otra.
- El bot debe poder buscar términos en Wikipedia y devolver resúmenes.
- El bot debe mantener un historial de conversaciones en una base de datos.

**No Funcionales**:
- El bot debe responder en menos de 2 segundos.
- El bot debe ser fácil de usar e intuitivo.
- La interfaz gráfica debe ser clara y accesible.

## 4. Arquitectura del Sistema
**Diagrama de Arquitectura**:

Usuario <-> Interfaz Gráfica (Tkinter) <-> Bot de Chat (ChatterBot)
|                                   |
|                                   |
Conversión de Divisas (forex-python)    Búsqueda en Wikipedia (wikipedia-api)
|                                   |
|                                   |
––––––––> Base de Datos (SQLite) <––––––––

**Descripción de Componentes**:
- **Interfaz de Usuario (UI)**: Implementada con Tkinter, permite a los usuarios interactuar con el bot a través de una ventana gráfica.
- **ChatBot**: Utiliza ChatterBot para responder a preguntas básicas y mantener conversaciones en español.
- **Conversión de Divisas**: Utiliza la biblioteca forex-python para convertir montos entre diferentes monedas.
- **Búsqueda en Wikipedia**: Usa la biblioteca wikipedia-api para buscar términos y devolver resúmenes de artículos.
- **Base de Datos**: SQLite se utiliza para almacenar las conversaciones del usuario con el bot.

## 5. Diseño Detallado
**Flujo de Trabajo**:
1. El usuario ingresa un comando en la interfaz gráfica.
2. El bot procesa el comando y determina si es una consulta de conversión de divisas, una búsqueda en Wikipedia o una conversación básica.
3. El bot genera la respuesta correspondiente y la muestra en la interfaz gráfica.
4. La conversación se almacena en la base de datos.

**Interfaces de Usuario (UI)**:
- **Ventana Principal**: Muestra un área de texto para la conversación y un campo de entrada para los comandos del usuario.
- **Botón de Enviar**: Permite al usuario enviar el comando ingresado al bot.

## 6. Tecnologías y Herramientas
**Lenguajes de Programación**: Python

**Bibliotecas y Herramientas**:
- **Tkinter**: Para la interfaz gráfica.
- **ChatterBot**: Para el bot de chat.
- **forex-python**: Para la conversión de divisas.
- **wikipedia-api**: Para la búsqueda en Wikipedia.
- **SQLite**: Para la base de datos.
- **Flask**: Para la API RESTful.
- **Git y GitHub**: Para el control de versiones y el repositorio.

## 7. Plan de Implementación
**Cronograma**:
- **Semana 1**: 
  - Configuración del entorno de desarrollo y creación del entorno virtual.
  - Instalación de las bibliotecas necesarias.
- **Semana 2**:
  - Implementación del bot básico con ChatterBot.
  - Pruebas iniciales de conversación.
- **Semana 3**:
  - Agregar funcionalidades de conversión de divisas.
  - Agregar funcionalidades de búsqueda en Wikipedia.
- **Semana 4**:
  - Integración con la base de datos SQLite.
  - Implementación de la API RESTful con Flask.
  - Pruebas finales y validación.

**Tareas y Responsabilidades**:
- **Configuración del Entorno y Bibliotecas**: Configurar el entorno de desarrollo y asegurar que todas las bibliotecas necesarias estén instaladas.
- **Desarrollo del Bot Básico**: Implementar el bot básico utilizando ChatterBot y realizar pruebas iniciales.
- **Funcionalidades Adicionales**: Implementar y probar las funcionalidades de conversión de divisas y búsqueda en Wikipedia.
- **Integración y Pruebas Finales**: Integrar todas las funcionalidades, implementar la API RESTful, realizar pruebas finales y validar el sistema.
- **Documentación**: Crear y mantener la documentación del proyecto, incluyendo este documento de diseño.

## 8. Pruebas y Validación
**Plan de Pruebas**:
- Realizar pruebas unitarias para cada funcionalidad (conversión de divisas, búsqueda en Wikipedia, respuestas básicas).
- Probar la integración de todas las funcionalidades con la interfaz gráfica.
- Verificar el correcto almacenamiento y recuperación de conversaciones en la base de datos.

**Criterios de Aceptación**:
- El bot debe responder correctamente a las consultas de divisas y Wikipedia.
- El bot debe mantener un historial de conversaciones preciso.
- La interfaz debe ser funcional y permitir una interacción fluida con el usuario.

## 9. Subir el Proyecto al Repositorio
1. Inicializar el Repositorio Git:
    ```sh
    git init
    git add .
    git commit -m "Initial commit"
    ```

2. Crear el Repositorio en GitHub: 
    - Ir a GitHub, crea un nuevo repositorio y sigue las instrucciones para conectar tu repositorio local. (https://github.com/MacielSergio29/2-AUTOMATAS.git)

3. Subir los Archivos a GitHub:
    ```sh
    git remote add origin https://github.com/MacielSergio29/2-AUTOMATAS.git
    git branch -M main
    git push -u origin main
    ```