import pandas as pd

def limpiar_datos(df):
    try:
        # Reemplazo de nulos por la media (lo que ya hicimos)
        df.fillna(df.mean(numeric_only=True), inplace=True)
        
        # Codificación de variables (Dummies)
        df = pd.get_dummies(df, drop_first=True)
        
        return df
    except Exception as e:
        raise Exception(f"Error en el preprocesamiento: {str(e)}")