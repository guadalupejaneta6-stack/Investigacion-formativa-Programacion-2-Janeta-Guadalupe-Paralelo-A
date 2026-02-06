from flask import Flask, render_template, request, send_file
import pandas as pd
import io
from preprocesamiento import limpiar_datos
from modelo import entrenar_modelos
from visualizacion import crear_grafico_resultados

app = Flask(__name__)

# 5. EXCEPCIÓN PERSONALIZADA (Punto 5 de la rúbrica)
class ArchivoInvalidoError(Exception):
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try: # 5. MANEJO DE EXCEPCIONES (Punto 5)
            file = request.files['file']
            if not file or not file.filename.endswith('.csv'):
                raise ArchivoInvalidoError("Por favor, sube un archivo CSV válido.")

            # Carga y Procesamiento
            df = pd.read_csv(file)
            df_limpio = limpiar_datos(df)
            
            # Entrenamiento
            acc_log, acc_tree, y_test, y_pred = entrenar_modelos(df_limpio)
            
            # 4. VISUALIZACIÓN INTERACTIVA (Punto 4)
            # Generamos el HTML del gráfico de Plotly
            grafico_html = crear_grafico_resultados(y_test, y_pred)
            
            return f"""
                <h1>Resultados del Modelo</h1>
                <p>Exactitud Árbol de Decisión: {acc_tree:.2f}</p>
                <div style="width:100%">{grafico_html}</div>
                <br>
                <p><i>Nota: Plotly permite descargar como PNG usando el icono de cámara en el gráfico.</i></p>
                <a href="/">Volver a intentar</a>
            """
        
        except ArchivoInvalidoError as e:
            return f"<h1>Error de Usuario</h1><p>{str(e)}</p><a href='/'>Volver</a>"
        except Exception as e:
            return f"<h1>Error Interno</h1><p>Ocurrió un problema: {str(e)}</p><a href='/'>Volver</a>"
        finally:
            print("Intento de procesamiento finalizado.")

    return """
        <h1>Analizador de Estrés Académico - UNACH</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".csv">
            <button type="submit">Analizar y Generar Gráfico</button>
        </form>
    """

if __name__ == '__main__':
    app.run(debug=True)