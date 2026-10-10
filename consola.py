def pedir_datos_usuario():
    print("\n--- CONSULTA DE ANÁLISIS DE SUELOS ---")
    departamento = input("1. Ingrese el Departamento (ej. Risaralda): ")
    municipio = input("2. Ingrese el Municipio (ej. Pereira): ")
    cultivo = input("3. Ingrese el Cultivo: ")
    limite = int(input("4. Número de registros a consultar: "))
    return departamento, municipio, cultivo, limite

def mostrar_tabla(df_filtrado, mediana_ph, mediana_p, mediana_k):
    print("\n" + "="*60)
    print(" TABLA DE RESULTADOS ".center(60, "="))
    print("="*60)
    
    columnas_mostrar = ['departamento', 'municipio', 'cultivo', 'topografia']
    columnas_existentes = [col for col in columnas_mostrar if col in df_filtrado.columns]
    
    print(df_filtrado[columnas_existentes].to_string(index=False))
    
    print("\n" + "-"*60)
    print(" MEDIANAS DE LAS VARIABLES EDÁFICAS ".center(60, "-"))
    print("-"*60)
    print(f"Mediana pH:          {mediana_ph}")
    print(f"Mediana Fósforo (P): {mediana_p}")
    print(f"Mediana Potasio (K): {mediana_k}")
    print("="*60 + "\n")