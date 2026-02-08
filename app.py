from flask import Flask, render_template, request
import pandas as pd
from preprocesamiento import limpiar_datos
from modelo import entrenar_modelos
from visualizacion import crear_grafico_resultados

app = Flask(__name__)

# --- ESTRUCTURA DE DATOS (Para la otra materia) ---
class AnalizadorEstructuras:
    def __init__(self, datos):
        # Almacenamos los datos en un Arreglo (Estructura Lineal)
        self.datos = list(datos)

    def calcular_media_manual(self):
        # Recorrido de un array (O(n))
        if not self.datos: return 0
        suma = 0
        for valor in self.datos:
            suma += valor
        return suma / len(self.datos)

    def obtener_mediana_manual(self):
        # Algoritmo de Ordenamiento para encontrar la tendencia central
        datos_ordenados = sorted(self.datos)
        n = len(datos_ordenados)
        if n % 2 == 0:
            return (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
        else:
            return datos_ordenados[n//2]

# 5. EXCEPCIÓN PERSONALIZADA
class ArchivoInvalidoError(Exception):
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            file = request.files['file']
            if not file or not file.filename.endswith('.csv'):
                raise ArchivoInvalidoError("Por favor, sube un archivo CSV válido.")

            # 1. Procesamiento de datos (Arrays/Matrices)
            df = pd.read_csv(file)
            df_limpio = limpiar_datos(df)
            
            # 2. IA y Estructuras No Lineales (Árboles)
            acc_log, acc_tree, y_test, y_pred = entrenar_modelos(df_limpio)
            
            # 3. Aplicando conceptos de Estructura de Datos manualmente
            analizador = AnalizadorEstructuras(y_pred)
            media_estres = analizador.calcular_media_manual()
            mediana_estres = analizador.obtener_mediana_manual()
            
            # 4. Visualización Interactiva
            grafico_html = crear_grafico_resultados(y_test, y_pred)
            
            # DISEÑO MEJORADO (Dashboard)
            return f"""
            <html>
            <head>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <title>Investigación UNACH</title>
            </head>
            <body class="bg-light p-5">
                <div class="container bg-white shadow p-4 rounded">
                    <h1 class="text-primary border-bottom pb-2"> Reporte de Investigación Académica</h1>
                    
                    <div class="row mt-4">
                        <div class="col-md-4">
                            <div class="card border-primary mb-3">
                                <div class="card-header bg-primary text-white">Exactitud (IA)</div>
                                <div class="card-body"><h2 class="card-title">{acc_tree:.2%}</h2></div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="card border-success mb-3">
                                <div class="card-header bg-success text-white">Media (Estructuras)</div>
                                <div class="card-body"><h2 class="card-title">{media_estres:.2f}</h2></div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="card border-info mb-3">
                                <div class="card-header bg-info text-white">Mediana (Algoritmos)</div>
                                <div class="card-body"><h2 class="card-title">{mediana_estres:.2f}</h2></div>
                            </div>
                        </div>
                    </div>

                    <div class="mt-4">
                        <h3>Interpretación de Nodos y Ramas</h3>
                        <div class="p-3 border rounded bg-white">{grafico_html}</div>
                    </div>

                    <div class="mt-4 p-3 bg-secondary text-white rounded">
                        <h5>Nota Técnica para Estructura de Datos:</h5>
                        <p>El modelo utiliza una <b>Estructura Dinámica No Lineal</b> (Árbol de Decisión) para clasificar los niveles de estrés. 
                        Los cálculos de tendencia central fueron realizados recorriendo el <b>Arreglo</b> de predicciones manualmente.</p>
                    </div>

                    <div class="mt-4 text-center">
                        <a href="/" class="btn btn-primary btn-lg">Realizar nuevo análisis</a>
                    </div>
                </div>
            </body>
            </html>
            """
        
        except ArchivoInvalidoError as e:
            return f"<div class='alert alert-danger'><h1>Error</h1><p>{str(e)}</p></div><a href='/'>Volver</a>"
        except Exception as e:
            return f"<div class='alert alert-warning'><h1>Error Interno</h1><p>{str(e)}</p></div><a href='/'>Volver</a>"
        finally:
            print("Procesamiento de estructuras finalizado.")

    return """
    <html>
    <head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"></head>
    <body class="bg-light d-flex align-items-center" style="height:100vh;">
        <div class="container text-center bg-white p-5 shadow rounded">
            <h1 class="text-primary mb-4">Investigación Formativa: Estrés Académico</h1>
            <p class="lead">Sube el CSV para procesar mediante IA y Estructuras de Datos</p>
            <form method="post" enctype="multipart/form-data" class="mt-4">
                <input type="file" name="file" accept=".csv" class="form-control mb-3">
                <button type="submit" class="btn btn-primary w-100">Analizar Datos</button>
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)