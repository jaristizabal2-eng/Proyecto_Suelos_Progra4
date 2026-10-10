import pandas as pd

def obtener_datos_excel(ruta_archivo, departamento, municipio, cultivo, limite):
    try:
        df = pd.read_excel(ruta_archivo)
    except FileNotFoundError:
        return None, "Error: No se encontró el archivo Excel."

    # Normalizar todo a minúsculas para evitar errores
    df.columns = df.columns.str.lower()
    
    # Filtrar
    filtro = (
        (df['departamento'].str.lower() == departamento.lower()) &
        (df['municipio'].str.lower() == municipio.lower()) &
        (df['cultivo'].str.lower() == cultivo.lower())
    )
    
    df_filtrado = df[filtro].head(limite)
    
    if df_filtrado.empty:
        return None, "No se encontraron registros para esa búsqueda."

    return df_filtrado, "Éxito"

def calcular_medianas(df):
    col_ph = 'ph' 
    col_fosforo = 'fósforo' 
    col_potasio = 'potasio'
    
    mediana_ph = df[col_ph].median() if col_ph in df.columns else 0
    mediana_p = df[col_fosforo].median() if col_fosforo in df.columns else 0
    mediana_k = df[col_potasio].median() if col_potasio in df.columns else 0
    
    return mediana_ph, mediana_p, mediana_k