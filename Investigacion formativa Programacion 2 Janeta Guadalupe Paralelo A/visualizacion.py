import pandas as pd
import plotly.express as px
import plotly.io as pio

def crear_grafico_resultados(y_test, y_pred):
    try:
        # Creamos un DataFrame para comparar valores reales vs predicciones
        df_res = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
        
        # Generamos un gráfico de dispersión interactivo
        fig = px.scatter(df_res, x='Real', y='Predicción', 
                         title='Comparación: Valores Reales vs Predicciones de Estrés',
                         labels={'Real': 'Nivel Real', 'Predicción': 'Nivel Predicho'},
                         template='plotly_white')
        
        # Esto permite que el gráfico sea interactivo en la web
        graph_html = pio.to_html(fig, full_html=False)
        return graph_html
    except Exception as e:
        raise Exception(f"Error al generar la visualización: {str(e)}")