from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def entrenar_modelos(df):
    try:
        # 1. BUSCAMOS LA COLUMNA OBJETIVO DINÁMICAMENTE
        # Esto busca cualquier columna que tenga la palabra 'stress' o 'Stress'
        posibles_columnas = [col for col in df.columns if 'stress' in col.lower()]
        
        if not posibles_columnas:
            raise Exception("No se encontró una columna que contenga la palabra 'Stress' en el CSV.")
        
        target = posibles_columnas[0] # Usamos la primera que encuentre
        
        X = df.drop(target, axis=1)
        y = df[target]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Modelo 1: Regresión Logística
        log_model = LogisticRegression(max_iter=1000)
        log_model.fit(X_train, y_train)
        pred_log = log_model.predict(X_test)
        acc_log = accuracy_score(y_test, pred_log)
        
        # Modelo 2: Árbol de Decisión
        tree_model = DecisionTreeClassifier(
        max_depth=5,
        min_samples_split=10,
        min_samples_leaf=5,
        random_state=42
        )

        tree_model.fit(X_train, y_train)
        pred_tree = tree_model.predict(X_test)
        acc_tree = accuracy_score(y_test, pred_tree)
        
        # 2. DEVOLVEMOS TAMBIÉN y_test y pred_tree PARA EL GRÁFICO (Punto 4 de la rúbrica)
        return acc_log, acc_tree, y_test, pred_tree
        
    except Exception as e:
        raise Exception(f"Error al entrenar el modelo: {str(e)}")