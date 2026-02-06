# 🧠 Sistema de Predicción de Estrés Académico
**Investigación formativa - Universidad Nacional de Chimborazo**

Este proyecto es una aplicación web interactiva que utiliza **Machine Learning** para analizar y predecir los niveles de estrés en estudiantes basados en factores académicos y del entorno.

## 🚀 Características
- **Modularidad:** Código organizado en módulos independientes (Limpieza, Modelo, Visualización).
- **Interactividad:** Gráficos dinámicos realizados con Plotly con opción de descarga en PNG.
- **Robustez:** Manejo de excepciones personalizadas (ArchivoInvalidoError) y bloques try-except-finally.
- **Modelado:** Optimización de hiperparámetros en el Árbol de Decisión para evitar sobreajuste.

## 📁 Estructura del Paquete
- `app.py`: Servidor Flask y gestión de rutas.
- `preprocesamiento.py`: Limpieza de nulos y preparación de datos.
- `modelo.py`: Entrenamiento de modelos con Scikit-Learn.
- `visualizacion.py`: Generación de gráficos interactivos.
- `academic Stress level - maintainance 1.csv`: Dataset utilizado.

## 🛠️ Instalación y Uso
1. Instalar dependencias: `pip install flask pandas scikit-learn plotly`
2. Ejecutar la aplicación: `python app.py`
3. Abrir en el navegador: `http://127.0.0.1:5000`

## 👤 Autora
**Guadalupe Janeta** - Paralelo A - Programación II (UNACH)